#!/usr/bin/env python3
"""Review Kinogaki group icons and selection neighbors at native sizes with resvg."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html import escape
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

from review_changes import placed, render, THEMES, SIZES

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--render-dir', type=Path, required=True)
    parser.add_argument('--subject-only', action='store_true',
                        help='Hide context and ghost strokes for readability review')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'catalog.json').read_text())['icons']
    names = ('group-create', 'group-expression', 'group-combine',
             'group-promote', 'group-delete', 'group-rename')
    groups = [next(item for item in catalog if item['id'] == name) for name in names]
    references = [next(item for item in catalog if item['id'] == name)
                  for name in ('select-grow', 'select-convert', 'face-select')]
    icons = groups + references
    sources = {item['id']: (ROOT / item['file']).read_text() for item in icons}
    if args.subject_only:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        for name, source in sources.items():
            svg = ET.fromstring(source)
            for parent in svg.iter():
                for child in list(parent):
                    if float(child.get('opacity', '1')) < 1:
                        parent.remove(child)
            sources[name] = ET.tostring(svg, encoding='unicode')
    args.render_dir.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    jobs = []
    for item in icons:
        folder = args.render_dir / item['id']
        folder.mkdir(exist_ok=True)
        for theme, bg, ink in THEMES:
            for alpha in (1, .35):
                for size in SIZES:
                    svg = folder / f'{theme}-{alpha:g}-{size}.svg'
                    svg.write_text(
                        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">'
                        f'<rect width="{size}" height="{size}" fill="{bg}"/>'
                        f'<g color="{ink}" opacity="{alpha}">'
                        f'{placed(sources[item["id"]], 0, 0, size)}</g></svg>')
                    jobs.append((svg, svg.with_suffix('.png')))
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(render, jobs))

    width, label, block, header, row = 1104, 224, 220, 136, 72
    height = header + len(icons) * row + 24
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             'font-family="Helvetica, Arial, sans-serif">',
             f'<rect width="{width}" height="{height}" fill="#eeeeee"/>']

    def text(x, y, value, size=13, ink='#262626'):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" '
                     f'fill="{ink}">{escape(value)}</text>')

    text(20, 32, 'LuciaOS / Kinogaki Studio group nodes', 24)
    text(20, 56, '6 group icons + select-grow, select-convert, face-select · native pixel sizes · resvg')
    text(20, 76, 'Subject only: context and ghost strokes hidden' if args.subject_only else
         'One currentColor ink · 2 px base stroke · disabled alpha applied to the whole icon')
    for i, item in enumerate(icons):
        y = header + i * row
        text(14, y + 32, item['id'], 12)
        text(14, y + 49, f'{item["domain"]}/{item["categoryId"]}', 10, '#666666')
    for group, (theme, bg, ink, alpha) in enumerate([
            (*THEMES[0], 1), (*THEMES[1], 1), (*THEMES[0], .35), (*THEMES[1], .35)]):
        x = label + group * block
        parts.append(f'<rect x="{x}" y="88" width="{block}" height="{height-88}" fill="{bg}"/>')
        text(x + 12, 107, f'{theme.title()} / {int(alpha*100)}%', 13, ink)
        for center, size in zip((40, 104, 172), (16, 24, 48)):
            text(x + center - 8, 126, str(size), 11, ink)
        for i, item in enumerate(icons):
            y = header + i * row
            parts.append(f'<path d="M{x} {y+row}h{block}" stroke="{ink}" opacity=".1"/>')
            for center, size in zip((40, 104, 172), (16, 24, 48)):
                parts.append(f'<g color="{ink}" opacity="{alpha}">' +
                             placed(sources[item['id']], x + center - size/2,
                                    y + (row-size)/2, size) + '</g>')
    parts.append('</svg>')
    sheet = args.output.with_suffix('.svg')
    sheet.write_text('\n'.join(parts) + '\n')
    subprocess.run(['resvg', str(sheet), str(args.output)], check=True)
    print(f'Wrote {args.output} ({width} × {height}); {len(jobs)} individual renders at 16/24/48/96 px.')


if __name__ == '__main__':
    main()
