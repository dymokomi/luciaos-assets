# LuciaOS Rounded

201 editable icons for shared controls, graphics, 3D, code and mail applications.

## Organization

```text
rounded/
  icons/
    common/      actions, files, layout, view, navigation, playback, interface
    graphics/    painting, color, effects, selection, paths, layers, transform, typography
    3d/          primitives, selection, modeling, sculpting, viewport, shading,
                 scene, transform, modifiers, animation, nodes
    code/        files, editing, search, debugging, version-control, workspace
    mail/        messages
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
| Common | 58 | Save, Undo, Zoom, Lock, Alignment, Arrows, Playback |
| Graphics | 46 | Brush, Pen, Magic Wand, Layers, Color, Transform |
| 3D | 54 | Cube, Extrude, Sculpt, Material, Lights, Keyframes, Nodes |
| Code | 29 | Terminal, Braces, Debugging, Git, Extensions |
| Mail | 14 | Compose, Reply, Inbox, Archive, Attachment |

## Preview and browse

- **Every icon on white:** [PNG](previews/all-white.png) · [SVG](previews/all-white.svg)
- **Every icon on dark:** [PNG](previews/all-dark.png) · [SVG](previews/all-dark.svg)
- [Offline catalog](catalog.html): search by name, keyword, or path; filter by collection and theme; copy source or download an icon.
- [Full icon index](ICONS.md)

Both sheets contain all 201 icons once, grouped by collection. Icons are shown
at 48 px on a 1600 × 4044 canvas. The white sheet uses a pure white background.

## Application controls

- **Files and windows:** Open, Close, Folder, New folder, and New file.
- **Navigation:** Arrow left, right, up and down: a straight shaft with the
  directional arrowhead, for Back, Forward and Up (a browser's history, a
  file list's parent folder). Undo and Redo keep their curved history cue.

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

## Editor control mapping

Paths below are relative to `icons/`. Reuse the existing shared icons for Play,
Pause, Search, Frame nodes, Go up one level, Show all, and Hide.

| Editor action | Icon |
| --- | --- |
| Go to start | `common/playback/go-to-start.svg` |
| Step back one frame | `common/playback/step-back.svg` |
| Play | `common/playback/run.svg` |
| Pause | `common/playback/pause.svg` |
| Step forward one frame | `common/playback/step-forward.svg` |
| Go to end | `common/playback/go-to-end.svg` |
| Loop / repeat playback | `common/playback/repeat.svg` |
| Play backwards | `common/playback/play-backwards.svg` |
| Add node | `3d/nodes/add-node.svg` |
| Group nodes / collapse into a subnetwork | `3d/nodes/group-nodes.svg` |
| Frame nodes / fit all nodes in view | `3d/viewport/frame-selection.svg` |
| Go up one level / parent network | `common/navigation/arrow-up.svg` |
| Subnetwork output node | `3d/nodes/output-node.svg` |
| Outliner search | `common/interface/search.svg` |
| Outliner filter | `common/interface/filter.svg` |
| Show all objects outside the current network | `common/view/visible.svg` |
| Show outside objects greyed / ghosted | `common/view/ghosted.svg` |
| Hide outside objects / show none | `common/view/hidden.svg` |
| Project settings | `common/files/project-settings.svg` |

The visibility set uses an eye: solid outline, thin dashed outline, or a slash.
Project settings combines a document and gear; app-wide settings keeps the
standalone `common/interface/settings.svg` gear. Frame stepping puts the bar
behind the triangle, while jumping to an endpoint puts it ahead of the triangle.

## Design

- **Canvas:** 24 × 24; transparent backgrounds.
- **Base stroke:** 2 px, rounded ends and joins, softer corners.
- **Directional arrowheads:** the compact rounded chevron used by Restart,
  4 px across and 2 px deep on the 24 px canvas, rotated to follow the shaft.
- **Color:** `currentColor`. New filled regions use soft fills (opacity .18–.45).
  Existing selection dots and Pause / Stop indicators retain their solid fills.
- **3D context:** follow `selection/vertex-select`, `edge-select`, and `face-select`:
  context uses a 1.25 px stroke, `1.6 2.2` dashes, and .75 opacity; the active
  subject uses the 2 px base stroke, with heavier lines for selected edges.
  Continuous supporting curves use 1.25 px strokes when dashes would obscure
  the shape. Keep internal mesh detail sparse at toolbar sizes.
- **Cube geometry:** reuse the selection cube: top `(12, 3.5)`, side corners
  `(4, 8)` and `(20, 8)`, front junction `(12, 12.5)`, and bottom `(12, 20.5)`.
  Modeling icons emphasize the affected edge, face, or operation. Planar mesh
  operations share a rounded 16 × 16 boundary from `(4, 4)` to `(20, 20)`.
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
For example, `icons/cube.svg` is now `icons/3d/primitives/cube.svg`. Existing
filenames and sprite IDs stay stable when artwork is revised.

`align-vertical-center` aligns center Y positions around a horizontal guide.
`align-horizontal-center` aligns center X positions around a vertical guide.

## Add or edit icons

1. Place the SVG in `icons/<collection>/<theme>/`.
2. Add or update its entry in `catalog.json`, including its unique `id`, name,
   domain, category, category ID, relative file path, and search keywords.
3. Run the builders from the repository root:

```sh
python3 rounded/scripts/build_previews.py
resvg rounded/previews/all-white.svg rounded/previews/all-white.png
resvg rounded/previews/all-dark.svg rounded/previews/all-dark.png
```

The first command requires Python 3.9+ and uses only its standard library.
It validates the icon inventory and regenerates the sprite, HTML catalog,
Markdown index, full SVG sheets, and preview index. New icons are included in
both full sheets automatically. Edit `scripts/catalog_template.html` to change
the catalog UI; `catalog.html` is generated.

The `resvg` commands export PNGs. On macOS, `python3 rounded/scripts/render_previews.py`
is an alternative using Quick Look and `sips`. PNGs are generated snapshots
and should be refreshed after editing.

For visual review, render each changed SVG with `resvg` at 24 px and 96 px,
using light ink on `#262626`; inspect both sizes and check the whole family at
24 px and 48 px. Set `color` only on the temporary review copy or wrapper so
the source SVG continues to inherit `currentColor` and stays transparent.

The offline catalog falls back to selecting the SVG source for manual copying
if clipboard access is unavailable. Individual downloads work offline.

## License

Icons by Dy Mokomi. See the repository's [CC BY 4.0 license](../LICENSE) and
[attribution guidance](../README.md#license).
