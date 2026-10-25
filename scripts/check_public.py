# SPDX-License-Identifier: GPL-3.0-or-later
"""Check static package references and publication boundaries; not a client audit."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
issues = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            if values['id'] in self.ids:
                issues.append(f'duplicate id: {values["id"]}')
            self.ids.add(values['id'])
        if 'href' in values:
            self.links.append(values['href'])
        if tag == 'form':
            issues.append('unexpected data collection form')

files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
for p in files:
    if p.suffix not in ('.md', '.html'):
        continue
    content = p.read_text(encoding='utf-8')
    links = re.findall(r'\]\(([^\s)]+)\)', content)
    if p.suffix == '.html':
        parser = Links()
        parser.feed(content)
        links.extend(parser.links)
        for link in parser.links:
            if link.startswith('#') and link[1:] not in parser.ids:
                issues.append(f'{p.relative_to(ROOT)}: missing anchor {link}')
        if 'Esempio illustrativo, non audit cliente.' not in content:
            issues.append('landing must label fictional examples')
        if 'tuo-indirizzo@' in content or 'e3b0c442' in content:
            issues.append('placeholder contact or invented digest in landing')
    for link in links:
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
            continue
        target = (p.parent / link.split('#')[0]).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            issues.append(f'{p.relative_to(ROOT)}: invalid local link {link}')

required = ['LICENSE', 'NOTICE', 'README.md', 'README.it.md', '.github/FUNDING.yml', 'SUPPORT.md', 'SECURITY.md', 'site/index.html', 'examples/report.md']
issues.extend(f'missing {name}' for name in required if not (ROOT / name).is_file())
core_lines = sum(len(p.read_text(encoding='utf-8').splitlines()) for p in files if p.suffix in ('.py', '.html'))
if core_lines >= 1500:
    issues.append(f'static core exceeds 1500 lines: {core_lines}')
if issues:
    raise SystemExit('\n'.join(issues))
print(f'PASS: {len(files)} files; local links, anchors, public scope; {core_lines} core lines < 1500.')
