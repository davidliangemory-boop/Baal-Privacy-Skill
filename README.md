# Data Privacy Legal Research Skills — v0.6

**Pre-production research architecture.** v0.6 is the third optimisation round after v0.3–v0.5.

## Architecture
**Source Mapping → Issue Synthesis → Legal Delta Management → Change Propagation → Regression Testing**

## Four-step legal research model
1. **Source Base** — establish the authoritative and maintainable source universe.
2. **Framework** — form the issue tree / legal test quickly.
3. **Issue Resolution** — resolve uncertain propositions through targeted official authority and strong factual analogies.
4. **Horizon** — monitor credible future legal/regulatory movement.

## v0.6 red-team refinements
- separated `research_role` from document taxonomy; the four steps are research functions, not mutually exclusive source types;
- separated authority tier from actual `legal_effect`;
- added procedural-status and binding-scope protocol;
- added analogical-fit controls to prevent overgeneralising from single enforcement cases;
- added horizon signal scoring and regulatory-event lifecycle deduplication;
- hardened EU/multi-level authority treatment;
- added package validation script and acceptance checks.

## Core skills
- `privacy_source_mapper`
- `privacy_issue_synthesizer`
- `privacy_regulatory_delta_monitor`

## Shared protocols
- `SHARED_EVIDENCE_CONTRACT.md`
- `shared/LEGAL_EPISTEMICS.md`
- `shared/AUTHORITY_EFFECT_PROTOCOL.md`
- `shared/ANALOGICAL_FIT_PROTOCOL.md`
- `shared/HORIZON_SIGNAL_PROTOCOL.md`
- `shared/KNOWLEDGE_GRAPH_CONTRACT.md`
- `shared/MULTI_JURISDICTION_PROTOCOL.md`
- `shared/OPERATING_MODES.md`
- `shared/TOOL_ROUTING_PROTOCOL.md`
