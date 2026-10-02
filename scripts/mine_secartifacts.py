import csv, pathlib, re, sys
import yaml

rows, skipped = [], []
for p in sorted(pathlib.Path("_conferences").glob("*/results.md")):
    m = re.match(r"([a-z]+)(\d{4})$", p.parent.name)
    venue, year = (m.group(1), m.group(2)) if m else (p.parent.name, "")
    parts = p.read_text(encoding="utf-8").split("---", 2)
    if len(parts) < 3:
        continue
    fm_text = parts[1].replace("\t", "    ")
    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        skipped.append((str(p), str(e).split("\n")[0]))
        continue
    for a in (fm.get("artifacts") or []):
        if not isinstance(a, dict):
            continue
        b = (a.get("badges") or "").lower()
        rows.append({
            "venue": venue, "year": year,
            "title": (a.get("title") or "").strip(),
            "available": "available" in b,
            "functional": "functional" in b,
            "reproduced": "reproduced" in b,
            "artifact_url": a.get("artifact_url") or "",
            "paper_url": a.get("paper_url") or "",
            "appendix_url": a.get("appendix_url") or "",
        })

with open("/tmp/artifacts.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

print("total:", len(rows))
print("reproduced:", sum(r["reproduced"] for r in rows))
print("func-not-repro:", sum(r["available"] and r["functional"] and not r["reproduced"] for r in rows))
for s in skipped:
    print("SKIP", s)
