#!/usr/bin/env python3
"""Run the Amber scenario matrix against an installed ``darnit-amber`` and write RESULTS.md.

Each scenario is a tiny synthetic experiment committed to a throwaway git repository,
built so that ``darnit-amber run``, ``verify`` and ``rerun`` must reach one specific
outcome. The matrix is the demonstration that the tool distinguishes the cases a
reproducibility check has to distinguish: a claim that holds, one that misses, one
inside tolerance, output that changes while the claim holds, a failed experiment, a
claim nothing measured, a tampered output, the wrong signer, an uncommitted checkout.

    python3 scenarios/run_scenarios.py                 # darnit-amber from PATH
    python3 scenarios/run_scenarios.py --amber ~/darnit-test/darnit/.venv/bin/darnit-amber
    python3 scenarios/run_scenarios.py --only s1,s7 --no-timestamp

Needs: git, openssl (ed25519 keys), witness on PATH, and darnit-amber (the Amber
run-bundle branch). Nothing is published; every bundle stays in the work directory.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent

METRIC_REGEX = '"accuracy": ([0-9.]+)'


def sh(*args: str, cwd: Path | None = None, check: bool = True, env: dict[str, str] | None = None) -> str:
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=env, timeout=600)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} -> {r.returncode}\n{r.stderr}")
    return r.stdout


@dataclass
class Check:
    name: str
    expected: str
    observed: str

    @property
    def ok(self) -> bool:
        return self.expected == self.observed


@dataclass
class Case:
    name: str
    shows: str
    experiment: str  # body of experiment.sh, run from the checkout root
    claims: list[dict[str, Any]]
    outputs: list[str]
    after: Callable[["Runner", "Case", dict[str, Any]], list[Check]]
    run_flags: list[str] = field(default_factory=list)
    expect_run_rc: int = 0

    @property
    def out_dir(self) -> str:
        return f"amber-{self.name}"


class Runner:
    def __init__(self, amber: str, work: Path, no_timestamp: bool) -> None:
        self.amber = amber
        self.work = work
        self.store = work / "store"
        self.ts = ["--no-timestamp"] if no_timestamp else []
        self.key = work / "researcher.key"
        self.pub = work / "researcher.pub"
        self.stranger_pub = work / "stranger.pub"
        self.stranger_key = work / "stranger.key"
        self.repos: dict[str, Path] = {}
        self.git_env = {
            **os.environ,
            "GIT_AUTHOR_NAME": "Amber Scenarios",
            "GIT_AUTHOR_EMAIL": "scenarios@amber.invalid",
            "GIT_COMMITTER_NAME": "Amber Scenarios",
            "GIT_COMMITTER_EMAIL": "scenarios@amber.invalid",
        }

    # -- setup -------------------------------------------------------------
    def keys(self) -> None:
        for key, pub in ((self.key, self.pub), (self.work / "stranger.key", self.stranger_pub)):
            sh("openssl", "genpkey", "-algorithm", "ed25519", "-out", str(key))
            sh("openssl", "pkey", "-in", str(key), "-pubout", "-out", str(pub))
            key.chmod(0o600)

    def artifact(self, case: Case) -> Path:
        repo = self.work / "artifacts" / case.name
        self.repos[case.name] = repo
        repo.mkdir(parents=True)
        (repo / "experiment.sh").write_text("#!/bin/sh\nset -eu\n" + case.experiment.strip() + "\n")
        (repo / "README.md").write_text(f"# {case.name}\n\nSynthetic Amber scenario: {case.shows}\n")
        sh("git", "init", "-q", "-b", "main", cwd=repo, env=self.git_env)
        sh("git", "add", "-A", cwd=repo, env=self.git_env)
        sh("git", "commit", "-q", "-m", f"scenario {case.name}", cwd=repo, env=self.git_env)
        return repo

    def entry(self, case: Case) -> Path:
        # JSON rather than YAML so the runner needs nothing outside the standard library;
        # darnit-amber reads either.
        doc = {
            "id": f"scenario-{case.name}",
            "title": case.shows,
            "role": "synthetic",
            "claims": case.claims,
            "run": {"command": "sh ./experiment.sh\n", "outputs": case.outputs},
        }
        path = self.work / "entries" / f"{case.name}.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(doc, indent=2) + "\n")
        return path

    # -- darnit-amber ------------------------------------------------------
    def amber_json(self, *args: str, rc_ok: tuple[int, ...] = (0,)) -> tuple[int, dict[str, Any], str]:
        r = subprocess.run([self.amber, *args], capture_output=True, text=True, timeout=900)
        try:
            data = json.loads(r.stdout) if r.stdout.strip() else {}
        except json.JSONDecodeError:
            data = {}
        return r.returncode, data, r.stderr

    def run(self, case: Case, repo: Path, entry: Path, *extra: str) -> tuple[int, dict[str, Any], str]:
        return self.amber_json(
            "run", str(repo), "--claims", str(entry), "--key", str(self.key), "--out", str(self.store), *self.ts, *extra
        )

    def verify(self, bundle_id: str, pub: Path | None = None, *extra: str) -> tuple[int, dict[str, Any], str]:
        return self.amber_json("verify", bundle_id, "--out", str(self.store), "--pubkey", str(pub or self.pub), *extra)

    def observe(self, repo: Path, *argv: str) -> tuple[int, dict[str, Any], str]:
        """``run`` with no entry: the command's argv after ``--`` (one element each, as a shell would split
        it; a single string would be quoted into one program name), outputs inferred, nothing judged."""
        return self.amber_json("run", str(repo), "--key", str(self.key), "--out", str(self.store), *self.ts, "--", *argv)

    def claim(self, bundle_id: str, key: Path, *spec: str) -> tuple[int, dict[str, Any], str]:
        return self.amber_json("claim", bundle_id, "--out", str(self.store), "--key", str(key), *self.ts, *spec)

    def rerun(self, bundle_id: str, artifact: Path | None = None) -> tuple[int, dict[str, Any], str]:
        # A bundle made from a local path records no path (its subject is local/<name>), so rerun is told
        # where the clone is; a bundle made from a URL needs nothing.
        where = ["--artifact", str(artifact)] if artifact else []
        return self.amber_json(
            "rerun", bundle_id, "--out", str(self.store), "--pubkey", str(self.pub), "--key", str(self.key), "--yes",
            *where, *self.ts
        )

    def stored_output(self, bundle_id: str, rel: str) -> Path:
        return self.store / bundle_id / "outputs" / rel

    def bundle(self, bundle_id: str) -> dict[str, Any]:
        return json.loads((self.store / f"{bundle_id}.intoto.json").read_text())


# -- shared assertions ----------------------------------------------------------
def claim(summary: dict[str, Any], i: int = 0) -> dict[str, Any]:
    return (summary.get("claims") or [{}])[i] if summary.get("claims") else {}


def verify_ok(r: Runner, bundle_id: str) -> list[Check]:
    rc, rep, _ = r.verify(bundle_id)
    return [
        Check("verify exit", "0", str(rc)),
        Check("verify.verified", "True", str(rep.get("verified"))),
        Check("verify.stored_outputs_match", "True", str(rep.get("stored_outputs_match"))),
        Check("verify.signatures_verified", "True", str(rep.get("signatures_verified"))),
    ]


def rerun_outputs(rep: dict[str, Any]) -> str:
    results = sorted({o["result"] for o in rep.get("outputs") or []})
    return ",".join(results) or "none"


# -- scenario post-conditions --------------------------------------------------
def after_s1(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    checks = [
        Check("verdict", "REPRODUCED", str(s.get("verdict"))),
        Check("claim.measured", "0.95", str(claim(s).get("measured"))),
        Check("subject records no path", "local/s1", str((s.get("subject") or {}).get("name"))),
        *verify_ok(r, s["id"]),
    ]
    rc, rep, _ = r.rerun(s["id"], r.repos[c.name])
    checks += [
        Check("rerun exit", "0", str(rc)),
        Check("rerun.drift", "False", str(rep.get("drift"))),
        Check("rerun.outputs", "identical", rerun_outputs(rep)),
        Check("rerun.verdict", "REPRODUCED", str(rep.get("verdict"))),
    ]
    return checks


def after_s2(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    return [
        Check("verdict", "NOT_REPRODUCED", str(s.get("verdict"))),
        Check("claim.measured", "0.93", str(claim(s).get("measured"))),
        Check("claim.matches_expected", "True", str(claim(s).get("matches_expected"))),
        *verify_ok(r, s["id"])[:2],
    ]


def after_s3(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    return [
        Check("verdict", "REPRODUCED", str(s.get("verdict"))),
        Check("claim.measured", "0.949", str(claim(s).get("measured"))),
        Check("claim.reason mentions tolerance", "True", str("tolerance" in str(claim(s).get("reason")))),
    ]


def after_s4(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    checks = [Check("verdict", "REPRODUCED", str(s.get("verdict")))]
    rc, rep, _ = r.rerun(s["id"], r.repos[c.name])
    changed = any(o["result"] == "changed" for o in rep.get("outputs") or [])
    same = all(x["result"] == "same" for x in rep.get("claims") or [])
    checks += [
        Check("rerun exit", "0", str(rc)),
        Check("rerun: some output changed", "True", str(changed)),
        Check("rerun: every claim verdict same", "True", str(same)),
        Check("rerun.drift", "False", str(rep.get("drift"))),
    ]
    return checks


def after_s5(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    return [
        Check("experiment.exit_code", "3", str((s.get("experiment") or {}).get("exit_code"))),
        Check("verdict", "NOT_COMPARABLE", str(s.get("verdict"))),
        Check("claim.reason: not produced", "True", str("not produced" in str(claim(s).get("reason")))),
        *verify_ok(r, s["id"])[:2],
    ]


def after_s6(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    return [
        Check("verdict", "NOT_COMPARABLE", str(s.get("verdict"))),
        Check("claim.measured", "None", str(claim(s).get("measured"))),
        Check("claim.reason: not produced", "True", str("not produced" in str(claim(s).get("reason")))),
    ]


def after_s7(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    before = verify_ok(r, s["id"])[:2]
    target = r.stored_output(s["id"], f"{c.out_dir}/metrics.json")
    target.write_text('{"accuracy": 0.99}\n')  # the attacker's number, after the fact
    rc, rep, _ = r.verify(s["id"])
    return [
        *before,
        Check("after tamper: verify exit", "2", str(rc)),
        Check("after tamper: verify.verified", "False", str(rep.get("verified"))),
        Check("after tamper: stored_outputs_match", "False", str(rep.get("stored_outputs_match"))),
        Check("after tamper: signatures still verify", "True", str(rep.get("signatures_verified"))),
    ]


def after_s8(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    rc, rep, _ = r.verify(s["id"], r.stranger_pub)
    return [
        Check("right key: verify.verified", "True", str(r.verify(s["id"])[1].get("verified"))),
        Check("stranger key: verify exit", "2", str(rc)),
        Check("stranger key: verify.verified", "False", str(rep.get("verified"))),
        Check("stranger key: signatures_verified", "False", str(rep.get("signatures_verified"))),
    ]


def after_s9(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    # ``s`` is the summary of the --allow-dirty run; the refused run is checked in run_case.
    digest = (s.get("subject") or {}).get("digest") or {}
    rc, _, err = r.rerun(s["id"], r.repos[c.name])
    return [
        Check("allow-dirty: bundle written", "True", str(bool(s.get("id")))),
        Check("allow-dirty: no commit recorded", "True", str("gitCommit" not in digest)),
        Check("allow-dirty: rerun refused", "True", str(rc != 0)),
    ]


def after_s10(r: Runner, c: Case, s: dict[str, Any]) -> list[Check]:
    """``s`` is the observe-mode run (no claims). A reviewer, holding a different key, attaches the claim later."""
    checks = [
        Check("observe: exit_code", "0", str((s.get("experiment") or {}).get("exit_code"))),
        Check("observe: verdict", "NOT_COMPARABLE", str(s.get("verdict"))),
        Check("observe: no claims", "0", str(len(s.get("claims") or []))),
        Check("observe: outputs inferred", "True", str(any("metrics.json" in o["path"] for o in s["experiment"]["outputs"]))),
    ]
    rc, d, err = r.claim(
        s["id"], r.stranger_key, "--id", "accuracy", "--file", f"{c.out_dir}/metrics.json",
        "--regex", METRIC_REGEX, "--threshold", "== 0.95", "--source", "reviewer, after the run",
    )
    checks.append(Check("claim exit", "0", str(rc)))
    if rc != 0 or not d.get("id"):
        checks.append(Check("claim produced a bundle", "True", f"False ({err.strip().splitlines()[-1] if err.strip() else ''})"))
        return checks
    checks += [
        Check("claim.verdict", "REPRODUCED", str(d.get("verdict"))),
        Check("claim.derived_from", s["id"][:12], str(d.get("derived_from"))[:12]),
    ]
    both = r.verify(d["id"], r.pub, "--claimer-pubkey", str(r.stranger_pub))
    one = r.verify(d["id"], r.pub)
    swapped = r.verify(d["id"], r.stranger_pub, "--claimer-pubkey", str(r.pub))
    checks += [
        Check("both keys: verified", "True", str(both[1].get("verified"))),
        Check("researcher key only: verified", "False", str(one[1].get("verified"))),
        Check("researcher key only: hint names --claimer-pubkey", "True",
              str("--claimer-pubkey" in str(one[1].get("signatures", {}).get("statement", {}).get("signature")))),
        Check("keys swapped: verified", "False", str(swapped[1].get("verified"))),
        # verify reports checks, not claims; the signer mark is in the stored derived bundle itself.
        Check("claim signed_by", "claim_signer",
              str(next((x.get("signed_by") for x in r.bundle(d["id"])["statement"]["predicate"].get("claims", [])
                        if x.get("id") == "accuracy"), None))),
    ]
    return checks


# -- the matrix ---------------------------------------------------------------
def _claim(threshold: str, tolerance: float = 0, expected: str = "REPRODUCED", file: str = "metrics.json") -> dict[str, Any]:
    return {
        "metric": "accuracy",
        "threshold": threshold,
        "tolerance": tolerance,
        "source": "synthetic scenario",
        "expected_verdict": expected,
        "measure": {"file": file, "regex": METRIC_REGEX},
    }


def _write(out: str, body: str) -> str:
    return f"mkdir -p {out}\n{body}"


CASES: list[Case] = [
    Case(
        "s1",
        "deterministic experiment, claim holds: REPRODUCED, verifies, rerun identical",
        _write("amber-s1", 'echo "accuracy 0.95" > amber-s1/run.log\nprintf \'{"accuracy": 0.95}\\n\' > amber-s1/metrics.json'),
        [_claim("== 0.95")],
        ["amber-s1/run.log", "amber-s1/metrics.json"],
        after_s1,
    ),
    Case(
        "s2",
        "claim misses outside tolerance: NOT_REPRODUCED (a negative-role entry expects exactly that)",
        _write("amber-s2", 'printf \'{"accuracy": 0.93}\\n\' > amber-s2/metrics.json'),
        [_claim("== 0.95", 0.01, expected="NOT_REPRODUCED")],
        ["amber-s2/metrics.json"],
        after_s2,
    ),
    Case(
        "s3",
        "claim inside tolerance: REPRODUCED",
        _write("amber-s3", 'printf \'{"accuracy": 0.949}\\n\' > amber-s3/metrics.json'),
        [_claim("== 0.95", 0.01)],
        ["amber-s3/metrics.json"],
        after_s3,
    ),
    Case(
        "s4",
        "non-deterministic output, stable claim: outputs change on rerun, verdict does not, no drift",
        _write(
            "amber-s4",
            'date +%s%N > amber-s4/run.log\nprintf \'{"accuracy": 0.95, "run_at": %s}\\n\' "$(date +%s%N)" > amber-s4/metrics.json',
        ),
        [_claim("== 0.95")],
        ["amber-s4/run.log", "amber-s4/metrics.json"],
        after_s4,
    ),
    Case(
        "s5",
        "experiment fails (exit 3) before writing metrics: bundle still written, exit recorded, nothing judged",
        _write("amber-s5", 'echo "crashed" > amber-s5/run.log\nexit 3'),
        [_claim("== 0.95")],
        ["amber-s5/run.log", "amber-s5/metrics.json"],
        after_s5,
    ),
    Case(
        "s6",
        "claim points at a file the experiment never produced: NOT_COMPARABLE with the reason",
        _write("amber-s6", 'printf \'{"accuracy": 0.95}\\n\' > amber-s6/other.json'),
        [_claim("== 0.95", file="amber-s6/metrics.json")],
        ["amber-s6/other.json"],
        after_s6,
    ),
    Case(
        "s7",
        "stored output edited after the run: verify fails on stored_outputs_match, signatures intact",
        _write("amber-s7", 'printf \'{"accuracy": 0.95}\\n\' > amber-s7/metrics.json'),
        [_claim("== 0.95")],
        ["amber-s7/metrics.json"],
        after_s7,
    ),
    Case(
        "s8",
        "verify with a key that did not sign: signatures_verified false",
        _write("amber-s8", 'printf \'{"accuracy": 0.95}\\n\' > amber-s8/metrics.json'),
        [_claim("== 0.95")],
        ["amber-s8/metrics.json"],
        after_s8,
    ),
    Case(
        "s10",
        "observe first, judge later: a run with no claims, a reviewer's claim signed by a second key, both signers verified",
        _write("amber-s10", 'printf \'{"accuracy": 0.95}\\n\' > amber-s10/metrics.json'),
        [],
        [],
        after_s10,
    ),
    Case(
        "s9",
        "uncommitted change in the checkout: run refused; --allow-dirty records no commit and cannot be rerun",
        _write("amber-s9", 'printf \'{"accuracy": 0.95}\\n\' > amber-s9/metrics.json'),
        [_claim("== 0.95")],
        ["amber-s9/metrics.json"],
        after_s9,
    ),
]

for _c in CASES:  # every claim's measure.file lives under the scenario's output dir
    for _cl in _c.claims:
        f = _cl["measure"]["file"]
        if "/" not in f:
            _cl["measure"]["file"] = f"{_c.out_dir}/{f}"


# -- driver -------------------------------------------------------------------
def run_case(r: Runner, c: Case) -> tuple[list[Check], str | None]:
    repo = r.artifact(c)
    entry = r.entry(c)
    checks: list[Check] = []
    if c.name == "s10":
        rc, s, err = r.observe(repo, "sh", "./experiment.sh")
    elif c.name == "s9":
        (repo / "README.md").write_text("edited, not committed\n")
        rc, _, err = r.run(c, repo, entry)
        checks += [
            Check("dirty: run exit", "1", str(rc)),
            Check("dirty: refusal names --allow-dirty", "True", str("--allow-dirty" in err)),
        ]
        rc, s, err = r.run(c, repo, entry, "--allow-dirty")
    else:
        rc, s, err = r.run(c, repo, entry)
    checks.append(Check("run exit", str(c.expect_run_rc), str(rc)))
    if rc != c.expect_run_rc or not s.get("id"):
        checks.append(Check("run produced a bundle", "True", f"False ({err.strip().splitlines()[-1] if err.strip() else 'no output'})"))
        return checks, None
    try:
        checks += c.after(r, c, s)
    except Exception as e:  # noqa: BLE001 - a scenario that blows up is a failed row, not a crashed matrix
        checks.append(Check("post-conditions ran", "True", f"False ({type(e).__name__}: {e})"))
    return checks, s["id"]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--amber", default="darnit-amber", help="darnit-amber executable (default: from PATH)")
    p.add_argument("--work", type=Path, help="work directory (default: a fresh temp dir)")
    p.add_argument("--keep", action="store_true", help="keep the work directory")
    p.add_argument("--only", help="comma-separated scenario names, e.g. s1,s7")
    p.add_argument("--no-timestamp", action="store_true", help="pass --no-timestamp to darnit-amber (offline TSA)")
    p.add_argument("--results", type=Path, default=HERE / "RESULTS.md")
    a = p.parse_args()

    for tool in ("git", "openssl", "witness"):
        if shutil.which(tool) is None:
            print(f"missing: {tool}", file=sys.stderr)
            return 2
    if shutil.which(a.amber) is None and not Path(a.amber).is_file():
        print(f"missing: {a.amber}", file=sys.stderr)
        return 2

    work = a.work or Path(tempfile.mkdtemp(prefix="amber-scenarios-"))
    work.mkdir(parents=True, exist_ok=True)
    r = Runner(str(Path(a.amber).resolve()) if Path(a.amber).is_file() else a.amber, work, a.no_timestamp)
    r.keys()

    wanted = set(a.only.split(",")) if a.only else {c.name for c in CASES}
    rows: list[tuple[Case, list[Check], str | None]] = []
    for c in CASES:
        if c.name not in wanted:
            continue
        print(f"{c.name}: {c.shows}", file=sys.stderr)
        checks, bundle_id = run_case(r, c)
        rows.append((c, checks, bundle_id))
        for ck in checks:
            print(f"   {'ok  ' if ck.ok else 'FAIL'} {ck.name}: expected {ck.expected}, got {ck.observed}", file=sys.stderr)

    witness = subprocess.run(["witness", "version"], capture_output=True, text=True).stdout.strip().splitlines()
    lines = [
        "# Amber scenario results",
        "",
        f"Generated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by `scenarios/run_scenarios.py`"
        f" on {platform.system()} {platform.release()} ({platform.machine()}), {witness[0] if witness else 'witness ?'},"
        f" timestamps {'off' if a.no_timestamp else 'on'}.",
        "",
        "| scenario | shows | checks | result | bundle |",
        "|---|---|---|---|---|",
    ]
    failed = 0
    for c, checks, bundle_id in rows:
        bad = [ck for ck in checks if not ck.ok]
        failed += bool(bad)
        result = "pass" if not bad else "**FAIL**: " + "; ".join(f"{ck.name} expected {ck.expected}, got {ck.observed}" for ck in bad)
        lines.append(f"| {c.name} | {c.shows} | {len(checks)} | {result} | `{(bundle_id or '')[:12]}` |")
    lines += ["", "## Every check", ""]
    for c, checks, _ in rows:
        lines.append(f"### {c.name}")
        lines.append("")
        lines.append("| check | expected | observed | |")
        lines.append("|---|---|---|---|")
        for ck in checks:
            lines.append(f"| {ck.name} | `{ck.expected}` | `{ck.observed}` | {'ok' if ck.ok else 'FAIL'} |")
        lines.append("")
    a.results.write_text("\n".join(lines) + "\n")
    print(f"\n{len(rows) - failed}/{len(rows)} scenarios pass; results in {a.results}; bundles in {r.store}", file=sys.stderr)

    if not a.keep and a.work is None and failed == 0:
        shutil.rmtree(work, ignore_errors=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
