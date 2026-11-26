#!/usr/bin/env python3
"""Run a corpus entry under darnit-amber and judge the paper's claims from the attested outputs.

Amber records, signs and reruns an experiment; it does not know the paper. This script owns the
other half: it pins the artifact at the entry's commit, has Amber run the entry's command with the
entry's ``run.outputs`` as results, then reads each claim's ``measure`` out of the copies Amber
kept and compares the value with the paper's threshold. The verdict names the signed run it was
derived from, so anyone with the bundle can recompute it.

    run_entry.py run entries/x.yaml [--work runs] [--key key.pem] [--rerun]
    run_entry.py judge entries/x.yaml --run-dir runs/x/bundle/runs/<id>
    run_entry.py check entries/x.yaml [entries/y.yaml ...]

``run``   clone + ``darnit-amber run`` + judge; with ``--rerun`` also ``darnit-amber rerun
          --host-environment`` and judge the rerun. Writes ``<work>/<id>/verdict.json``.
``judge`` judge a run Amber already stored (its ``outputs/`` copies, checked against the statement).
``check`` judge the entry's own ``baseline.metrics`` without running anything (entry self-consistency).

Exit status: 0 when every verdict matches the entry's ``expected_verdict``, 1 when one does not,
2 when the run itself failed.

The comparison (``compare``, ``measure_claim``, ``overall_verdict``) is darnit-amber's own from
before claims left it (darnit 7190b2f), kept verbatim so verdicts do not change with the move.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
from collections.abc import Callable
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml

VERDICTS = ("REPRODUCED", "NOT_REPRODUCED", "NOT_COMPARABLE")


class EntryError(Exception):
    pass


# --- the judge: darnit-amber 7190b2f, run.py ------------------------------------------------------------------


def _parse_threshold(threshold: str) -> tuple[str, str]:
    t = str(threshold).strip()
    for op in ("==", "!=", "<=", ">=", "<", ">"):
        if t.startswith(op):
            return op, t[len(op) :].strip()
    return "==", t


_NUMBER = re.compile(r"[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")
_NUMBER_LIKE = re.compile(r"[+-]?(?:inf(?:inity)?|nan|0[xX][0-9a-fA-F_]+|[\d_]*\.?[\d_]+(?:[eE][+-]?[\d_]+)?)", re.I)


def _number(s: Any) -> Decimal | None:
    """A finite number in plain decimal notation, exactly as written; inf, nan and 1_000 are not numbers here."""
    if isinstance(s, bool):
        return None
    if isinstance(s, int):
        return Decimal(s)
    if isinstance(s, float):
        return Decimal(repr(s)) if math.isfinite(s) else None
    if not isinstance(s, str) or not _NUMBER.fullmatch(s.strip()):
        return None
    v = Decimal(s.strip())
    return v if v.is_finite() else None


def _plain(d: Decimal) -> str:
    with localcontext() as ctx:
        ctx.prec = len(d.as_tuple().digits) + 2
        return f"{d.normalize():f}"


def _exact_product(a: Decimal, b: Decimal) -> str:
    with localcontext() as ctx:
        ctx.prec = len(a.as_tuple().digits) + len(b.as_tuple().digits) + 2
        return _plain(a * b)


def compare(value: str, threshold: str, tolerance: Any) -> tuple[bool | None, str]:
    """``value`` against ``threshold`` (``op number`` or ``op text``): (holds, reason); None when not comparable."""
    op, want = _parse_threshold(threshold)
    a, b = _number(value), _number(want)
    tol = _number(tolerance) if tolerance is not None else Decimal(0)
    if tol is None or tol < 0:
        return None, f"tolerance {tolerance!r} is not a finite number >= 0"
    if a is None or b is None:
        for side, text in (("measured", value), ("threshold", want)):
            if _number(text) is None and isinstance(text, str) and _NUMBER_LIKE.fullmatch(text.strip()):
                return None, f"{side} {text!r} is not a finite number in plain decimal notation"
        if op in ("==", "!="):
            same = value.strip() == want.strip()
            return (same if op == "==" else not same), f"measured {value!r} {op} {want!r}"
        return None, f"{op} needs two numbers: measured {value!r}, threshold {want!r}"
    x, y, t = Fraction(a), Fraction(b), Fraction(tol)
    strict = {"==": x == y, "!=": x != y, "<=": x <= y, ">=": x >= y, "<": x < y, ">": x > y}[op]
    holds = {
        "==": abs(x - y) <= t,
        "!=": abs(x - y) > t,
        "<=": x <= y + t,
        ">=": x >= y - t,
        "<": x < y + t,
        ">": x > y - t,
    }[op]
    note = ""
    if tol:
        shown = _plain(tol)
        note = f" (holds only with tolerance {shown})" if holds and not strict else f" (tolerance {shown})"
    return holds, f"measured {value} {op} {want}" + note


def safe_rel(path: str) -> str:
    p = Path(path)
    if not path or p.is_absolute() or path.startswith(("/", "\\")) or ".." in p.parts or "\\" in path:
        raise EntryError(f"output path {path!r} is not a relative path inside the repository")
    return p.as_posix()


def claims_of(entry: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for c in entry.get("claims") or []:
        out.append(
            {
                "id": c.get("id") or c.get("metric"),
                "threshold": c.get("threshold"),
                "tolerance": c.get("tolerance"),
                "unit": c.get("unit"),
                "source": c.get("source"),
                "expected_verdict": c.get("expected_verdict"),
                "measure": c.get("measure"),
                "measured": None,
                "verdict": "NOT_COMPARABLE",
                "reason": "no measure declared for this claim",
            }
        )
    return out


def measure_claim(claim: dict[str, Any], read: Callable[[str], bytes | None]) -> None:
    """Fill measured, verdict and reason; never raises."""
    m = claim.get("measure")
    if not m:
        return
    try:
        path = safe_rel(str(m.get("file") or ""))
        data = read(path)
        if data is None:
            claim["reason"] = f"output {m.get('file')} not produced by the experiment"
            return
        found = re.search(m["regex"], data.decode(errors="replace"), re.M)
        if not found:
            claim["reason"] = f"regex did not match in {path}"
            return
        value = found.group(1) if found.groups() else found.group(0)
        if m.get("scale") is not None:
            n = _number(value)
            if n is None:
                claim["reason"] = f"scale given but {value!r} is not a number"
                return
            scale = _number(m["scale"])
            if scale is None:
                claim["reason"] = f"scale {m['scale']!r} is not a number"
                return
            value = _exact_product(n, scale)
        claim["measured"] = value
        if m.get("comparable") is False:
            claim["reason"] = m.get("reason") or "measured, but not on the paper's terms"
            return
        if claim.get("threshold") is None:
            claim["reason"] = "no threshold"
            return
        holds, reason = compare(value, claim["threshold"], claim.get("tolerance"))
        claim["reason"] = reason
        if holds is not None:
            claim["verdict"] = "REPRODUCED" if holds else "NOT_REPRODUCED"
    except Exception as e:  # noqa: BLE001 - a bad regex or spec is a failed measurement, not a crash
        claim["measured"] = None
        claim["verdict"] = "NOT_COMPARABLE"
        claim["reason"] = f"measurement failed: {type(e).__name__}: {e}"


def overall_verdict(claims: list[dict[str, Any]]) -> str:
    verdicts = [c["verdict"] for c in claims]
    if "NOT_REPRODUCED" in verdicts:
        return "NOT_REPRODUCED"
    if verdicts and all(v == "REPRODUCED" for v in verdicts):
        return "REPRODUCED"
    return "NOT_COMPARABLE"


# --- the entry -------------------------------------------------------------------------------------------------


def load_entry(path: Path) -> dict[str, Any]:
    entry = yaml.safe_load(path.read_text()) or {}
    for key in ("id", "artifact", "claims", "run", "expected_verdict"):
        if key not in entry:
            raise EntryError(f"{path}: entry has no {key!r}")
    if entry["expected_verdict"] not in VERDICTS:
        raise EntryError(f"{path}: expected_verdict {entry['expected_verdict']!r}")
    return entry


_URL = re.compile(r"https?://\S+?\.git\b|https?://(?:github\.com|gitlab\.com|codeberg\.org)/[^/\s]+/[^/\s)]+")


def artifact_source(entry: dict[str, Any]) -> tuple[str, str]:
    """The git URL to clone and the commit to pin, from ``artifact.clone`` / ``artifact.url`` / ``artifact.ref``."""
    a = entry["artifact"]
    if a.get("ref_type") not in ("commit", "tag"):
        raise EntryError(f"artifact.ref_type {a.get('ref_type')!r}: only git artifacts can be run here")
    for text in (a.get("clone") or "", a.get("url") or ""):
        found = _URL.search(text)
        if found:
            url = found.group(0)
            url = url.removesuffix(".git")
            url = re.sub(r"/(?:tree|commit|blob)/.*$", "", url)
            return url, str(a["ref"])
    raise EntryError("no git URL in artifact.clone or artifact.url")


def judge(entry: dict[str, Any], read: Callable[[str], bytes | None]) -> dict[str, Any]:
    claims = claims_of(entry)
    for c in claims:
        measure_claim(c, read)
    baseline = (entry.get("baseline") or {}).get("metrics") or {}
    for c in claims:
        b = baseline.get(c["id"])
        c["baseline"] = None if b is None else str(b)
        c["matches_expected"] = c["expected_verdict"] in (None, c["verdict"])
    overall = overall_verdict(claims)
    return {
        "verdict": overall,
        "expected_verdict": entry["expected_verdict"],
        "matches_expected": overall == entry["expected_verdict"],
        "claims": claims,
    }


# --- Amber ----------------------------------------------------------------------------------------------------


def call(argv: list[str], **kw: Any) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, text=True, **kw)


def statement_of(run_dir: Path) -> dict[str, Any]:
    env = json.loads((run_dir / "amber.intoto.json").read_text())
    return json.loads(base64.b64decode(env["payload"]))


def reader_for_run(run_dir: Path) -> Callable[[str], bytes | None]:
    """Read an output from the run's ``outputs/`` copies, refusing a copy whose digest is not the attested one."""
    recorded = statement_of(run_dir)["predicate"]["outputs"]

    def read(path: str) -> bytes | None:
        want = recorded.get(path)
        copy = run_dir / "outputs" / path
        if want is None or not copy.is_file():
            return None
        data = copy.read_bytes()
        if hashlib.sha256(data).hexdigest() != want:
            raise EntryError(f"{path}: the copy in {run_dir} does not match the attested digest")
        return data

    return read


def reader_for_dir(root: Path) -> Callable[[str], bytes | None]:
    def read(path: str) -> bytes | None:
        p = root / path
        return p.read_bytes() if p.is_file() else None

    return read


def pin_checkout(url: str, ref: str, dest: Path) -> str:
    if dest.exists():
        shutil.rmtree(dest)
    call(["git", "clone", "-q", url, str(dest)], check=True)
    call(["git", "-C", str(dest), "checkout", "-q", ref], check=True)
    return call(["git", "-C", str(dest), "rev-parse", "HEAD"], capture_output=True, check=True).stdout.strip()


def amber_run(amber: str, checkout: Path, bundle: Path, entry: dict[str, Any], key: Path | None, timestamp: bool) -> Path:
    outputs = [safe_rel(o) for o in entry["run"].get("outputs") or []]
    argv = [amber, "run", str(checkout), "--output", str(bundle)]
    if key:
        argv += ["--key", str(key)]
    if not timestamp:
        argv.append("--no-timestamp")  # a run without a timestamp does not verify, so it cannot be rerun
    for o in outputs:
        argv += ["--results", o]
    argv += ["--", "sh", "-c", entry["run"]["command"]]
    r = call(argv)
    if r.returncode != 0:
        raise EntryError(f"darnit-amber run exited {r.returncode}")
    runs = sorted((bundle / "runs").iterdir(), key=lambda p: p.stat().st_mtime)
    if not runs:
        raise EntryError("darnit-amber run recorded nothing")
    return runs[-1]


def amber_rerun(amber: str, bundle: Path, run_id: str, checkout: Path, key: Path | None) -> tuple[Path, dict[str, Any]]:
    argv = [amber, "rerun", run_id, "--bundle", str(bundle), "--source", str(checkout), "--host-environment", "--no-shell", "--yes"]
    if key:
        argv += ["--key", str(key)]
    if (bundle / "key.pub").is_file():
        argv += ["--pubkey", str(bundle / "key.pub")]
    before = set((bundle / "reruns").iterdir()) if (bundle / "reruns").is_dir() else set()
    r = call(argv)
    after = set((bundle / "reruns").iterdir()) if (bundle / "reruns").is_dir() else set()
    new = sorted(after - before, key=lambda p: p.stat().st_mtime)
    if r.returncode != 0 or not new:
        raise EntryError(f"darnit-amber rerun exited {r.returncode}")
    here = new[-1]
    return here, json.loads((here / "result.json").read_text())


# --- commands -------------------------------------------------------------------------------------------------


def print_report(name: str, report: dict[str, Any]) -> None:
    flag = "" if report["matches_expected"] else f"  <-- expected {report['expected_verdict']}"
    print(f"{name}: {report['verdict']}{flag}")
    for c in report["claims"]:
        drift = "" if c["baseline"] in (None, c["measured"]) else f"  (baseline {c['baseline']})"
        bad = "" if c["matches_expected"] else f"  <-- expected {c['expected_verdict']}"
        print(f"   {str(c['id'])[:44]:44} {str(c['measured'])[:16]:16} {str(c['threshold'])[:20]:20} {c['verdict']:15}{drift}{bad}")
        if not c["matches_expected"]:
            print(f"      {c['reason']}")


def cmd_check(args: argparse.Namespace) -> int:
    bad = 0
    for path in args.entry:
        try:
            entry = load_entry(path)
        except EntryError as e:
            print(f"{path}: skipped ({e})")
            bad += 1
            continue
        metrics = (entry.get("baseline") or {}).get("metrics") or {}
        report = judge(entry, lambda p, m=metrics: json.dumps(m).encode())  # one JSON with every baseline metric
        print_report(entry["id"], report)
        bad += not report["matches_expected"]
    return 1 if bad else 0


def cmd_judge(args: argparse.Namespace) -> int:
    entry = load_entry(args.entry[0])
    report = judge(entry, reader_for_run(args.run_dir))
    report["run_id"] = args.run_dir.name
    print_report(entry["id"], report)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2) + "\n")
    return 0 if report["matches_expected"] else 1


def cmd_run(args: argparse.Namespace) -> int:
    entry = load_entry(args.entry[0])
    url, ref = artifact_source(entry)
    work = args.work / entry["id"]
    work.mkdir(parents=True, exist_ok=True)
    checkout, bundle = work / "checkout", work / "bundle"
    if bundle.exists():
        shutil.rmtree(bundle)
    commit = pin_checkout(url, ref, checkout)
    print(f"amber-corpus: {entry['id']}: {url} at {commit[:12]}", file=sys.stderr)

    run_dir = amber_run(args.amber, checkout, bundle, entry, args.key, args.timestamp)
    statement = statement_of(run_dir)
    report = judge(entry, reader_for_run(run_dir))
    report.update(
        {
            "entry": str(args.entry[0]),
            "run_id": run_dir.name,
            "bundle": str(bundle),
            "subject": statement["subject"][0],
            "exit_code": statement["predicate"]["exit_code"],
            "outputs": statement["predicate"]["outputs"],
        }
    )
    print_report(entry["id"], report)
    ok = report["matches_expected"]

    if args.rerun:
        here, result = amber_rerun(args.amber, bundle, run_dir.name, checkout, args.key)
        clone = here / Path(statement["subject"][0]["name"].rstrip("/")).name.removesuffix(".git")
        again = judge(entry, reader_for_dir(clone))
        again.update({"dir": str(here), "exit_code": result.get("exit_code"), "grade": result.get("grade"), "changed": result.get("changed")})
        print(f"rerun: outputs {result.get('grade')}, exit {result.get('exit_code')}", file=sys.stderr)
        print_report(entry["id"] + " (rerun)", again)
        report["rerun"] = again
        ok = ok and again["matches_expected"] and result.get("exit_code") == statement["predicate"]["exit_code"]

    (work / "verdict.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"amber-corpus: verdict in {work / 'verdict.json'} (run {run_dir.name[:12]} in {bundle})", file=sys.stderr)
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="pin, run under darnit-amber, judge")
    r.add_argument("entry", type=Path, nargs=1)
    r.add_argument("--work", type=Path, default=Path("runs"), help="where checkouts, bundles and verdicts go (default: runs/)")
    r.add_argument("--key", type=Path, help="signing key (PEM) for darnit-amber; without it Amber signs keyless")
    r.add_argument("--amber", default="darnit-amber", help="the darnit-amber executable")
    r.add_argument("--rerun", action="store_true", help="also rerun on this machine and judge the rerun")
    r.add_argument(
        "--no-timestamp", dest="timestamp", action="store_false", help="no timestamp authority (such a run cannot be rerun)"
    )
    j = sub.add_parser("judge", help="judge a stored run")
    j.add_argument("entry", type=Path, nargs=1)
    j.add_argument("--run-dir", type=Path, required=True, help="<bundle>/runs/<id>")
    j.add_argument("--out", type=Path, help="write the verdict here")
    c = sub.add_parser("check", help="judge the entries' own baseline metrics")
    c.add_argument("entry", type=Path, nargs="+")
    args = p.parse_args(argv)
    try:
        return {"run": cmd_run, "judge": cmd_judge, "check": cmd_check}[args.cmd](args)
    except (EntryError, subprocess.CalledProcessError) as e:
        print(f"amber-corpus: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
