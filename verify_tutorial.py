"""Verify the learning artifact's coverage, navigation, fixtures and local demo."""
import csv
import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'tutorial.json').read_text())
sources = json.loads((ROOT / 'sources.json').read_text())
errors = []
actual_folders = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith('.'))
expected_folders = sorted(c['folder'] for c in data['chapters'])
if actual_folders != expected_folders or len(expected_folders) != 10:
    errors.append('Expected exactly the ten approved chapter folders')
if sorted(s['id'] for s in sources) != list(range(1, 109)):
    errors.append('Source IDs must cover all 108 navigation entries once')
for source in sources:
    if not (ROOT / source['local_path']).is_file():
        errors.append(f"Missing mapped lesson for S{source['id']:03d}")
    if not source['url'].startswith(('https://www.ibm.com/', 'https://bob.ibm.com/')):
        errors.append(f"Unexpected source host: {source['url']}")
    if f"S{source['id']:03d}:" not in (ROOT / source['local_path']).read_text():
        errors.append(f"Mapped lesson lacks citation S{source['id']:03d}")
lesson_count = 0
for chapter in data['chapters']:
    for lesson in chapter['lessons']:
        lesson_count += 1
        text = (ROOT / lesson['path']).read_text()
        for heading in ('## In plain English', '## Try it: original exercise', '## Check your understanding', '## Common mistake', '## IBM sources'):
            if heading not in text:
                errors.append(f"Missing {heading}: {lesson['path']}")
if lesson_count != data['lesson_count']:
    errors.append('Lesson count does not match manifest')
markdown_files = list(ROOT.rglob('*.md'))
link_count = 0
for path in markdown_files:
    text = path.read_text()
    if re.search(r'turn\d+(?:view|search)\d+|TODO|FIXME|PLACEHOLDER', text):
        errors.append(f'Unresolved marker in {path.relative_to(ROOT)}')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        link_count += 1
        resolved = (path.parent / unquote(target.split('#')[0])).resolve()
        if not resolved.exists():
            errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')
        if not resolved.is_relative_to(ROOT):
            errors.append(f'Link leaves repository: {target}')
with (ROOT / '05-lifecycle-and-operations/example_tickets.csv').open(newline='') as stream:
    tickets = list(csv.DictReader(stream))
expected = json.loads((ROOT / '05-lifecycle-and-operations/expected_ticket_results.json').read_text())['expected']
if {t['ticket_id'] for t in tickets} != set(expected) or len(tickets) != len(expected):
    errors.append('Synthetic ticket coverage mismatch')
spec = importlib.util.spec_from_file_location('demo', ROOT / '02-components/tool_calling_demo.py')
demo = importlib.util.module_from_spec(spec)
# Avoid creating an extra __pycache__ directory in the ten-folder learning structure.
exec(compile((ROOT / '02-components/tool_calling_demo.py').read_text(), 'tool_calling_demo.py', 'exec'), demo.__dict__)
if demo.dispatch({'name':'add','arguments':{'a':'18','b':'24'}}) != '42':
    errors.append('Local tool calculation mismatch')
for request in [
    {'name':'shell','arguments':{'a':'18','b':'24'}},
    {'name':'add','arguments':{'a':'18','b':'24','extra':'ignored'}},
    {'name':'add','arguments':{'a':'NaN','b':'24'}},
]:
    try:
        demo.dispatch(request)
        errors.append('Invalid tool call was accepted')
    except ValueError:
        pass
result = dict(chapters=10, lessons=lesson_count, source_entries=len(sources), markdown_files=len(markdown_files), local_links_checked=link_count, synthetic_tickets=len(tickets), tool_demo='valid calculation and invalid-call rejection passed', errors=errors)
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
