#!/usr/bin/env python3
"""
process_articles.py v1.0 — The Contrarian / FoodGameMedia
Triggered by GitHub Actions on every push to articles/*.html

What it does:
  1. Finds every article in articles/ (format: DD.MM.YY-headline-slug.html)
  2. Strips any old FGM nav, injects current version
  3. Extracts metadata (date, headline) from filename
  4. Rebuilds archive.html and archive.json in repo root

Safe to re-run — nav is always stripped and reinjected clean.
"""

import os
import re
import json
import glob
from datetime import datetime

# ─── VERSION HEADER ────────────────────────────────────────────────────────────
# v1.0 — 2026-02-28 — initial build for The Contrarian

# ─── NAV CSS ──────────────────────────────────────────────────────────────────

NAV_CSS = """\
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=DM+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
/* FGM site nav — auto-injected by process_articles.py — do not edit by hand */
.fgm-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  background: rgba(15,31,56,0.96);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(244,167,185,0.15);
  font-family: 'DM Sans', Arial, sans-serif;
}
.fgm-nav-inner {
  max-width: 1200px; margin: 0 auto;
  padding: 0 40px;
  display: flex; align-items: center; justify-content: space-between;
  height: 68px; box-sizing: border-box;
}
.fgm-nav-brand {
  font-family: 'Playfair Display', serif;
  font-size: 18px; font-weight: 900;
  text-decoration: none; color: #ffffff;
  letter-spacing: -0.3px;
}
.fgm-nav-brand span { color: #f4a7b9; }
.fgm-nav-links { display: flex; gap: 28px; align-items: center; }
.fgm-nav-links a {
  font-size: 11px; font-weight: 600; letter-spacing: 1.2px;
  text-decoration: none; color: #8a9ab5;
  transition: color 0.2s; text-transform: uppercase;
}
.fgm-nav-links a:hover { color: #f4a7b9; }
.fgm-nav-cta {
  background: #c0185d !important;
  color: #ffffff !important;
  padding: 8px 20px !important;
  border-radius: 6px;
  letter-spacing: 0.8px !important;
}
.fgm-nav-cta:hover { background: #e91e8c !important; color: #ffffff !important; }
.fgm-nav-toggle {
  display: none; background: none; border: none;
  color: #ffffff; font-size: 24px; cursor: pointer; line-height: 1; padding: 0;
}
.fgm-mobile-menu {
  display: none;
  position: fixed; top: 68px; left: 0; right: 0; bottom: 0;
  background: #1a2f52; padding: 40px;
  flex-direction: column; gap: 24px; z-index: 999;
  font-family: 'DM Sans', Arial, sans-serif;
}
.fgm-mobile-menu a {
  font-size: 16px; font-weight: 600; color: #ffffff;
  text-decoration: none; letter-spacing: 0.5px;
}
.fgm-mobile-menu a:hover { color: #f4a7b9; }
.fgm-mobile-menu.open { display: flex; }
@media (max-width: 768px) {
  .fgm-nav-links { display: none; }
  .fgm-nav-toggle { display: block; }
  .fgm-nav-inner { padding: 0 20px; }
}
body { padding-top: 88px !important; }
</style>"""

NAV_HTML = """\
<nav class="fgm-nav" id="fgmNav">
  <div class="fgm-nav-inner">
    <a class="fgm-nav-brand" href="https://foodgamemedia.com.au">Food Game <span>Media</span></a>
    <div class="fgm-nav-links">
      <a href="https://foodgamemedia.com.au/#about">About</a>
      <a href="https://foodgamemedia.com.au/#consulting">Services</a>
      <a href="https://foodgamemedia.com.au/#book">The Book</a>
      <a href="https://foodgamemedia.com.au/#podcast">Podcast</a>
      <a href="https://foodgamemedia.com.au/newsletter.html">Newsletter</a>
      <a href="https://foodgamemedia.com.au/contrarian.html" class="fgm-nav-cta">The Contrarian</a>
    </div>
    <button class="fgm-nav-toggle"
      onclick="document.getElementById('fgmMobile').classList.toggle('open')"
      aria-label="Toggle menu">&#9776;</button>
  </div>
</nav>
<div class="fgm-mobile-menu" id="fgmMobile">
  <a href="https://foodgamemedia.com.au/#about">About</a>
  <a href="https://foodgamemedia.com.au/#consulting">Services</a>
  <a href="https://foodgamemedia.com.au/#book">The Book</a>
  <a href="https://foodgamemedia.com.au/#podcast">Podcast</a>
  <a href="https://foodgamemedia.com.au/newsletter.html">Newsletter</a>
  <a href="https://foodgamemedia.com.au/contrarian.html">The Contrarian &rarr;</a>
</div>"""

# ─── NAV INJECTION ────────────────────────────────────────────────────────────

def already_injected(html):
    return 'class="fgm-nav"' in html or 'fgm-nav-brand' in html

def strip_nav(html):
    """Remove previously injected nav so current version can be reinjected cleanly."""
    html = re.sub(r'<link[^>]*Playfair[^>]*>\s*', '', html)
    html = re.sub(r'<style>\s*/\* FGM site nav.*?</style>\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<nav class="fgm-nav".*?</nav>\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="fgm-mobile-menu".*?</div>\s*', '', html, flags=re.DOTALL)
    return html

def inject_nav(html):
    if '</head>' in html:
        html = html.replace('</head>', NAV_CSS + '\n</head>', 1)
    else:
        html = NAV_CSS + '\n' + html

    body_match = re.search(r'<body[^>]*>', html, re.IGNORECASE)
    if body_match:
        pos = body_match.end()
        html = html[:pos] + '\n' + NAV_HTML + '\n' + html[pos:]
    else:
        html = NAV_HTML + '\n' + html

    return html

# ─── METADATA EXTRACTION ──────────────────────────────────────────────────────

# Filename format: DD.MM.YY-headline-slug-source-slug.html
FILENAME_RE = re.compile(r'^(\d{2})\.(\d{2})\.(\d{2})-(.+)\.html$', re.IGNORECASE)

def extract_metadata(filepath):
    filename = os.path.basename(filepath)
    url = 'https://foodgamemedia.github.io/The-Contrarian/articles/' + filename

    m = FILENAME_RE.match(filename)
    if m:
        dd, mm, yy, slug = m.group(1), m.group(2), m.group(3), m.group(4)
        year = '20' + yy
        try:
            dt = datetime.strptime(f'{dd}/{mm}/{year}', '%d/%m/%Y')
            date_display = dt.strftime('%-d %b %Y')
            sort_key = dt.strftime('%Y%m%d')
        except ValueError:
            date_display = f'{dd}.{mm}.{yy}'
            sort_key = yy + mm + dd

        # Humanise slug: strip trailing source slug (last segment after final hyphen group)
        # Headline slug is everything; title-case it for display
        headline = slug.replace('-', ' ').title()
    else:
        date_display = ''
        sort_key = '00000000'
        headline = filename.replace('.html', '').replace('-', ' ').title()
        url = 'https://foodgamemedia.github.io/The-Contrarian/articles/' + filename

    # Try to pull real headline from HTML <title> or article header
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        # Look for the article headline in the rendered piece header
        title_match = re.search(r'font-style:italic[^>]*>([^<]{10,120})</div>', html)
        if not title_match:
            # Fallback: <title> tag
            title_match = re.search(r'<title>([^<]{5,120})</title>', html, re.IGNORECASE)
        if title_match:
            candidate = title_match.group(1).strip()
            # Ignore generic titles
            if 'Contrarian' not in candidate or len(candidate) > 20:
                headline = candidate
    except Exception:
        pass

    return {
        'filename': filename,
        'date': date_display,
        'sort_key': sort_key,
        'headline': headline,
        'url': url,
    }

# ─── ARCHIVE BUILD ────────────────────────────────────────────────────────────

ARCHIVE_HTML_TEMPLATE = """\
<!DOCTYPE html>
<!-- archive.html v1.0 — auto-rebuilt by process_articles.py — do not edit by hand -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Contrarian · Archive · Food Game Media</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,900&family=DM+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'DM Sans',Arial,sans-serif; background:#fdf0f5; color:#0f1f38; }}
.archive-header {{
  background: #0f1f38; padding: 80px 40px 60px; text-align: center;
}}
.archive-header .overline {{
  font-size: 9px; letter-spacing: 4px; text-transform: uppercase;
  color: #f4a7b9; margin-bottom: 16px; font-weight: 600;
}}
.archive-header h1 {{
  font-family: 'Playfair Display', serif; font-size: clamp(32px,5vw,56px);
  font-weight: 900; font-style: italic; color: #fff; letter-spacing: -1px;
}}
.archive-header .rule {{
  width: 48px; height: 2px;
  background: linear-gradient(90deg, transparent, #f4a7b9, transparent);
  margin: 20px auto;
}}
.archive-header p {{
  font-size: 13px; color: rgba(138,154,181,0.7); letter-spacing: 0.3px;
}}
.archive-grid {{
  max-width: 880px; margin: 0 auto; padding: 60px 32px;
  display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 24px;
}}
.article-card {{
  background: #fff; border-radius: 12px; overflow: hidden;
  box-shadow: 0 2px 12px rgba(15,31,56,0.08);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  text-decoration: none; display: block; color: inherit;
}}
.article-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(15,31,56,0.15);
}}
.card-header {{
  background: #0f1f38; padding: 24px 28px 20px;
}}
.card-date {{
  font-size: 9px; letter-spacing: 2.5px; text-transform: uppercase;
  color: rgba(244,167,185,0.7); margin-bottom: 10px; font-weight: 600;
}}
.card-headline {{
  font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 900;
  font-style: italic; color: #fff; line-height: 1.25; letter-spacing: -0.3px;
}}
.card-body {{
  padding: 18px 28px 24px; display: flex; align-items: center; justify-content: space-between;
}}
.card-read {{
  font-size: 11px; font-weight: 600; letter-spacing: 1px;
  text-transform: uppercase; color: #e91e8c;
}}
.card-arrow {{ color: #f4a7b9; font-size: 14px; }}
@media (max-width: 600px) {{
  .archive-grid {{ grid-template-columns: 1fr; padding: 32px 16px; }}
  .archive-header {{ padding: 100px 20px 48px; }}
}}
</style>
</head>
<body>
{nav_css}
{nav_html}
<div class="archive-header">
  <div class="overline">Food Game Media</div>
  <h1>The Contrarian</h1>
  <div class="rule"></div>
  <p>Every piece, newest first.</p>
</div>
<div class="archive-grid">
{cards}
</div>
</body>
</html>"""

def build_card(article):
    return f"""\
  <a class="article-card" href="{article['url']}">
    <div class="card-header">
      <div class="card-date">{article['date']}</div>
      <div class="card-headline">{article['headline']}</div>
    </div>
    <div class="card-body">
      <span class="card-read">Read the piece</span>
      <span class="card-arrow">→</span>
    </div>
  </a>"""

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    articles_dir = 'articles'
    pattern = os.path.join(articles_dir, '*.html')
    files = sorted(glob.glob(pattern))
    files = [f for f in files if os.path.basename(f) != '.gitkeep']

    if not files:
        print('No article files found — nothing to do.')
        return

    articles = []

    for filepath in files:
        filename = os.path.basename(filepath)
        print(f'Processing: {filename}')

        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Always strip + reinject so nav stays current
        if already_injected(html):
            html = strip_nav(html)
        html = inject_nav(html)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  Nav: injected')

        meta = extract_metadata(filepath)
        articles.append(meta)
        print(f'  Meta: {meta["date"]} · {meta["headline"][:60]}')

    # Newest first
    articles.sort(key=lambda x: x['sort_key'], reverse=True)

    # Rebuild archive.html
    cards = '\n'.join(build_card(a) for a in articles)
    archive_html = ARCHIVE_HTML_TEMPLATE.format(
        nav_css=NAV_CSS,
        nav_html=NAV_HTML,
        cards=cards,
    )
    with open('archive.html', 'w', encoding='utf-8') as f:
        f.write(archive_html)
    print(f'\narchive.html rebuilt — {len(articles)} articles')

    # Rebuild archive.json
    json_data = [
        {
            'date':     a['date'],
            'headline': a['headline'],
            'url':      a['url'],
        }
        for a in articles
    ]
    with open('archive.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print(f'archive.json rebuilt — {len(articles)} articles')

if __name__ == '__main__':
    main()
