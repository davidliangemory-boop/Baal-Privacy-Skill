# Tool & Source Routing Protocol — v0.5

This protocol is tool-agnostic. Adapt the actual search/fetch tools available in the environment, but preserve the routing order.

## 1. Default Routing Order
For a proposition that should have official support:
1. official legislation / official gazette;
2. official court database;
3. official regulator database / guidance / decision repository;
4. official consultation / rulemaking repository;
5. reputable secondary legal database or professional source;
6. aggregator/tracker for discovery only.

## 2. Search Strategy
For each outcome-determinative proposition use at least two complementary query types where practical:
- **precision query** — legal term + article/section + authority + fact pattern;
- **recall query** — shorter terminology / synonyms / regulator language.

For non-English jurisdictions, search both the local language and English when this may materially improve recall.

## 3. Escalation Logic
If official source is not found:
- broaden terminology;
- search regulator/court site directly;
- search secondary indexes for document identifiers;
- follow the identifier back to official text;
- after reasonable attempts, mark `SECONDARY_ONLY` or `SOURCE_GAP`.

## 4. Primary-Text Preservation
When both a summary and full decision/guideline exist:
- store summary as `summary_of`;
- treat full official text as canonical proposition authority;
- preserve official-language original;
- link translations separately.

## 5. Search Log
For `FORMAL_OPINION_SUPPORT` or a material `SOURCE_GAP`, record:
```yaml
research_log:
  - query:
    repository:
    date:
    result:
    next_step:
```
This log is not required in the user-facing answer unless useful, but should be available for audit.

## 6. Tool Failure
A tool failure, blocked page, dynamic-site failure, or unavailable PDF is not substantive evidence. Record acquisition failure separately from legal/source absence.
