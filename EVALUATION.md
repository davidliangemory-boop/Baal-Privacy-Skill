# Evaluation Harness — Data Privacy Legal Research Skills v0.6

## Purpose
Test whether the skills improve legal-research quality compared with an unstructured baseline.

## Benchmark Set
Maintain a curated set of real privacy questions across jurisdictions and issue types. Each benchmark should have a manually reviewed gold record:

```yaml
benchmark_id:
question:
jurisdiction:
facts:
required_issue_tree:
required_authorities:
key_factual_pivots:
acceptable_conclusion_range:
known_traps:
known_superseded_sources:
```

## Suggested Benchmark Categories
- employee monitoring
- biometrics
- sensitive/special-category data
- cross-border transfer
- controller/processor qualification
- processor contracting
- DSAR
- retention/deletion
- children/minors
- cookies/adtech/SDK/pixels
- AI training data
- breach response
- DPO/CPO/local representative
- geolocation
- data localisation

## Metrics
Score at least:
- Authority recall
- Primary-source ratio
- Wrong-authority rate
- Unsupported-proposition rate
- Outdated-law rate
- Issue-tree completeness
- Counter-authority recall
- Fact-pivot identification
- Citation-to-proposition accuracy
- Horizon/current-law separation
- False-delta rate for monitoring
- Dependency-propagation accuracy
- Material-fact identification accuracy
- Cross-jurisdiction false-equivalence rate
- Recommendation-vs-requirement separation

## Comparison Modes
Run the same benchmark under:
1. no skill / generic research prompt
2. source mapper only
3. issue synthesizer v1
4. current full stack

Track regressions whenever a skill is modified.

## Pass Criteria
A production candidate should show clear improvement in primary-source coverage, issue-tree completeness, and unsupported-proposition rate without materially increasing false confidence or obsolete-law errors.


## Release Regression Protocol
Before promoting a new version:
1. run a fixed benchmark subset across the prior and candidate version;
2. compare primary-source recall, unsupported proposition rate, current-law accuracy, counter-authority recall, issue-tree completeness, and false-delta rate;
3. inspect every regression affecting an outcome-determinative proposition;
4. do not promote if the candidate improves verbosity/coverage but worsens legal reliability;
5. retain benchmark outputs for version-to-version comparison.

Use `benchmarks/BENCHMARK_SCHEMA.yaml`, `benchmarks/SCORING_RUBRIC.md`, and `benchmarks/SEED_SET.md`.
