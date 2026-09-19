#!/usr/bin/env python3
"""Rebuild the sprite, catalog, index, and complete white/dark SVG sheets."""
import json
import math
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
WIDTH = 1600
COLUMNS = 8
MARGIN = 48
GAP = 16
TILE_WIDTH = (WIDTH - 2 * MARGIN - (COLUMNS - 1) * GAP) // COLUMNS
ROW_HEIGHT = 124


def text(x, y, value, size=12, color='#747a86', weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'


def display_svg(source, icon_id, x, y, size=48):
    return source.replace('<svg ', f'<svg data-icon-id="{escape(icon_id)}" x="{x}" y="{y}" ', 1).replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)


def complete_sheet(data, sources, dark=False):
    sections = []
    cursor = 160
    for collection in data['collections']:
        icons = [item for item in data['icons'] if item['domain'] == collection['id']]
        if not icons:
            continue
        sections.append((collection, icons, cursor))
        cursor += 72 + math.ceil(len(icons) / COLUMNS) * ROW_HEIGHT + 24
    height = cursor + 56
    bg, card, ink, muted, rule = (
        ('#14171c', '#1b1f26', '#eef1f6', '#a2abb9', '#353c47') if dark else
        ('#ffffff', '#ffffff', '#272b33', '#727b89', '#e2e6ec')
    )
    theme = 'Dark' if dark else 'White'
    total = len(data['icons'])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}" color="{ink}" font-family="Helvetica, Arial, sans-serif">',
             f'<title>LuciaOS Rounded — all {total} icons on {theme.lower()}</title>',
             '<desc>Complete icon library, grouped by common controls, graphics, 3D, and code. Each icon is labelled by name and category.</desc>',
             f'<rect width="{WIDTH}" height="{height}" fill="{bg}"/>',
             text(MARGIN, 44, 'LUCIAOS / ASSET LIBRARY', 12, muted, 600),
             text(MARGIN, 94, 'Rounded icon library', 40, ink, 600),
             text(MARGIN, 127, f'{total} icons · 24 × 24 canvas · 2 px base stroke · CurrentColor · Shown at 48 px', 15, muted),
             text(WIDTH - MARGIN, 44, f'{theme.upper()} / COMPLETE SET', 12, muted, 600, 'end')]
    for collection, icons, top in sections:
        parts += [text(MARGIN, top + 26, collection['name'], 24, ink, 600),
                  text(MARGIN, top + 50, collection['description'], 13, muted),
                  text(WIDTH - MARGIN, top + 26, f'{len(icons)} ICONS', 12, muted, 600, 'end')]
        for index, item in enumerate(icons):
            x = MARGIN + index % COLUMNS * (TILE_WIDTH + GAP)
            y = top + 72 + index // COLUMNS * ROW_HEIGHT
            cx = x + TILE_WIDTH / 2
            parts += [f'<rect x="{x}" y="{y}" width="{TILE_WIDTH}" height="112" rx="10" fill="{card}" stroke="{rule}"/>',
                      display_svg(sources[item['id']], item['id'], cx - 24, y + 13),
                      text(cx, y + 83, item['name'], 11.5, ink, 500, 'middle'),
                      text(cx, y + 101, item['category'], 10, muted, 400, 'middle')]
    parts += [f'<path d="M{MARGIN} {height-51}h{WIDTH-2*MARGIN}" stroke="{rule}"/>',
              text(MARGIN, height - 24, f'All {total} icons · Editable SVG paths · Browse and search in rounded/catalog.html', 12, muted),
              text(WIDTH - MARGIN, height - 24, 'Dy Mokomi / CC BY 4.0', 12, muted, 400, 'end'), '</svg>']
    return '\n'.join(parts) + '\n', height


def main():
    data = json.loads((ROOT / 'catalog.json').read_text())
    icons = data['icons']
    ids = [item['id'] for item in icons]
    if len(ids) != len(set(ids)):
        raise ValueError('Icon IDs must be unique.')
    collection_ids = {collection['id'] for collection in data['collections']}
    sources = {}
    for item in icons:
        if item['domain'] not in collection_ids:
            raise ValueError(f'Unknown collection for {item["id"]}.')
        path = (ROOT / item['file']).resolve()
        if not path.is_relative_to(ROOT / 'icons') or not path.is_file():
            raise ValueError(f'Missing icon or invalid file path: {item["file"]}')
        source = path.read_text()
        svg = ET.fromstring(source)
        if svg.get('viewBox') != '0 0 24 24':
            raise ValueError(f'Unexpected canvas for {item["id"]}.')
        sources[item['id']] = source
    listed = {(ROOT / item['file']).resolve() for item in icons}
    actual = {path.resolve() for path in (ROOT / 'icons').rglob('*.svg')}
    if listed != actual:
        raise ValueError('catalog.json must list each SVG in icons/ exactly once.')

    symbols = ['<svg xmlns="http://www.w3.org/2000/svg">']
    for item in icons:
        source = sources[item['id']]
        svg = ET.fromstring(source)
        attrs = ' '.join(f'{key}="{escape(value, quote=True)}"' for key, value in svg.attrib.items() if key not in ('width', 'height'))
        body = source[source.index('>') + 1:source.rindex('</svg>')].strip()
        symbols.append(f'<symbol id="{item["id"]}" {attrs}>\n{body}\n</symbol>')
    symbols.append('</svg>')
    (ROOT / 'sprite.svg').write_text('\n'.join(symbols) + '\n')

    previews = ROOT / 'previews'
    previews.mkdir(exist_ok=True)
    pages = []
    for theme in ('white', 'dark'):
        sheet, height = complete_sheet(data, sources, theme == 'dark')
        relative = f'previews/all-{theme}.svg'
        (ROOT / relative).write_text(sheet)
        pages.append(dict(theme=theme, file=relative, count=len(icons), width=WIDTH, height=height))
    (ROOT / 'preview-index.json').write_text(json.dumps(pages, indent=2) + '\n')

    template = (ROOT / 'scripts/catalog_template.html').read_text()
    embedded = dict(data, icons=[dict(item, svg=sources[item['id']]) for item in icons])
    (ROOT / 'catalog.html').write_text(template.replace('__ICON_DATA__', json.dumps(embedded, ensure_ascii=False).replace('<', '\\u003c')))
    index = ['# Rounded icon index', '', f'{len(icons)} icons. Paths are relative to this directory; filenames and sprite IDs are stable.', '']
    for collection in data['collections']:
        items = [item for item in icons if item['domain'] == collection['id']]
        index += [f'## {collection["name"]} — {len(items)}', '', '| Icon | SVG file | Theme |', '| --- | --- | --- |']
        index += [f'| {item["name"]} | [{item["id"]}.svg]({item["file"]}) | {item["category"]} |' for item in items]
        index.append('')
    (ROOT / 'ICONS.md').write_text('\n'.join(index) + '\n')
    print(f'Built {len(icons)} symbols, catalog and index, and 2 complete preview sheets ({WIDTH} × {pages[0]["height"]}).')


if __name__ == '__main__':
    main()
