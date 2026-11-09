# The oracle test: one machine runs, another verifies and re-runs

The claim Amber makes is not "this ran"; it is "someone else can check that it ran
and run it again". The scenarios (`scenarios/`) show the tool tells cases apart on one
machine. This procedure shows the hand-off: a bundle produced on machine A, verified
and re-executed on machine B by a person who only has the bundle, the producer's
public key and these instructions.

The entry is `entries/usenixsec2024-oideli.yaml` (ProVerif proofs, about a second of
compute; the setup is what takes time). The artifact is a public git URL at a pinned
commit, so machine B clones it fresh — nothing from A's checkout is reused.

## 0. Setup, on every machine (A and B)

Everything lands under one directory, `~/amber-oracle`; no root, nothing outside it.
About 15 minutes, most of it compiling OCaml. Needs only git, gcc, make, curl, tar,
python3 and openssl on the machine.

    curl -fsSLO https://raw.githubusercontent.com/darnitdevorg/amber-corpus/main/scripts/oracle-setup.sh
    bash oracle-setup.sh
    source ~/amber-oracle/env.sh

(Until the script is on `main`, copy `scripts/oracle-setup.sh` over by hand.) It installs
uv, Witness, OCaml 4.14.2 (built from the tagged source), ProVerif 2.05 (tarball SHA-256 checked against the
entry), darnit-amber from PR #678 at a pinned commit, and makes an ed25519 key pair in
`~/amber-oracle/keys/`. `rm -rf ~/amber-oracle` removes all of it.

## 1. Machine A: run, and hand over

    source ~/amber-oracle/env.sh
    git clone https://github.com/darnitdevorg/amber-corpus.git ~/amber-oracle/corpus   # or your checkout
    cd ~/amber-oracle
    darnit-amber run https://gitlab.inria.fr/oideli/oideli-artifact.git \
        --ref 8c71077e40a100344ed817cbb06f4c16881a0c06 \
        --claims corpus/entries/usenixsec2024-oideli.yaml \
        --key keys/oracle.key --out store | tee run-A.json

Expected in `run-A.json`: `"verdict": "REPRODUCED"`, two claims each `"measured": "1"`,
`"exit_code": 0`, four outputs. Note the `id`. Then:

    tar czf oideli-handoff.tgz store keys/oracle.pub run-A.json

Give `oideli-handoff.tgz` to machine B by any route (scp, a shared drive). The tarball
holds signed statements, the four captured outputs and a public key; nothing secret.

## 2. Machine B: verify, then re-run

    source ~/amber-oracle/env.sh
    mkdir -p ~/amber-oracle/from-A && cd ~/amber-oracle/from-A
    tar xzf ../oideli-handoff.tgz
    ID=$(python3 -c 'import json;print(json.load(open("run-A.json"))["id"])')

Verify — signatures against A's public key, every stored output against the digest in
the signed statement, a trusted timestamp on every signature:

    darnit-amber verify "$ID" --out store --pubkey keys/oracle.pub | tee verify-B.json

Expected: `"verified": true`, exit 0. Then re-run: Amber verifies again, asks for
consent (the command it is about to execute is printed), clones the artifact at the
recorded commit, runs it under Witness, measures the same claims, and compares:

    darnit-amber rerun "$ID" --out store --pubkey keys/oracle.pub --key ~/amber-oracle/keys/oracle.key | tee rerun-B.json

Expected: `"drift": false`, `"verdict": "REPRODUCED"`, every claim `"result": "same"`,
exit 0. The `outputs` list shows which files were byte-identical across machines and
which were not (`proverif-version.txt` and `metrics.json` should be identical; the
two `.stdout.log` files may differ — ProVerif prints timings — and that is exactly
the case Amber is built to tell apart from a failed claim).

The re-run is itself a new signed bundle in `store/`, signed with B's key. Send
`rerun-B.json` (and, if you like, the new bundle) back to A.

## 3. Two things that are allowed to differ

- **Audit statuses.** `run` also audits the artifact checkout with darnit's Amber
  controls; a machine without `gh` or without network to GitHub will show some
  controls as ERROR. That is recorded, and it is not part of the verdict.
- **Output bytes.** See above. Only a verdict change (or, for an entry with no
  measured claims, a byte change) counts as drift.

## 4. Record

| machine | role | OS / CPU | run id (12) | verdict | verify | rerun drift | notes |
|---|---|---|---|---|---|---|---|
| darnit VM (NYU) | A | RHEL 10.2, x86_64 | `3bef6135c89e` | REPRODUCED | – | – | 2026-11-09; all four output digests equal the entry's `baseline` block (captured 2026-10-26, Ubuntu 24.04) |
| sbomit (NYU) | B | RHEL 10.2, x86_64 | `2a834edf2dcc` | REPRODUCED | verified | none; 4/4 outputs identical, 2/2 claims same | 2026-11-09; found the consent-prompt-on-stdout bug, fixed in #678 `fbdf9a2` |
| | B | | | | | | |

If anything in this page did not work exactly as written, that is a finding too —
open an issue on the corpus repo with the step and the output.
