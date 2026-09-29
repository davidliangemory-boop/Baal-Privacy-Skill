# Benchmark Scoring Rubric — v0.5

Score each dimension 0–4 unless stated otherwise.

## A. Issue Architecture
- issue-tree completeness
- identification of dispositive vs peripheral branches
- key factual pivots
- jurisdiction-specific overlays

## B. Authority Quality
- primary-source recall
- authority hierarchy correctness
- temporal/current-law accuracy
- counter-authority recall
- citation-to-proposition fit

## C. Epistemic Discipline
- unsupported-proposition rate (reverse score)
- no-silent-supplement compliance
- negative-evidence discipline
- law/inference/recommendation separation
- conclusion proportionality

## D. Operational Usefulness
- decision relevance
- required vs recommended control separation
- clear evidence gaps
- escalation/re-analysis trigger quality

## E. Monitoring Quality
For delta tests:
- true-delta recall
- false-delta suppression
- affected-proposition mapping
- change-propagation accuracy
- horizon/current-law separation

## Production Gate
A release should not be promoted if it materially increases:
- wrong-authority rate;
- outdated-law rate;
- unsupported material propositions;
- false-delta rate;
- false-equivalence across jurisdictions.
