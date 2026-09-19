# LuciaOS Rounded

157 editable icons for shared controls, graphics, 3D, and code applications.

## Organization

```text
rounded/
  icons/
    common/      actions, files, layout, view, playback, interface
    graphics/    painting, color, effects, selection, paths, layers, transform, typography
    3d/          primitives, selection, modeling, sculpting, viewport, shading,
                 scene, transform, modifiers, animation
    code/        files, editing, search, debugging, version-control, workspace
  previews/
    all-white.svg / all-white.png
    all-dark.svg  / all-dark.png
  catalog.json
  catalog.html
  sprite.svg
  ICONS.md
  path-migrations.json
  scripts/
```

| Collection | Count | Examples |
| --- | ---: | --- |
| Common | 45 | Save, Undo, Zoom, Lock, Alignment, Playback |
| Graphics | 43 | Brush, Pen, Magic Wand, Layers, Color, Transform |
| 3D | 40 | Cube, Extrude, Sculpt, Material, Lights, Keyframes |
| Code | 29 | Terminal, Braces, Debugging, Git, Extensions |

## Preview and browse

- **Every icon on white:** [PNG](previews/all-white.png) · [SVG](previews/all-white.svg)
- **Every icon on dark:** [PNG](previews/all-dark.png) · [SVG](previews/all-dark.svg)
- [Offline catalog](catalog.html): search by name, keyword, or path; filter by collection and theme; copy source or download an icon.
- [Full icon index](ICONS.md)

Both sheets contain all 157 icons once, grouped by collection. Icons are shown
at 48 px on a 1600 × 3204 canvas. The white sheet uses a pure white background.

## Application controls

- **Files and windows:** Open, Close, Folder, New folder, and New file.

- **Split window horizontally:** stacked top/bottom panes, with a horizontal divider.
- **Split window vertically:** side-by-side panes, with a vertical divider.
- **Snap to grid:** the Grid frame with dots at its four interior intersections.
- **Development:** Terminal, Build, Bug, Start / Run, Stop, Pause, and Reload.
- **2D editing:** Corner pin, Crop, Reflection, Clone stamp, Brush, and Pencil.

Reflection depicts a screen with a sharp 45-degree glare. `reload` is a plain
refresh arrow; the existing `restart` icon retains its playback cue. Start
uses the stable `run` icon ID, with the catalog label **Start / Run**.

Open shares its artwork with Open folder; Folder shares its artwork with
Group. Each has its own stable ID for application-specific control labels.

## Design

- **Canvas:** 24 × 24; transparent backgrounds.
- **Base stroke:** 2 px, rounded ends and joins, softer corners.
- **Directional arrowheads:** the compact rounded chevron used by Restart,
  4 px across and 2 px deep on the 24 px canvas, rotated to follow the shaft.
- **Color:** `currentColor`. Selected faces use a translucent fill, playback
  controls use solid indicators, and Edge selection uses a heavier line.
- **Source:** native SVG paths and shapes; no fonts or embedded raster images.
- **Sizing:** 24 px is the preferred toolbar size. Fine details become less
  distinct at 16 px.

## Use an individual file

Use the `file` property in [catalog.json](catalog.json), relative to `rounded/`:

```text
icons/common/files/save.svg
icons/graphics/selection/magic-wand-tool.svg
icons/3d/primitives/cube.svg
icons/code/version-control/git-branch.svg
```

Inline an SVG to inherit the surrounding CSS `color`. An SVG loaded through
`<img>` does not inherit the page's color; use inline SVG, the sprite, or a CSS
mask for theme-aware color.

## Use the sprite

Sprite IDs are unchanged by the folder reorganization:

```html
<button type="button" aria-label="Extrude selected faces">
  <svg width="24" height="24" aria-hidden="true" focusable="false">
    <use href="/assets/rounded/sprite.svg#extrude"></use>
  </svg>
</button>
```

Adjust the URL to where the sprite is served. Keep external sprite references
on the same origin. For a self-contained page, insert the sprite markup with
`style="display: none"` on its outer SVG and reference `href="#extrude"`.

Put accessible names on icon-only buttons and mark decorative SVGs with
`aria-hidden="true"`. A standalone meaningful SVG can use `role="img"` and an
appropriate `aria-label`. Icons do not contain fixed IDs or titles.

## Existing imports

Version 2 organizes the flat source folder into collection/theme subfolders.
Use [path-migrations.json](path-migrations.json) to update direct file imports.
For example, `icons/cube.svg` is now `icons/3d/primitives/cube.svg`. The artwork,
filenames, and sprite IDs are unchanged.

`align-vertical-center` aligns center Y positions around a horizontal guide.
`align-horizontal-center` aligns center X positions around a vertical guide.

## Add or edit icons

1. Place the SVG in `icons/<collection>/<theme>/`.
2. Add or update its entry in `catalog.json`, including its unique `id`, name,
   domain, category, category ID, relative file path, and search keywords.
3. Run the builders from the repository root:

```sh
python3 rounded/scripts/build_previews.py
python3 rounded/scripts/render_previews.py
```

The first command requires Python 3.9+ and uses only its standard library.
It validates the icon inventory and regenerates the sprite, HTML catalog,
Markdown index, full SVG sheets, and preview index. New icons are included in
both full sheets automatically. Edit `scripts/catalog_template.html` to change
the catalog UI; `catalog.html` is generated.

The second command exports PNGs using macOS Quick Look and `sips`; no Python
packages are required. The SVG sheets work on other platforms as well. PNGs
are generated snapshots and should be refreshed after editing.

The offline catalog falls back to selecting the SVG source for manual copying
if clipboard access is unavailable. Individual downloads work offline.

## License

Icons by Dy Mokomi. See the repository's [CC BY 4.0 license](../LICENSE) and
[attribution guidance](../README.md#license).
