# Knowledge Graph Contract — v0.4

The system should preserve reusable legal knowledge as linked issue, proposition, fact, source, and delta nodes rather than as isolated summaries.

## 1. Core Node Types
- `SOURCE`
- `ISSUE`
- `PROPOSITION`
- `FACT`
- `CONTROL`
- `DELTA`
- `HORIZON_SIGNAL`

## 2. Issue Record
```yaml
issue_id:
title:
jurisdiction:
topic:
subtopic:
business_question:
decision_required:
status: DRAFT | RESEARCHING | VERIFIED | QUALIFIED | CONFLICTED | STALE | REOPENED | ARCHIVED
current_conclusion:
legal_confidence:
factual_confidence:
forward_confidence:
material_fact_ids: []
proposition_ids: []
source_ids: []
control_ids: []
horizon_ids: []
last_full_review_at:
next_review_trigger:
```

## 3. Proposition Dependency Graph
A proposition may depend on other propositions and facts.

Examples:
```text
P-3 "explicit consent is required"
  depends_on -> P-1 "data is sensitive"
  depends_on -> P-2 "no statutory employment exception applies"
  depends_on -> F-4 "processing purpose is attendance authentication"
```

Required relationship types:
- `depends_on`
- `conditioned_on`
- `exception_to`
- `overrides`
- `supports`
- `contradicts`
- `applied_to_fact`
- `implemented_by_control`
- `changed_by_delta`

## 4. Fact Record
```yaml
fact_id:
issue_id:
fact:
source: user | document | system | inference
verification_status: CONFIRMED | ASSUMED | DISPUTED | UNKNOWN
materiality: dispositive | high | medium | low
changes_if:
last_verified_at:
```

A legal conclusion that depends on an `ASSUMED` or `UNKNOWN` dispositive fact cannot be marked fully verified.

## 5. Legal-to-Operational Control Link
Where the research supports a business action, link the proposition to a control rather than embedding the recommendation only in prose.

```yaml
control_id:
issue_id:
control:
control_type: notice | consent | contract | governance | technical | access | retention | assessment | filing | training | monitoring
required_or_recommended: REQUIRED | RECOMMENDED | OPTIONAL
proposition_ids: []
owner:
trigger:
status:
```

## 6. Issue Lifecycle
- `DRAFT` — issue created, not researched.
- `RESEARCHING` — source/framework work underway.
- `VERIFIED` — outcome-determinative propositions supported and material facts confirmed.
- `QUALIFIED` — conclusion usable but depends on stated assumptions or limited authority.
- `CONFLICTED` — unresolved material authority conflict.
- `STALE` — relevant authority/source has changed or review age threshold exceeded.
- `REOPENED` — delta or factual change requires renewed analysis.
- `ARCHIVED` — no longer operationally relevant; history retained.

## 7. Change Propagation
When a delta affects a source or proposition:
1. identify changed source node;
2. identify linked proposition(s);
3. identify dependent propositions;
4. identify affected issue(s);
5. identify operational controls that relied on those propositions;
6. mark affected nodes `STALE` or `REOPENED` according to materiality;
7. refresh only the affected branches unless the change undermines the root framework.

## 8. Cross-Jurisdiction Normalisation
For multi-jurisdiction work, maintain a common issue ontology while preserving local doctrine.

Example common nodes:
- lawful basis
- sensitive/special-category data
- notice/transparency
- cross-border transfer
- localisation
- data subject rights
- security
- retention
- DPO/local representative

Do not force local rules into GDPR terminology when the local law uses a materially different legal structure. Use `local_equivalent_of` only for functional comparison, not doctrinal identity.

## 9. Conflict Preservation
Do not auto-harmonise conflicting authorities. Preserve:
- source A proposition;
- source B proposition;
- hierarchy/territorial differences;
- reason for conflict;
- practical consequence;
- whether the conflict is unresolved or only apparent.
