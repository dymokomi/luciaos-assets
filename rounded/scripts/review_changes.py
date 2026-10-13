#!/usr/bin/env python3
"""Render changed SVGs and paired contact sheets with resvg (no Python deps)."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html import escape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
THEMES = [('light', '#ffffff', '#262626'), ('dark', '#262626', '#eeeeee')]
SIZES = (16, 24, 48, 96)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)


def placed(source, x, y, size):
    return source.replace('<svg ', f'<svg x="{x}" y="{y}" ', 1).replace(
        'width="24" height="24"', f'width="{size}" height="{size}"', 1)


def render(pair):
    source, output = pair
    subprocess.run(['resvg', '--skip-system-fonts', str(source), str(output)],
                   check=True, capture_output=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--before-ref', required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--sheet-prefix', type=Path, required=True)
    parser.add_argument('--names', type=Path, help='Optional ordered list of changed stems')
    args = parser.parse_args()
    changed = [Path(p) for p in git('diff', '--name-only', args.before_ref, '--',
                                   'rounded/icons').splitlines() if p.endswith('.svg')]
    if not changed:
        parser.error('No changed icons relative to --before-ref')
    if args.names:
        names = args.names.read_text().split()
        by_name = {p.stem: p for p in changed}
        if len(names) != len(changed) or set(names) != set(by_name):
            parser.error('--names must contain exactly the changed icons, once each')
        changed = [by_name[n] for n in names]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.sheet_prefix.parent.mkdir(parents=True, exist_ok=True)
    (args.output_dir / 'manifest.txt').write_text('\n'.join(map(str, changed)) + '\n')
    for version in ('before', 'after'):
        sources = {p.stem: git('show', f'{args.before_ref}:{p}') if version == 'before'
                   else (ROOT / p).read_text() for p in changed}
        jobs = []
        for name, source in sources.items():
            folder = args.output_dir / version / name
            folder.mkdir(parents=True, exist_ok=True)
            for theme, bg, ink in THEMES:
                for alpha in (1, .35):
                    for size in SIZES:
                        target = folder / f'{theme}-{alpha:g}-{size}.svg'
                        target.write_text(
                            f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
                            f'viewBox="0 0 {size} {size}" color="{ink}">'
                            f'<rect width="{size}" height="{size}" fill="{bg}"/>'
                            f'<g opacity="{alpha}">{placed(source, 0, 0, size)}</g></svg>')
                        jobs.append((target, target.with_suffix('.png')))
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(render, jobs))
        width, header, row, label, block = 1104, 136, 72, 224, 220
        height = header + row * len(changed) + 24
        pieces = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
                  f'font-family="Helvetica, Arial, sans-serif">',
                  f'<rect width="{width}" height="{height}" fill="#eeeeee"/>']

        def text(x, y, value, size=13, ink='#262626'):
            pieces.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{ink}">{escape(value)}</text>')

        title = re.sub(r'(?<=\D)(?=\d)', ' ', args.sheet_prefix.name.replace('_', ' ')).title()
        text(20, 32, f'LuciaOS / {title} / {version.upper()}', 24)
        text(20, 56, f'{len(changed)} changed icons · native pixel sizes · resvg · baseline {args.before_ref}')
        text(20, 76, 'Color: currentColor · overall disabled alpha 35%')
        for group, (theme, bg, ink, alpha) in enumerate([
                (*THEMES[0], 1), (*THEMES[1], 1), (*THEMES[0], .35), (*THEMES[1], .35)]):
            x = label + group * block
            pieces.append(f'<rect x="{x}" y="88" width="{block}" height="{height-88}" fill="{bg}"/>')
            text(x + 12, 107, f'{theme.title()} / {int(alpha*100)}%', 13, ink)
            for center, size in zip((40, 104, 172), (16, 24, 48)):
                text(x + center - 8, 126, str(size), 11, ink)
            for i, path in enumerate(changed):
                y = header + row * i
                if group == 0:
                    text(14, y + 32, path.stem, 12)
                    text(14, y + 49, path.parent.name, 10, '#666666')
                pieces.append(f'<path d="M{x} {y+row}h{block}" stroke="{ink}" opacity=".1"/>')
                for center, size in zip((40, 104, 172), (16, 24, 48)):
                    pieces.append(f'<g color="{ink}" opacity="{alpha}">' +
                                  placed(sources[path.stem], x + center - size/2,
                                         y + (row-size)/2, size) + '</g>')
        pieces.append('</svg>')
        sheet = args.output_dir / f'{args.sheet_prefix.name}_{version}.svg'
        sheet.write_text('\n'.join(pieces) + '\n')
        png = Path(f'{args.sheet_prefix}_{version}.png')
        subprocess.run(['resvg', str(sheet), str(png)], check=True)
        print(f'{version}: {len(jobs)} individual resvg renders; {png}')


if __name__ == '__main__':
    main()
