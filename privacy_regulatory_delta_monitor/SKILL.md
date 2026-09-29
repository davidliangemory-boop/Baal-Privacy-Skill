# privacy_regulatory_delta_monitor — v0.6

## Purpose
Monitor legal and regulatory changes in data privacy and determine whether a new development changes any existing issue framework, legal conclusion, compliance control, or business action. This skill answers: **what changed, which existing issues are affected, how material is the change, and what must be re-opened or updated?**

## Operating Principle
**No-silent-supplement:** if a claimed legal change cannot be verified against adequate authority, keep it as an unverified signal rather than filling the gap from memory or secondary reporting. Link related proposal/consultation/adoption/effective-date items into a single event lifecycle to prevent duplicate “changes.”

Apply `../shared/LEGAL_EPISTEMICS.md`, `../shared/AUTHORITY_EFFECT_PROTOCOL.md`, `../shared/HORIZON_SIGNAL_PROTOCOL.md`, `../shared/KNOWLEDGE_GRAPH_CONTRACT.md`, `../shared/OPERATING_MODES.md`, `../shared/TOOL_ROUTING_PROTOCOL.md`, and `../SHARED_EVIDENCE_CONTRACT.md`.

This is **delta-based, state-aware research**. Do not re-summarize the entire legal landscape every day.

## Operating Modes
Use:
- `DAILY_ISSUE_BRIEF` for one concrete issue monitored day by day;
- default delta mode for a portfolio of issues/sources;
- `DEEP_RESEARCH` when a delta creates a material conflict or unclear doctrinal shift.

## Inputs
- Existing source map / corpus
- Existing issue frameworks / issue graph
- Existing proposition/evidence records
- Jurisdictions and topics to monitor
- Time window since last run
- Last-seen source versions / hashes if available

## State Model
Maintain or consume the following state where available:
- source_id
- prior_version_id
- current_version_id
- prior_content_hash
- current_content_hash
- last_seen_at
- publication_date
- effective_date
- status
- affected_issue_ids
- affected_proposition_ids
- prior_conclusion
- current_conclusion

## Step 1 — Detect Delta
Identify only new or changed items, including:
- new documents
- new stage in an existing regulatory event chain (proposal → consultation → adoption → effective date → enforcement)
- updated documents
- corrected or replaced versions
- new decisions
- new consultations
- consultation closed
- draft → final
- proposal → adopted
- guidance withdrawn
- judgment appealed
- judgment overturned / varied
- rule effective date approaching
- effective date postponed
- regulator announces enforcement priority

Where possible, distinguish a true substantive delta from:
- formatting changes;
- URL migration;
- metadata-only changes;
- duplicate publication;
- translated/reposted copies.

## Step 2 — Validate the Delta
Before analysing legal significance:
- confirm the source is official or clearly label secondary-only discovery;
- confirm publication/update date;
- compare current text against the prior version where available;
- identify the exact changed provision, paragraph, test, threshold, remedy, or effective date;
- suppress false-positive changes caused by republishing or web-page restructuring.

If the underlying document cannot be verified, mark `UNVERIFIED_DELTA` and do not trigger a strong substantive conclusion. If expected official material cannot be located after targeted research, record `SOURCE_GAP`; do not infer that no change occurred.

## Step 3 — Assess Legal Significance
For every validated delta determine:
- whether it is a new event or merely a new stage/version of an existing regulatory event;
- affected topic(s)
- affected issue(s)
- affected proposition(s)
- authority tier, legal effect, binding scope, procedural posture, temporal status, and issue fit
- whether the change affects a legal test, factual threshold, burden, remedy, procedure, enforcement posture, or timing
- materiality: low / medium / high / critical

Use these impact labels:
- `NO_CHANGE`
- `CLARIFICATION_ONLY`
- `NARROWS_POSITION`
- `EXPANDS_POSITION`
- `NEW_EXCEPTION`
- `HIGHER_ENFORCEMENT_RISK`
- `LOWER_ENFORCEMENT_RISK`
- `PROCEDURAL_CHANGE`
- `EFFECTIVE_DATE_CHANGE`
- `CONFLICT_CREATED`
- `REANALYSIS_REQUIRED`

## Step 4 — Propagate Through Existing Issue Graph
Do not stop at direct topic tagging. Apply dependency-aware propagation:
1. changed source → directly supported proposition;
2. direct proposition → dependent propositions;
3. dependent propositions → affected issue conclusions;
4. affected propositions → linked operational controls;
5. mark nodes `STALE` or `REOPENED` where appropriate.

Refresh only the affected branch unless the changed authority alters the root legal framework.

Map the delta to affected framework nodes and existing conclusions.

For each affected issue state:
- issue_id / issue name
- framework node affected
- prior proposition/conclusion
- changed authority
- revised proposition/conclusion, if determinable
- whether the existing issue must be re-run

Do not merely tag a topic; link the change to the **specific proposition or legal test** it affects where possible.

## Step 5 — Trigger Re-analysis / Knowledge Backfill
Where material, instruct `privacy_issue_synthesizer` to re-run the affected issue and update:
- Executive Conclusion
- Analytical Framework
- Authorities
- Counter-Authority
- Practical Actions
- Horizon
- Evidence support status

Use trigger thresholds:
- **Critical / High + binding:** re-analysis required.
- **High + persuasive:** re-analysis normally required.
- **Medium:** targeted proposition refresh.
- **Low:** metadata/update log only unless cumulative pattern emerges.

## Delta Record Contract
For each material change create:

```yaml
delta_id:
source_id:
old_version_id:
new_version_id:
authority:
document:
status:
publication_date:
effective_date:
changed_text_or_rule:
affected_issue_ids:
affected_proposition_ids:
affected_control_ids: []
dependency_path: []
impact_label:
materiality:
prior_position:
new_position:
verification_status: VERIFIED | PARTIALLY_VERIFIED | UNVERIFIED_DELTA
reanalysis_required: true | false
action:
```

## Four-Step Daily Issue Brief Mode
When monitoring one concrete issue, structure each run around the same four legal-research layers:
1. **Source Base Delta** — new/updated authoritative sources;
2. **Framework Delta** — changes to issue tree, legal test, thresholds, exceptions, burdens;
3. **Issue-Resolution Delta** — new FAQ, decision, judgment, enforcement action, staff opinion, or factual analogue affecting a specific proposition;
4. **Horizon Delta** — draft, consultation, proposed law, work programme, policy signal, pending appeal.

Then state whether the **current conclusion changed** and whether `privacy_issue_synthesizer` must re-run. Use `templates/daily_issue_brief.md`.

## Daily Output Format
### Daily Privacy Delta — [Date]

**Material Change**
- Authority / document / status

**Affected Issues**
- issue names / framework nodes / proposition IDs

**What Changed**
- concise legal delta, not a news summary

**Impact on Existing Position**
- impact label + explanation

**Action**
- no action / update metadata / targeted proposition refresh / re-run issue analysis / business follow-up

**Evidence Status**
- VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED_DELTA

If nothing material changed, output:
**No material change to existing issue frameworks today.**

## Weekly Roll-Up
For a weekly summary, aggregate only:
- new high/critical deltas;
- repeated medium deltas forming a trend;
- approaching effective dates;
- unresolved conflicts;
- issues awaiting re-analysis.

Do not duplicate daily low-value items.

## Validator / Quality Gates
Before finalising:
- no filler news is included;
- every material delta is verified against the underlying source where reasonably possible;
- effective law is separated from proposals and drafts;
- publication, adoption, and effective dates are distinguished;
- version history is preserved;
- false deltas from republishing/format changes are suppressed;
- the affected legal proposition is identified, not merely the topic;
- conclusion changes are proportionate to binding scope, procedural posture, issue fit, and actual textual change;
- a new enforcement action is not automatically treated as a new general legal rule;
- a new draft/consultation is never promoted to current law;
- absence of a new item is not treated as evidence that regulator policy is unchanged unless the monitored universe is demonstrably complete;
- unresolved conflicts remain visible rather than being harmonised without support.
