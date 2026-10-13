# LuciaOS Rounded

258 editable icons for shared controls, graphics, 3D, code and mail applications.

## Organization

```text
rounded/
  icons/
    common/      actions, files, layout, view, navigation, playback, interface
    graphics/    painting, color, effects, selection, paths, layers, transform, typography
    3d/          primitives, selection, modeling, sculpting, viewport, shading,
                 scene, transform, modifiers, animation, nodes, cad, surfacing
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
| Common | 59 | Save, Undo, Zoom, Lock, Alignment, Arrows, Playback |
| Graphics | 46 | Brush, Pen, Magic Wand, Layers, Color, Transform |
| 3D | 110 | Cube, Extrude, Sculpt, Material, Lights, Keyframes, Nodes |
| Code | 29 | Terminal, Braces, Debugging, Git, Extensions |
| Mail | 14 | Compose, Reply, Inbox, Archive, Attachment |

## Preview and browse

- **Every icon on white:** [PNG](previews/all-white.png) · [SVG](previews/all-white.svg)
- **Every icon on dark:** [PNG](previews/all-dark.png) · [SVG](previews/all-dark.svg)
- [Offline catalog](catalog.html): search by name, keyword, or path; filter by collection and theme; copy source or download an icon.
- [Full icon index](ICONS.md)

Both sheets contain all 258 icons once, grouped by collection. Icons are shown
at 48 px on a 1600 × 4912 canvas. The white sheet uses a pure white background.

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
Timeline playback uses the separate `play` icon ID, paired with `play-backwards`.

Open shares its artwork with Open folder; Folder shares its artwork with
Group. Each has its own stable ID for application-specific control labels.

## Editor control mapping

Paths below are relative to `icons/`. Reuse the existing shared icons for Play,
Pause, Search, Frame nodes, Go up one level, Show all, and Hide.

| Editor action | Icon |
| --- | --- |
| Go to start | `common/playback/go-to-start.svg` |
| Step back one frame | `common/playback/step-back.svg` |
| Play backwards | `common/playback/play-backwards.svg` |
| Play | `common/playback/play.svg` |
| Pause | `common/playback/pause.svg` |
| Step forward one frame | `common/playback/step-forward.svg` |
| Go to end | `common/playback/go-to-end.svg` |
| Loop / repeat playback | `common/playback/repeat.svg` |
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
  Existing selection dots and Stop indicators retain their solid fills.
- **Source:** native SVG paths and shapes; no fonts or embedded raster images.
- **Sizing:** 24 px is the preferred toolbar size. Fine details become less
  distinct at 16 px.

### 3D fidelity and shading

These rules extend the canvas, `currentColor`, round caps and joins, and
transparent background conventions. `3d/selection/vertex-select`, `edge-select`,
and `face-select` are the unchanged references. One ink is used throughout;
value comes only from opacity, in either theme and at 35% disabled alpha.

#### Four value tiers, no more

| Tier | Use | How |
| --- | --- | --- |
| **Subject** | The element created or acted on: new loop, fillet face, bold curve | 2 px stroke (selected edges 2.5–3.25 px), opacity 1. Face fill .35–.45; use .45 beside a .2–.3 face of the same body. |
| **Shaded surface** | Body faces giving volume; new geometry's side walls | Fill .2–.3 with a 1.5 px solid stroke, or no stroke. |
| **Context** | The cube, grid, mesh or base surface | 1.25 px, `stroke-dasharray="1.6 2.2"`, opacity .75. Continuous curves where dashes break the shape: 1.25 px solid at .6. |
| **Ghost / before** | Old face position, removed region, old curve | 1.25 px dashed at .45, no fill (or fill .12 when removal must read as an area). |

- Never use more than one fill tier on the same face. Adjacent solid faces step
  their values: top .2, front .45, side .3. The lit top stays lightest, as in
  Fusion's two-tone shading.
- Fills sit under strokes: put the fill path first, then the stroke path.
- Do not use opacity below .35 on strokes. At 35% disabled alpha a .35 stroke
  drops to about 12% and disappears; that is acceptable only for ghosts.
- Semi-opaque fills darken when they overlap. Avoid overlap unless it conveys
  the operation (Intersect, Combine).

#### Geometry

- **Cubes:** selection cube top `(12,3.5)`, sides `(4,8)` and `(20,8)`, front
  junction `(12,12.5)`, bottom `(12,20.5)`: isometric, 30-degree rise, no
  vanishing point. Badge and two-body cubes scale about their center by .6 or .5.
- **Planar perspective faces:** `(3,15) (12,19.5) (21,15) (12,10.5)`, or a scaled
  form, so surfaces and sketch planes share an angle.
- **Curved patches:** four sides, top and bottom gentle S or C curves (about
  2.5 px control offset). Add 1–2 isolines at 1 px, opacity .5.
- **Curves:** smooth cubic paths at 2 px. Control vertices are hollow 2.5 × 2.5 px
  squares at 1.25 px. Edit and picked points are solid radius-1.5 dots; radius 3
  is reserved for a vertex subject, as in Vertex Select.
- **Arrows:** compact chevron, 4 px across, 2 px deep, on a 2 px shaft. One per
  icon, two at most; a double-headed slide counts as one. Revolve and Spin use
  arcs with the chevron tangent to the arc.
- **Badges (+, −, x, check):** bottom-right 7 × 7 px only, 2 px stroke, 1 px
  clear gap from art. They mark mode (Insert Knot, Remove Knot, Delete Face),
  never replace the picture.
- **Optical size:** content box 3–21 px; keep at least 1.5 px between parallel
  strokes. Use at most about 8 strokes. At 16 px the subject must read even
  when every context line vanishes.

#### How to show change

- **New geometry:** subject tier; face fill .45. Never dashed.
- **Moved geometry:** old position ghost, new position subject, one arrow
  between them (Offset Face, Edge Slide, Stretch).
- **Removed geometry:** ghost; add an x badge only when removal is the point
  (Delete Face, Remove Knot).
- **Before / after side by side:** conversions only (Trim Convert, Tessellate,
  Curve to Mesh). Small left glyph at .6, 4 px arrow, right glyph at full opacity.
- **Inputs:** sketch profile, rail and boundary curves use subject strokes, no
  fill. Their surface or body result takes the shaded tier.

#### Consistency

- Sketches are flat: reference lines 1.25 px, new entities 2 px, clicked points
  solid dots (the equivalent of Fusion's blue squares).
- Constraints are flat: constrained entity 2 px, reference 1.25 px at .6, with
  a small relation glyph (square corner, equals sign, triangle).
- Share family bases: select rules use a 3 × 3 grid or the selection cube;
  surfacing the same curved patch; curves the same S-curve; node kinds the
  rounded box from `3d/nodes`.
- Every new filename must have a library-wide unique stem: luce-ui embeds by
  stem, regardless of folder.
- Tool-specific drawings may specify extra normal arrows or analysis fill
  values (for example .15 density and .6 selected centers); those explicit
  exceptions do not change the four default tiers.

#### Five worked examples

1. **Fillet (`3d/cad`):** selection cube context, omitting `M12 12.5v8`.
   Replace that edge with a quarter-round strip whose boundaries lie 2.5 px
   either side, 2 px solid, fill .45. A thin 1 px / .5 curved middle isoline
   and a dashed radius-2.5 rolling ball show roundness. It must read at 16 px
   and differ from Chamfer (one flat strip, no isoline or ball) and Bevel
   (2–3 segment lines across the strip).
2. **Offset Face (`3d/cad`, Fusion Press Pull):** whole dashed cube, top lifted
   by 4 px. Original diamond ghost .45; new diamond fill .45, 2 px outline.
   Connecting walls fill .2 with 1.25 px solid edges. One upward arrow leaves
   the cap, ending near y=1.5. Extrude instead starts with a single face.
3. **Skin (`3d/surfacing`):** three bold gentle-C sections, the middle larger,
   arranged diagonally back to front. Two 1.25 px boundaries join their ends;
   lofted region fill .25. No arrows. Input curves are subject; result shaded.
4. **Select Loop (`3d/selection`):** unchanged selection cube context. The
   visible closed edge loop is `M4 12l8 4.5 8-4.5`, 3 px, with 3 px dots where
   it crosses visible edges. No plus. Loop Cut's new line gains a 2 px plus
   badge bottom-right, separating adding from picking.
5. **Constraint Tangent (`3d/sketch`):** flat circle centered `(10,14)`, radius
   6, 1.25 px at .6. A bold line touches it at the upper-right at 45 degrees
   (approximately `(6,4)` to `(21,15)`); a 3 px solid dot marks tangency. The
   line is subject, the circle reference.


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

For visual review, render every changed or new SVG with `resvg` at 16, 24 and
96 px: light ink on `#262626` and dark ink on `#ffffff`, enabled and at 35%
opacity. Inspect the family together at 16, 24 and 48 px. Set `color` only on the temporary review copy or wrapper so
the source SVG continues to inherit `currentColor` and stays transparent.

The offline catalog falls back to selecting the SVG source for manual copying
if clipboard access is unavailable. Individual downloads work offline.

## License

Icons by Dy Mokomi. See the repository's [CC BY 4.0 license](../LICENSE) and
[attribution guidance](../README.md#license).
