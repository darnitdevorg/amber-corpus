# Amber scenarios

Synthetic experiments that each force one outcome of `darnit-amber run` / `verify` /
`rerun`. The corpus entries under `entries/` are real artifacts with external ground
truth; this directory is the opposite: tiny, deterministic by construction, and built
so the expected verdict is known before the tool runs. Together they answer two
different questions. The entries ask *does Amber reach the right verdict on real
research code*; the scenarios ask *does Amber tell the cases apart at all*.

| scenario | what it shows | expected |
|---|---|---|
| s1 | deterministic experiment, claim holds | `REPRODUCED`; `verify` passes; `rerun` identical outputs, no drift |
| s2 | claim misses outside tolerance | `NOT_REPRODUCED`; the entry expects that, so `matches_expected` is true |
| s3 | claim inside tolerance | `REPRODUCED`, reason names the tolerance |
| s4 | output embeds a timestamp, claim stable | outputs *change* on rerun, claim verdict does not, `drift: false` |
| s5 | experiment exits 3 before writing metrics | bundle still written, `exit_code: 3`, claim `NOT_COMPARABLE` (output not produced), `verify` passes |
| s6 | claim points at a file never produced | `NOT_COMPARABLE` with the reason |
| s7 | stored output edited after the run | `verify` exits 2, `stored_outputs_match: false`, signatures still verify |
| s8 | verify with a key that did not sign | `verify` exits 2, `signatures_verified: false` |
| s9 | uncommitted change in the checkout | run refused; `--allow-dirty` records no commit and cannot be rerun |
| s10 | observe first, judge later: `run` with no claims, then a reviewer's `claim` signed by a second key | `NOT_COMPARABLE` with outputs inferred; the derived bundle is `REPRODUCED`; `verify` passes with both keys, fails with the researcher's alone (and says `--claimer-pubkey`), fails with the keys swapped |

s4 is the one that matters most: a reproducibility check that compares bytes calls
every timing log a failure, one that compares claims does not. Amber records both and
reports drift only when a verdict changes (or when nothing was measured and the bytes
moved).

## Run it

Needs `git`, `openssl`, `witness` on `PATH`, and `darnit-amber` from the run-bundle
branch. Nothing is published and no key outside the work directory is touched: the
runner generates its own ed25519 pair (and a stranger's, for s8).

    python3 scenarios/run_scenarios.py
    python3 scenarios/run_scenarios.py --amber ~/darnit-test/darnit/.venv/bin/darnit-amber
    python3 scenarios/run_scenarios.py --only s4,s7 --no-timestamp --keep --work /tmp/amber-scn

It writes `scenarios/RESULTS.md` (one row per scenario, every check underneath) and
exits non-zero if any scenario misses its expectation. `--no-timestamp` skips the
RFC 3161 countersignature, for a machine without network; the default exercises the
real timestamp authority.

Each scenario is a throwaway git repository holding `experiment.sh`, plus an entry
in the corpus format (`claims[].measure` and `run.command`), so what runs is exactly
what a corpus entry runs.
