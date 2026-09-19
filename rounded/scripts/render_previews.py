#!/usr/bin/env python3
"""Export the full SVG sheets to PNG with macOS Quick Look and sips."""
import json
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    if not shutil.which('qlmanage') or not shutil.which('sips'):
        raise SystemExit('PNG export requires macOS Quick Look and sips. The SVG sheets work on every platform.')
    pages = json.loads((ROOT / 'preview-index.json').read_text())
    with tempfile.TemporaryDirectory(prefix='luciaos-preview-') as temp:
        folder = Path(temp)
        for page in pages:
            source = ROOT / page['file']
            width, height = page['width'], page['height']
            side = max(width, height)
            wrapper = folder / source.name
            # Quick Look can crop rectangular SVGs; a square wrapper preserves scale.
            centered = source.read_text().replace('<svg ', f'<svg x="{(side-width)//2}" y="{(side-height)//2}" ', 1)
            wrapper.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{side}" height="{side}" viewBox="0 0 {side} {side}">' + centered + '</svg>')
            subprocess.run(['qlmanage', '-t', '-s', str(side), '-o', str(folder), str(wrapper)], check=True, capture_output=True)
            thumbnail = folder / (wrapper.name + '.png')
            if struct.unpack('>II', thumbnail.read_bytes()[16:24]) != (side, side):
                raise RuntimeError('Quick Look produced an unexpected thumbnail size.')
            target = source.with_suffix('.png')
            subprocess.run(['sips', '--cropToHeightWidth', str(height), str(width), str(thumbnail), '--out', str(target)], check=True, capture_output=True)
            if struct.unpack('>II', target.read_bytes()[16:24]) != (width, height):
                raise RuntimeError('PNG output has unexpected dimensions.')
            print(f'Wrote {target.relative_to(ROOT)} ({width} × {height}).')


if __name__ == '__main__':
    main()
