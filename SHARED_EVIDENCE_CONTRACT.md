# Shared Evidence Contract — v0.6

All three Data Privacy Legal Research skills must use compatible source, proposition, issue, and delta records.

## 1. Verification Status
### Source
- `VERIFIED_OFFICIAL` — official source located and checked.
- `VERIFIED_SECONDARY` — reputable secondary source checked, official source unavailable or intentionally unnecessary.
- `SECONDARY_ONLY` — located only through secondary discovery; official source expected but not verified.
- `SOURCE_GAP` — no adequate source located after targeted research.

### Proposition
- `VERIFIED` — authority directly supports the proposition.
- `PARTIALLY_VERIFIED` — support is incomplete or materially fact-dependent.
- `UNVERIFIED` — proposition lacks adequate support.
- `CONFLICTED` — material authorities point in different directions.
- `NO_AUTHORITY_LOCATED` — no authority found; not equivalent to “no authority exists.”

## 2. Authority Dimensions
Apply `shared/AUTHORITY_EFFECT_PROTOCOL.md`. Authority tier and legal effect are not interchangeable.

Record both a rough tier and the dimensions in `shared/LEGAL_EPISTEMICS.md`.

- Tier 0 — binding primary law / binding final judgment / binding final order
- Tier 1 — authoritative official interpretation
- Tier 2 — persuasive official material / draft / policy signal
- Tier 3 — reputable secondary legal research
- Tier 4 — discovery-only source

Required material fields:
```yaml
authority_tier:
legal_effect:
binding_scope:
institutional_weight:
procedural_posture:
temporal_status:
issue_fit:
```

## 3. Proposition Record
```yaml
proposition_id:
issue_id:
proposition_type: LEGAL_RULE | LEGAL_TEST | FACTUAL_PREDICATE | APPLICATION_INFERENCE | ENFORCEMENT_SIGNAL | PRACTICAL_RECOMMENDATION | HORIZON_SIGNAL
proposition:
conclusion:
jurisdiction:
actor_scope:
data_scope:
purpose_scope:
territorial_scope:
temporal_scope:
authority_ids: []
counter_authority_ids: []
pinpoints: []
material_facts: []
assumptions: []
limitations: []
support_status:
legal_confidence: high | medium | low
factual_confidence: high | medium | low
last_verified_at:
```

## 4. Relationship Vocabulary
- `interprets`
- `applies`
- `clarifies`
- `narrows`
- `expands`
- `distinguishes`
- `cites`
- `conflicts_with`
- `supersedes`
- `amends`
- `enforces`
- `proposes_change_to`
- `appeals`
- `implements`
- `factually_analogous_to`
- `summary_of`
- `translation_of`
- `depends_on`
- `exception_to`
- `overrides`

## 5. No-Silent-Supplement
If available research does not support a material proposition, disclose the gap. Model knowledge may be used only as explicitly labelled unverified background, never as substitute authority.

## 6. Negative-Evidence Rule
“No authority located” is a research result, not a legal conclusion. Never convert a search failure into “the law does not require X.”
