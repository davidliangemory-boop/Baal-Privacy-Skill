from pathlib import Path
import sys

base = Path(__file__).resolve().parent
required = [
    'README.md','CHANGELOG.md','SHARED_EVIDENCE_CONTRACT.md','EVALUATION.md',
    'privacy_source_mapper/SKILL.md','privacy_issue_synthesizer/SKILL.md','privacy_regulatory_delta_monitor/SKILL.md',
    'shared/LEGAL_EPISTEMICS.md','shared/AUTHORITY_EFFECT_PROTOCOL.md','shared/ANALOGICAL_FIT_PROTOCOL.md',
    'shared/HORIZON_SIGNAL_PROTOCOL.md','shared/KNOWLEDGE_GRAPH_CONTRACT.md','shared/MULTI_JURISDICTION_PROTOCOL.md',
    'shared/OPERATING_MODES.md','shared/TOOL_ROUTING_PROTOCOL.md',
    'templates/issue_record.yaml','templates/proposition_record.yaml','templates/delta_record.yaml','templates/daily_issue_brief.md',
    'benchmarks/BENCHMARK_SCHEMA.yaml','benchmarks/SCORING_RUBRIC.md','benchmarks/SEED_SET.md'
]
errors=[]
for rel in required:
    if not (base/rel).exists():
        errors.append(f'MISSING {rel}')

skills = [base/'privacy_source_mapper/SKILL.md', base/'privacy_issue_synthesizer/SKILL.md', base/'privacy_regulatory_delta_monitor/SKILL.md']
for p in skills:
    if not p.exists():
        continue
    t=p.read_text().lower()
    for token in ['source_gap','validator','current']:
        if token not in t:
            errors.append(f'{p.name}: missing expected token {token}')

issue=(base/'privacy_issue_synthesizer/SKILL.md').read_text().lower()
for token in ['source base','framework','issue resolution','horizon','analogical-fit','legal_effect']:
    if token not in issue:
        errors.append(f'issue synthesizer missing {token}')

delta=(base/'privacy_regulatory_delta_monitor/SKILL.md').read_text().lower()
for token in ['daily_issue_brief','event chain','reanalysis_required']:
    if token not in delta:
        errors.append(f'delta monitor missing {token}')

mapper=(base/'privacy_source_mapper/SKILL.md').read_text().lower()
if 'research_roles' not in mapper:
    errors.append('source mapper must use research_roles')
if 'source_layer:' in mapper:
    errors.append('source mapper still contains deprecated source_layer field')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS — {len(required)} required files and core acceptance checks')
