# Authority & Legal Effect Protocol — v0.6

Authority tier and legal effect are separate. Every material authority should capture both.

## 1. Legal Effect Labels
Use one of:
- `BINDING_GENERAL` — binding generally within the relevant legal system.
- `BINDING_PARTIES` — binding on identified parties/case but not necessarily generally.
- `AUTHORITATIVE_INTERPRETATION` — official interpretation with material persuasive/institutional weight.
- `PERSUASIVE_OFFICIAL` — official but nonbinding material.
- `NONBINDING_DRAFT` — consultation/draft/proposal.
- `DISCOVERY_ONLY` — not suitable as substantive support.

## 2. Procedural Status Labels
- `FINAL`
- `INTERIM`
- `UNDER_APPEAL`
- `STAYED`
- `OPEN_CONSULTATION`
- `ADOPTED_NOT_EFFECTIVE`
- `IN_FORCE`
- `SUPERSEDED`
- `WITHDRAWN`
- `REPEALED`

## 3. Binding Scope
Record:
```yaml
binding_scope:
  territory:
  institutions_or_parties:
  subject_matter:
  temporal_scope:
```

## 4. Hierarchy Rule
When authorities conflict, do not resolve solely by publication date. Assess:
1. formal legal hierarchy;
2. jurisdiction/territorial competence;
3. procedural posture;
4. issue fit;
5. later-in-time effect where hierarchy permits;
6. whether the apparent conflict is factual rather than doctrinal.

## 5. EU / Multi-Level Systems
For EU privacy work distinguish, where relevant:
- EU legislation;
- CJEU judgments;
- EDPB binding decisions;
- EDPB opinions/guidelines;
- national law overlays;
- national supervisory-authority decisions;
- national court judgments.

Do not label all regulator outputs as equivalent merely because they are official.
