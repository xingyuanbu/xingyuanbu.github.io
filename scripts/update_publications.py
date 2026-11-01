#!/usr/bin/env python3
"""Rebuild the static publication list from data/publications.json. No dependencies."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def render(pub):
    title = escape(pub['title'])
    url = pub.get('paper') or pub.get('scholar')
    title_html = f'<a href="{escape(url, quote=True)}">{title}</a>' if url else title
    authors = escape(pub.get('authors', ''))
    authors = authors.replace('X Bu∗†', '<strong>Xingyuan Bu*†</strong>')
    authors = authors.replace('X Bu∗', '<strong>Xingyuan Bu*</strong>')
    authors = authors.replace('X Bu†', '<strong>Xingyuan Bu†</strong>')
    authors = authors.replace('X Bu', '<strong>Xingyuan Bu</strong>')
    links = []
    for key, label in [('paper', 'Paper'), ('code', 'Code'), ('scholar', 'Scholar')]:
        if pub.get(key):
            links.append(f'<a href="{escape(pub[key], quote=True)}" aria-label="{label}: {title}">{label} ↗</a>')
    preprint = ' preprint' if pub['venue'].startswith('arXiv') else ''
    note = f'<span class="pub-note">{escape(pub["note"])}</span>' if pub.get('note') else ''
    return f'''          <article class="publication" data-year="{pub['year']}" data-area="{pub['area']}" data-selected="{str(pub['selected']).lower()}">
            <div class="pub-year">{pub['year']}</div>
            <div><h3 class="pub-title">{title_html}</h3>
              {f'<p class="pub-authors">{authors}</p>' if authors else ''}
              <div class="pub-meta"><span class="venue{preprint}">{escape(pub['venue'])}</span><span class="pub-links">{' '.join(links)}</span>{note}</div>
            </div>
          </article>'''

def main():
    pubs = json.loads((ROOT / 'data/publications.json').read_text())
    pubs.sort(key=lambda p: p['year'], reverse=True)  # Stable: retain CV order within each year.
    page = (ROOT / 'index.html').read_text()
    start, end = '<!-- PUBLICATIONS:START -->', '<!-- PUBLICATIONS:END -->'
    before, remainder = page.split(start)
    _, after = remainder.split(end)
    page = before + start + '\n' + '\n'.join(map(render, pubs)) + '\n' + end + after
    page = re.sub(r'All papers <span>\d+</span>', f'All papers <span>{len(pubs)}</span>', page)
    page = re.sub(r'View all \d+ publications', f'View all {len(pubs)} publications', page)
    page = re.sub(r'(<p id="paper-count" aria-live="polite">)\d+ papers', rf'\g<1>{len(pubs)} papers', page)
    (ROOT / 'index.html').write_text(page)
    print(f'Rendered {len(pubs)} publications ({sum(p["selected"] for p in pubs)} selected).')

if __name__ == '__main__':
    main()
