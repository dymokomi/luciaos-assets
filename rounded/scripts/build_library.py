#!/usr/bin/env python3
"""Rebuild the rounded sprite, catalog, and SVG previews using only Python 3."""
import json
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = '{http://www.w3.org/2000/svg}'


def text(x, y, value, size=12, color='#747a86', weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'


def display_svg(source, x, y, size):
    return source.replace('<svg ', f'<svg x="{x}" y="{y}" ', 1).replace('width="24" height="24"', f'width="{size}" height="{size}"', 1)


def sheet(icons, sources, title, subtitle, footer, dark=False):
    bg, card, ink, muted, rule = ('#181a1e', '#21242a', '#f0f1f3', '#989da8', '#343840') if dark else ('#f4f5f7', '#ffffff', '#252931', '#747a86', '#e0e3e8')
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="892" viewBox="0 0 1200 892" color="{ink}" font-family="Helvetica, Arial, sans-serif">',
             f'<title>{escape(title)} — {escape(subtitle)}</title>',
             f'<rect width="1200" height="892" fill="{bg}"/>',
             text(40, 42, 'GFX / ROUNDED LIBRARY', 11, muted, 600),
             text(40, 87, title, 34, ink, 600),
             text(40, 120, subtitle, 14, muted),
             text(1160, 42, 'DARK' if dark else 'LIGHT', 11, muted, 600, 'end')]
    for i, item in enumerate(icons):
        x, y = 40 + i % 6 * 189, 156 + i // 6 * 164
        parts += [f'<rect x="{x}" y="{y}" width="175" height="150" rx="12" fill="{card}" stroke="{rule}"/>',
                  display_svg(sources[item['id']], x + 63.5, y + 24, 48),
                  text(x + 87.5, y + 107, item['name'], 11.5, ink, 500, 'middle'),
                  text(x + 87.5, y + 129, item['category'], 10, muted, 400, 'middle')]
    parts += [f'<path d="M40 839h1120" stroke="{rule}"/>', text(40, 866, footer, 11, muted), text(1160, 866, '24 px / 2 px stroke', 11, muted, 400, 'end'), '</svg>']
    return '\n'.join(parts) + '\n'


def main():
    data = json.loads((ROOT / 'catalog.json').read_text())
    icons = data['icons']
    sources = {item['id']: (ROOT / item['file']).read_text() for item in icons}
    symbols = ['<svg xmlns="http://www.w3.org/2000/svg">']
    for item in icons:
        source = sources[item['id']]
        svg = ET.fromstring(source)
        attributes = ' '.join(f'{key}="{escape(value, quote=True)}"' for key, value in svg.attrib.items() if key not in ('width', 'height'))
        body = source[source.index('>') + 1:source.rindex('</svg>')].strip()
        symbols.append(f'<symbol id="{item["id"]}" {attributes}>\n{body}\n</symbol>')
    symbols.append('</svg>')
    (ROOT / 'sprite.svg').write_text('\n'.join(symbols) + '\n')

    featured = ['brush-tool', 'pen-tool', 'gradient-tool', 'magic-wand-tool', 'layer-mask', 'rotate-tool', 'pan-tool', 'color-swatch',
                'cube', 'sphere', 'extrude', 'bevel', 'sculpt-tool', 'camera', 'rig', 'keyframe',
                'terminal', 'file-code', 'bug', 'git-branch', 'pull-request', 'extensions', 'settings', 'command-palette']
    by_id = {item['id']: item for item in icons}
    samples = [by_id[key] for key in featured]
    for dark in (False, True):
        suffix = '-dark' if dark else ''
        (ROOT / f'preview{suffix}.svg').write_text(sheet(samples, sources, 'A toolkit for making things.', f'{len(icons)} SVG icons · Graphics, 3D, and code · 24 × 24 canvas · 2 px strokes', 'Selected icons at 48 px · Browse every icon in catalog.html', dark))

    previews = ROOT / 'previews'
    previews.mkdir(exist_ok=True)
    pages = []
    for domain, title in [('graphics', 'Graphics & shared controls'), ('3d', '3D tools'), ('code', 'Code editor')]:
        group = [item for item in icons if item['domain'] == domain]
        count = (len(group) + 23) // 24
        for start in range(0, len(group), 24):
            page = start // 24 + 1
            selected = group[start:start + 24]
            stem = f'{domain}-{page:02}'
            for dark in (False, True):
                suffix = '-dark' if dark else ''
                (previews / f'{stem}{suffix}.svg').write_text(sheet(selected, sources, title, f'{len(group)} icons · Page {page} of {count} · Rounded library', f'{start+1:02}–{start+len(selected):02} of {len(group)} · Shown at 48 px', dark))
            pages.append(dict(domain=domain, page=page, file=f'previews/{stem}.svg'))

    # Small-size contact sheets show one domain per sheet in light and dark.
    for domain in ('graphics', '3d', 'code'):
        group = [item for item in icons if item['domain'] == domain]
        rows = (len(group) + 22) // 23
        section_height = 66 + rows * 3 * 44
        total_height = section_height * 2
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{total_height}" viewBox="0 0 1200 {total_height}" font-family="Helvetica, Arial, sans-serif">', f'<title>{domain}: all icons at 16, 20, and 24 pixels, light and dark</title>']
        for theme in (0, 1):
            offset = theme * section_height
            bg, ink, muted = ('#181a1e', '#f0f1f3', '#989da8') if theme else ('#f4f5f7', '#252931', '#747a86')
            parts += [f'<rect y="{offset}" width="1200" height="{section_height}" fill="{bg}"/>', f'<g color="{ink}">', text(32, offset + 32, f'{domain.upper()} / ACTUAL SIZES / ' + ('DARK' if theme else 'LIGHT'), 11, muted, 600)]
            for batch in range(rows):
                for j, size in enumerate((16, 20, 24)):
                    cy = offset + 68 + (batch * 3 + j) * 44
                    parts.append(text(32, cy + 4, f'{size} px', 11, muted))
                    for i, item in enumerate(group[batch * 23:(batch + 1) * 23]):
                        parts.append(display_svg(sources[item['id']], 113 + i * 48 - size / 2, cy - size / 2, size))
            parts.append('</g>')
        parts.append('</svg>')
        (previews / f'{domain}-sizes.svg').write_text('\n'.join(parts) + '\n')

    # Preserve the familiar small-size entry point using the full graphics domain.
    (ROOT / 'toolbar-sizes.svg').write_text((previews / 'graphics-sizes.svg').read_text())
    template = (ROOT / 'scripts/catalog_template.html').read_text()
    embedded = dict(data, icons=[dict(item, svg=sources[item['id']]) for item in icons])
    (ROOT / 'catalog.html').write_text(template.replace('__ICON_DATA__', json.dumps(embedded, ensure_ascii=False).replace('<', '\\u003c')))
    (ROOT / 'preview-index.json').write_text(json.dumps(pages, indent=2) + '\n')
    print(f'Built {len(icons)} sprite symbols, searchable catalog, {len(pages)} preview pages in both themes, and size samples.')


if __name__ == '__main__':
    main()
