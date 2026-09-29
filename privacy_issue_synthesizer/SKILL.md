# privacy_issue_synthesizer — v0.6

## Purpose
Turn a concrete data privacy / data protection issue into a structured, source-grounded legal analysis using a four-step research process. This skill answers: **how should this issue be analysed, what is the current position, which uncertainties require authority, how strong is the evidence, and what may change next?**

## Operating Principles
0. **Apply shared contracts.** Follow `../shared/LEGAL_EPISTEMICS.md`, `../shared/AUTHORITY_EFFECT_PROTOCOL.md`, `../shared/ANALOGICAL_FIT_PROTOCOL.md`, `../shared/HORIZON_SIGNAL_PROTOCOL.md`, `../shared/KNOWLEDGE_GRAPH_CONTRACT.md`, `../shared/MULTI_JURISDICTION_PROTOCOL.md`, `../shared/OPERATING_MODES.md`, `../shared/TOOL_ROUTING_PROTOCOL.md`, and `../SHARED_EVIDENCE_CONTRACT.md`.
1. **Framework first, cases second.** Build the issue tree before searching factually similar cases.
2. **Proposition-level sourcing.** Every material legal proposition should be traceable to an identified authority or explicitly marked as unsupported.
3. **No silent supplement.** If research does not support a proposition, do not fill the gap from model memory. Mark `SOURCE_GAP`, `UNVERIFIED`, or state the assumption.
4. **Separate law, inference, and recommendation.** A legal rule, a factual inference, and a business recommendation are different outputs.
5. **Counter-authority matters.** Search for narrowing, conflicting, superseding, or jurisdiction-specific authority where the proposition is contestable.
6. **Current-law discipline.** Drafts, consultations and speeches may inform Horizon analysis but must not be presented as current binding law.

## Select Operating Mode
Select one before research:
- `RAPID_SCREEN`
- `STANDARD_ANALYSIS` (default)
- `FORMAL_OPINION_SUPPORT`
- `MULTI_JURISDICTION_MATRIX`
- `DEEP_RESEARCH`

The selected mode determines search depth, source standard, output length, and stop condition.

## Inputs
- Specific issue / legal question
- Relevant facts
- Jurisdiction(s)
- Business context
- Time sensitivity / decision deadline
- Existing source map / corpus if any
- Existing issue framework / prior conclusion if any

## Step 0 — Research Scoping
Before the four-step analysis:
- restate the issue as one or more legal propositions;
- identify missing facts that could change the answer;
- identify the decision that the client/business actually needs to make;
- set the required authority level: screening / internal advice / board paper / formal legal opinion;
- tag each proposed proposition as `LEGAL_RULE`, `LEGAL_TEST`, `FACTUAL_PREDICATE`, `APPLICATION_INFERENCE`, `ENFORCEMENT_SIGNAL`, `PRACTICAL_RECOMMENDATION`, or `HORIZON_SIGNAL`;
- define a research stop condition: what must be verified before the business decision can safely be made.

## Issue-State Setup
Create or update an `ISSUE` record before research. Mark initial status `DRAFT` or `RESEARCHING`. Identify material facts as `FACT` nodes and tag each as `CONFIRMED`, `ASSUMED`, `DISPUTED`, or `UNKNOWN`. A dispositive unknown fact must remain visible through conclusion.

For multi-jurisdiction questions, normalise the business question first, then preserve each jurisdiction's own legal test.

## Four-Step Workflow

### Step 1 — Source Base
Apply the source-routing hierarchy in `shared/TOOL_ROUTING_PROTOCOL.md`. For formal or deep research, preserve a search log for material source gaps.

Confirm the applicable legal universe:
- statutes / regulations
- competent regulators
- relevant court hierarchy
- core official guidance / decision repositories

Output only enough to establish that the applicable source universe is reasonably complete.

If a source universe is missing, trigger or request `privacy_source_mapper` before drawing a strong conclusion.

### Step 2 — Framework
Build the **Issue Tree / Legal Test** before searching cases.

Convert framework materials into:
- threshold questions
- legal tests
- required factors
- exceptions
- factual pivots
- burdens / evidence
- procedural requirements
- remediation / governance consequences

Preferred structure:
**Issue → Rule → Test → Factors → Exceptions → Factual Pivots → Preliminary Conclusion**

For each branch create or update a proposition node and identify whether it is:
- dispositive;
- cumulative;
- balancing-based;
- procedural;
- evidentiary;
- jurisdiction-specific.

### Step 3 — Issue Resolution
For each unresolved factual or doctrinal point, search targeted authority:
- regulator FAQ / Q&A
- official opinions
- binding decisions
- court judgments
- AG opinions
- enforcement decisions
- staff letters / policy statements

For each material proposition create an evidence record:

```yaml
proposition_id:
issue_id:
proposition_type:
proposition:
conclusion:
authority:
authority_tier:
legal_effect:
binding_status:
source_type:
source_url:
source_date:
effective_date:
pinpoint:
quoted_support:
facts_relied_upon:
interpretation:
counter_authority:
limitations:
support_status: VERIFIED | PARTIALLY_VERIFIED | UNVERIFIED | CONFLICTED | NO_AUTHORITY_LOCATED
legal_confidence: high | medium | low
factual_confidence: high | medium | low
temporal_status:
last_verified_at:
```

#### Analogical-Fit Check
When using a case, enforcement decision, FAQ example, or other fact-specific authority, apply `shared/ANALOGICAL_FIT_PROTOCOL.md` and label the analogy `DIRECT`, `STRONG_ANALOGY`, `LIMITED_ANALOGY`, or `BACKGROUND_ONLY`.

#### Quote-to-Proposition Check
Before relying on a source, verify:
- the quoted or paraphrased passage actually supports the proposition;
- the statement is the court/regulator's position, not merely a party argument;
- the cited passage is holding / operative reasoning rather than incidental dicta where that distinction matters;
- the source is current and not superseded;
- the factual pattern is sufficiently analogous if the proposition depends on facts.

#### Negative-Evidence Check
Do not infer that a requirement, prohibition, or enforcement practice does not exist merely because no case or FAQ was located. Use `NO_AUTHORITY_LOCATED` and describe the search scope.

#### Temporal Check
For outcome-determinative propositions, verify whether the authority is still in force and whether later amendments, judgments, guidance, appeals, stays, or withdrawals materially alter it.

#### Counter-Authority Check
For any proposition that is material, novel, jurisdictionally contested, or outcome-determinative, search for:
- contrary authority;
- narrower authority;
- later superseding authority;
- different treatment by another competent regulator/court;
- national-law overlays.

### Step 4 — Horizon
Identify whether the current conclusion may change in the next 6–24 months through:
- draft guidance
- consultations
- proposed rulemaking
- legislative proposals
- regulator work programmes
- policy statements / speeches
- pending appeals or cases likely to alter doctrine

Always separate:
- **Current Law**
- **Emerging Regulatory Position**
- **Possible Future Change**

For each horizon item apply `shared/HORIZON_SIGNAL_PROTOCOL.md` and assess:
- adoption probability;
- legal impact if adopted;
- expected timing;
- business implementation lead time;
- issue-tree nodes affected;
- whether preparation should begin before the legal change becomes effective.

## Proposition Dependency Graph
Identify dependencies among propositions and facts. Do not treat the issue tree as a flat checklist. Mark outcome-determinative root propositions and downstream propositions that depend on them.

Example:
`P3 consent required` → `depends_on` → `P1 data is sensitive` + `P2 no employment exception` + `F4 purpose is biometric identification`.

## Operational Control Linkage
For each final recommendation, distinguish `REQUIRED`, `RECOMMENDED`, or `OPTIONAL` and link it to the legal proposition(s) supporting it. Do not convert a conservative business recommendation into a statement of law.

## Source Relationship Graph
Where useful, link materials using controlled relationships:
- interprets
- applies
- clarifies
- narrows
- expands
- distinguishes
- cites
- conflicts_with
- supersedes
- amends
- enforces
- proposes_change_to
- appeals
- implements
- factually_analogous_to

## Decision Gate Before Output
Before finalising, ask:
1. Which proposition actually determines the business answer?
2. Is that proposition verified at the authority level required by the operating mode?
3. Which facts would reverse or materially narrow the conclusion?
4. Would more research reasonably change the decision?

If the answer to (2) is no and the issue is material, do not provide an unqualified conclusion. If (4) is no, stop researching and disclose bounded uncertainty.

## Required Output Format
1. **Issue** — one sentence
2. **Executive Conclusion** — concise answer with confidence and principal qualification
3. **Decision-Relevant Facts** — facts that materially drive the answer
4. **Analytical Framework** — issue tree / legal tests
5. **Key Uncertainties** — unresolved law or facts
6. **Authority & Case Resolution** — proposition-by-proposition analysis with support status
7. **Counter-Authority / Limits** — material contrary or narrowing sources
8. **Regulatory Direction** — forward-looking developments
9. **Practical Legal Action** — concrete business/legal next steps
10. **Evidence Gaps** — what could not be verified and why
11. **Research Boundary** — sources searched, material residual uncertainty, and why additional research is or is not expected to change the decision

## Confidence Protocol
Do not use a single undifferentiated confidence score. Distinguish:
- **legal confidence** — strength/clarity of authority;
- **factual confidence** — completeness/reliability of facts;
- **forward-looking confidence** — uncertainty of pending changes.

## Issue Lifecycle at Completion
Set the issue status:
- `VERIFIED` if outcome-determinative propositions and facts are adequately verified;
- `QUALIFIED` if usable but materially assumption-dependent;
- `CONFLICTED` if unresolved authority conflict could change the answer.

## Re-analysis Triggers
Re-open the issue if any of the following occurs:
- binding law changes;
- regulator adopts or withdraws key guidance;
- higher court reverses or materially narrows authority;
- a material factual assumption changes;
- new evidence changes support status;
- `privacy_regulatory_delta_monitor` returns `REANALYSIS_REQUIRED`.

## Validator / Quality Gates
Before finalising:
- framework was built before case collection;
- no general rule is inferred from a handful of enforcement cases when higher authority exists;
- binding authority, guidance, consultation, and commentary are distinguished;
- each material proposition has a support status;
- no unsupported proposition has been silently completed from memory;
- quotations and paraphrases actually support the proposition cited;
- counter-authority has been considered for contestable points;
- draft guidance is not presented as current law;
- factual assumptions are explicit;
- conclusion strength matches the evidence strength;
- enforcement signals are not presented as binding rules;
- recommendations are distinguished from legal requirements;
- no negative legal proposition is based only on search failure;
- temporal status and later authority have been checked for outcome-determinative propositions.
