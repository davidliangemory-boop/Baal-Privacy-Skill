# privacy_source_mapper — v0.6

## Purpose
Build and maintain a classified, authoritative, continuously updateable source universe for public data privacy / data protection legal research. This skill answers: **what sources exist, how authoritative are they, what role should they play, and how should they be acquired and maintained over time?**

## Scope
Use for source discovery, source classification, source inventory design, corpus expansion, acquisition planning, and source quality control. Do **not** use this skill to form a final legal conclusion on a concrete issue.

## Operating Principles
0. **Apply shared contracts.** Use `../shared/LEGAL_EPISTEMICS.md`, `../shared/AUTHORITY_EFFECT_PROTOCOL.md`, `../shared/KNOWLEDGE_GRAPH_CONTRACT.md`, `../shared/TOOL_ROUTING_PROTOCOL.md`, and `../SHARED_EVIDENCE_CONTRACT.md`. Select an operating mode from `../shared/OPERATING_MODES.md` where the mapper is invoked for a live research task.
1. **Official first.** Prefer legislation, courts, regulators, and official repositories over aggregators and commentary.
2. **Framework before volume.** A smaller set of high-value framework materials may be more useful than a large enforcement dump.
3. **No silent supplement.** If authoritative materials cannot be found, return a `SOURCE_GAP`; do not silently fill the gap from model memory.
4. **Discovery is not authority.** Secondary indexes may be used to find materials, but conclusions should trace back to the official source whenever reasonably available.
5. **Version-aware by design.** Treat updated guidance, amended regulations, corrected decisions, appeals, and superseding documents as linked versions rather than unrelated records.

## Four-Step Research Role Model
The four steps are **research functions**, not mutually exclusive document categories. A single document may serve multiple roles. Record `research_roles: []` rather than forcing one `source_layer`.

Assign one or more roles:

1. **Source Base** — statutes, regulations, regulator databases, court databases, enforcement repositories.
2. **Framework** — guidelines, opinions, detailed guidance, topic handbooks, practice-oriented analytical materials.
3. **Issue Resolution** — FAQs, Q&A, staff letters, regulatory opinions, enforcement decisions, judgments, AG opinions.
4. **Horizon** — consultations, draft guidance, proposed rules, legislative proposals, work programmes, regulator speeches/policy statements, pending appeals.

## Authority Hierarchy
Use the following hierarchy unless the jurisdiction requires a different ordering:

- **Tier 0 — Binding primary law:** constitution/statute/regulation, binding court judgment, binding regulator order where legally binding.
- **Tier 1 — Authoritative official interpretation:** regulator guidance, binding opinion, official FAQ/Q&A, agency staff interpretation with identified status.
- **Tier 2 — Persuasive official material:** consultation paper, draft guidance, policy statement, regulator speech, enforcement press release.
- **Tier 3 — Secondary legal research:** recognised legal databases, professional associations, reputable law-firm analysis.
- **Tier 4 — Discovery only:** aggregators, trackers, news, blogs, forums.

Never use Tier 4 as the sole support for a legal proposition when higher-tier sources should exist.

## Operating Mode
For a corpus-build task, default to `STANDARD_ANALYSIS`. For a one-off source check, use `RAPID_SCREEN`. For high-stakes source validation supporting formal advice, use `FORMAL_OPINION_SUPPORT`.

## Inputs
- Jurisdiction(s)
- Topic / subtopic
- Time window
- Optional source type
- Optional requirement for official-only / primary sources
- Optional crawl requirement: one-off, periodic, daily, event-driven

## Source Discovery & Routing Protocol
Follow `shared/TOOL_ROUTING_PROTOCOL.md`. Distinguish **source absence** from **acquisition/tool failure**.

For each jurisdiction/topic:

1. Identify the **official legal publisher**, **privacy regulator**, **relevant courts**, and **official enforcement repository**.
2. Search known official repositories first.
3. If discovery requires a secondary index, use it only to identify the official document or docket.
4. Attempt at least three materially different search formulations before declaring a gap when the proposition should normally have an official source.
5. If the official source cannot be located, label the result `SECONDARY_ONLY` or `SOURCE_GAP` rather than upgrading a secondary source by implication.
6. Record whether a source is suitable for:
   - framework building;
   - proposition-level authority;
   - enforcement calibration;
   - horizon monitoring;
   - discovery only.

## Acquisition / Crawlability Protocol
Assess acquisition method in this order:

1. Official API / feed / RSS / structured endpoint
2. Official sitemap or stable index page
3. Stable HTML document page
4. Stable PDF repository
5. Search-driven dynamic site
6. Secondary discovery source only

For continuously crawled sources, capture:
- canonical URL
- document identifier / docket / decision number
- listing-page URL
- publication date
- effective date
- updated date
- last-seen timestamp
- retrieval timestamp
- content hash or equivalent version fingerprint where possible
- prior-version pointer
- superseded-by pointer

## Source Canonicalisation Rules
Do not treat the following as separate authorities unless substantively different:
- press release vs underlying final decision;
- HTML summary vs attached official PDF;
- translated copy vs official-language original;
- consultation page vs final adopted guidance;
- appeal judgment vs first-instance judgment.

Instead, link them using relationships such as:
`summary_of`, `official_text_of`, `translation_of`, `supersedes`, `appeals`, `implements`.

## Required Metadata
Capture where available:
- jurisdiction
- authority
- authority_level
- binding_status
- document_type
- research_roles
- topic
- subtopic
- title
- document_id / docket / decision_number
- date_published
- date_effective
- date_updated
- status
- official_source
- source_url
- pdf_url
- listing_url
- legal_basis
- articles
- entities
- industry
- language
- crawlability
- acquisition_method
- update_frequency
- version_id
- content_hash / version_fingerprint
- last_seen_at
- retrieved_at
- supersedes
- superseded_by
- discovery_source

## Controlled Document Types
Use controlled labels where possible:
- statute
- regulation
- guideline
- opinion
- faq
- regulatory_qa
- enforcement_decision
- court_judgment
- ag_opinion
- consultation
- draft_rule
- work_programme
- policy_statement
- staff_letter
- corrective_action_plan
- settlement
- press_release
- secondary_index

## Source Admission Test
A source should be admitted to the authoritative corpus only if its role is explicit. Ask:
- Is it official or merely discovery material?
- What proposition types can it support?
- What is its binding scope and procedural posture?
- Is it current, future-effective, superseded, withdrawn, appealed, or stayed?
- Is the underlying full text available, or only a summary/press release?
- Can the source be versioned and re-fetched reliably?

Do not admit a source as proposition-level authority solely because it is published by a regulator; determine whether the document is binding, interpretive, procedural, promotional, or merely explanatory.

## Source Record Contract
Each admitted source should have a minimal quality record:

```yaml
source_id:
title:
jurisdiction:
authority:
authority_tier:
binding_status:
document_type:
research_roles: []
official_url:
date_published:
date_effective:
status:
primary_use:
acquisition_method:
update_frequency:
verification_status: VERIFIED_OFFICIAL | VERIFIED_SECONDARY | SECONDARY_ONLY | SOURCE_GAP
notes:
```

## Knowledge-Graph Handoff
Every admitted source should be linkable to one or more existing or prospective `ISSUE` / `PROPOSITION` nodes. Record whether the source:
- establishes a framework node;
- supports a proposition;
- supplies a factual analogue;
- calibrates enforcement;
- creates a horizon signal;
- supersedes or changes an existing source.

Do not create duplicate issue concepts merely because different jurisdictions use different terminology. Apply `shared/MULTI_JURISDICTION_PROTOCOL.md` for cross-jurisdiction source mapping.

## Required Output
Produce a **Source Map**, not a raw search-result dump. For each source state:
- what it contains;
- which layer(s) it belongs to;
- authority tier, legal effect, binding scope, and procedural status;
- whether it should be continuously crawled;
- expected update frequency;
- whether it is fit for framework, proposition-level authority, enforcement calibration, horizon monitoring, or discovery only;
- known acquisition/versioning limitations.

End with:
- **Coverage Gaps**
- **Priority Crawl List**
- **Recommended Handoff to `privacy_issue_synthesizer`**

## Research Stop / Escalation Rule
Stop source expansion when each requested jurisdiction/topic has:
- an identified official legal publisher;
- competent regulator(s);
- relevant court repository;
- official guidance/decision repository where it exists;
- a documented acquisition path or explicit acquisition limitation;
- no unresolved source gap likely to alter the intended use.

Escalate where a missing repository or inaccessible source would prevent proposition-level verification.

## Validator / Quality Gates
Before finalising a Source Map, verify:
- no aggregator has been treated as primary authority where an official source exists;
- press release and underlying decision are distinguished;
- binding status is explicit;
- publication/effective dates are not conflated;
- current and superseded versions are linked;
- the source can actually support the use assigned to it;
- crawlability claims are based on the observed site structure, not assumption;
- unresolved source gaps are visible and not silently filled;
- search failure has not been converted into a negative legal proposition;
- sources are checked for temporal status and later superseding authority;
- authority strength is assessed by binding scope, procedural posture, and issue fit, not tier alone.
