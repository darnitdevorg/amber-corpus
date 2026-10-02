# Amber corpus

A set of real, publicly downloadable research artifacts (secartifacts.github.io) with known expected
outcomes for testing whether Amber reaches the right verdict. To judge that you need artifacts where someone independent has already established the answer. Every entry here comes from a conference artifact-evaluation committee. The Results Reproduced badge means an evaluator, not the authors, obtained the paper's main results from the submitted artifact. That badge is the ground truth.

Three roles and a corpus needs all three:

| role | meaning | a tool that gets this wrong is... |
|---|---|---|
| `positive` | claims reproduce | under-reporting |
| `negative` | claims do not reproduce | over-reporting - the dangerous one |
| `not_comparable` | measurable, but not on the paper's terms | mislabelling method as failure |

The third exists because of a real case. Re-running the gittuf NDSS'25 benchmark
by measuring whole-RSL verification per call, then dividing by push count, gives
an upper bound on the paper's *incremental* per-push figure. Measured that way it
reads 0.97 s against a 0.59 s threshold and looks like a failed claim. It isn't:
it's a different quantity. A tool that reports NOT_REPRODUCED there is wrong.

    corpus.csv            index of candidates, machine-generated
    entries/*.yaml        one per artifact; TEMPLATE.yaml documents the fields
    docs/                 appendix excerpts used for screening
    scripts/              the miner that built corpus.csv

Candidates are mined from https://github.com/secartifacts/secartifacts.github.io
(NDSS, USENIX Security, S&P, PETS, ACSAC, CHES, VehicleSec, WOOT) and filtered to
artifacts that are runnable on an ordinary machine: CPU only, no cluster, bounded
runtime and disk, no credentials or gated datasets.

Copy `entries/TEMPLATE.yaml`, fill it in and open a PR. Quote the appendix for
resource claims and the paper for metric thresholds - including how the paper
measured them.

-> No expected output hash

The obvious design would be record a digest of the expected output, compare. The Results Reproduced badge certifies that an evaluator obtained results *supporting the paper's claims*, within tolerance - USENIX states the goal is
"not to reproduce the results exactly but instead to generate results independently within an allowed tolerance." No digest is recorded, because most artifacts are not bit-reproducible: timings depend on hardware, ML runs on seeds
and backends, fuzzing on chance.

So each entry's external ground truth is a threshold on a metric, not a digest, and the fields are `threshold`, `measurement_protocol` and `expected_verdict`.

