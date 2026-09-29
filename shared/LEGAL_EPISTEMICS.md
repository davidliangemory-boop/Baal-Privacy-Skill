# Legal Epistemics Protocol — v0.3

This protocol governs how all privacy legal-research skills distinguish law, authority, evidence, inference, and recommendation.

## 1. Authority Is Multi-Dimensional
Do not reduce authority to a single tier. For every material source record, capture:
- `binding_scope`: who is legally bound and in what territory;
- `institutional_weight`: legislature / apex court / regulator / staff / secondary source;
- `procedural_posture`: final / interim / appealed / stayed / consultation / draft;
- `temporal_status`: in force / future effective / repealed / superseded / withdrawn;
- `issue_fit`: direct / analogous / background only.

A regulator FAQ may be highly persuasive but not binding. A lower-court judgment may be binding in a narrow procedural setting but weaker than a higher-court judgment on doctrine. The record must preserve that distinction.

## 2. Proposition Types
Every material proposition should be tagged as one of:
- `LEGAL_RULE` — what the law requires or permits;
- `LEGAL_TEST` — factors/elements used to decide a rule;
- `FACTUAL_PREDICATE` — fact required before a rule applies;
- `APPLICATION_INFERENCE` — application of rule/test to known facts;
- `ENFORCEMENT_SIGNAL` — evidence of regulator priorities or penalty posture;
- `PRACTICAL_RECOMMENDATION` — business/legal action, not itself a rule;
- `HORIZON_SIGNAL` — possible future change.

Do not phrase an enforcement signal or recommendation as if it were a binding legal rule.

## 3. Negative-Evidence Rule
Absence of a located case, FAQ, or enforcement action is not evidence that no rule or risk exists. Use:
- `NO_AUTHORITY_LOCATED` for a research result;
- never “there is no authority” unless the proposition is itself verified from an authoritative source.

## 4. Temporal Validation
Before relying on a material source, check where reasonably possible:
1. publication/adoption date;
2. effective date;
3. amendment or repeal status;
4. later guidance or judgment;
5. pending appeal/stay if outcome-determinative.

A source that is historically accurate but no longer current may be retained as a versioned historical authority but cannot support a current-law conclusion without qualification.

## 5. Citation-to-Proposition Fit
A source supports a proposition only if the cited passage supports the same proposition at the same level of generality.

Reject or downgrade support where:
- the source addresses a materially different actor, data type, purpose, or jurisdiction;
- the text is a party submission rather than the authority’s view;
- the proposition generalizes from an enforcement fact pattern without a general rule;
- the source is only a press release summarizing an underlying decision that is available.

## 6. Controlled Inference
Inference is permitted only when:
- the underlying facts are stated;
- the legal rule/test is separately sourced;
- the inference is labelled as analysis, not authority;
- material assumptions are explicit;
- plausible contrary inferences are considered when outcome-determinative.

## 7. Conclusion Strength
Use conclusion verbs proportionate to evidence:
- `REQUIRES / PROHIBITS` — only where legal authority is clear;
- `LIKELY / UNLIKELY` — strong but not conclusive authority/application;
- `ARGUABLY / RISK EXISTS` — mixed or fact-sensitive authority;
- `CANNOT VERIFY` — authority or facts are insufficient.

## 8. Research Stop Rule
Stop expanding research when all outcome-determinative propositions are `VERIFIED` or the remaining uncertainty is explicitly bounded and unlikely to change the decision. Continue when a missing or conflicted proposition could materially change the conclusion.
