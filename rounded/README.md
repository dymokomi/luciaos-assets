# LuciaOS Rounded

424 editable icons for shared controls, graphics, 3D, code and mail applications.

## Organization

```text
rounded/
  icons/
    common/      actions, files, layout, view, navigation, playback, interface
    graphics/    painting, color, effects, selection, paths, layers, transform, typography
    3d/          primitives, selection, modeling, sculpting, viewport, shading,
                 scene, transform, modifiers, animation, nodes, cad, surfacing,
                 curves, sketch
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
| Common | 60 | Save, Undo, Zoom, Lock, Alignment, Arrows, Playback, Tool shelf |
| Graphics | 48 | Brush, Pen, Magic Wand, Layers, Color, Transform |
| 3D | 273 | Cube, Extrude, Sculpt, Material, Lights, Keyframes, Nodes |
| Code | 29 | Terminal, Braces, Debugging, Git, Extensions |
| Mail | 14 | Compose, Reply, Inbox, Archive, Attachment |

## Preview and browse

- **Every icon on white:** [PNG](previews/all-white.png) · [SVG](previews/all-white.svg)
- **Every icon on dark:** [PNG](previews/all-dark.png) · [SVG](previews/all-dark.svg)
- [Offline catalog](catalog.html): search by name, keyword, or path; filter by collection and theme; copy source or download an icon.
- [Full icon index](ICONS.md)

Both sheets contain all 424 icons once, grouped by collection. Icons are shown
at 48 px on a 1600 × 7516 canvas. The white sheet uses a pure white background.

## Application controls

- **Files and windows:** Open, Close, Folder, New folder, and New file.
- **Navigation:** Arrow left, right, up and down: a straight shaft with the
  directional arrowhead, for Back, Forward and Up (a browser's history, a
  file list's parent folder). Undo and Redo keep their curved history cue.

- **Split window horizontally:** stacked top/bottom panes, with a horizontal divider.
- **Split window vertically:** side-by-side panes, with a vertical divider.
- **Tool shelf:** a bottom-docked tool palette, with an active tab, two shaded
  tabs, and a 2 × 3 grid of tiles inside a rounded panel.
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
| Open the tabbed tool shelf | `common/interface/tool-shelf.svg` |
| Press Pull | `3d/cad/press-pull.svg` |
| Move/Copy | `graphics/transform/move-tool.svg` |

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
- **Sizing:** 24 px is the preferred toolbar size. The operation and differences
  between related tools must also read at 16 px; reserve fine detail for context.

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
- Essential contours belong to the subject, even when they describe supporting
  geometry. Use solid 1.5–2 px edges at full opacity for a necessary rail, rim,
  table or endpoint; keep the operation itself at 2–3 px. A dashed context line
  must never be the only cue separating two operations. The context and ghost
  tiers above stay unchanged: adding weight to every scaffold makes small icons
  busy. Verify the subject with those tiers hidden as well as at 35% overall alpha.
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
  never replace the picture. Attribute operations instead pair a two-row table
  with a large subject mark in the right half: plus, minus, up arrow, pencil or
  text glyph. Name uses a path-drawn A, distinct from Promote's upward arrow.
  Finish Sketch's check is the operation itself and spans the plane.
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
  Curve to Mesh). Small left glyph at .6, 4 px arrow, larger right glyph at full
  opacity. Essential source contours may use full-opacity 2 px strokes when
  the source must distinguish related conversions at node size. The destination
  must read by itself. Set Curve Type instead overlays
  an angular ghost and a smooth curve, without the conversion layout.
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
- Prefer a magnified edge or face when a whole cube hides the operation.
  Fillet and Chamfer use broad curved and straight edge sections; Shell uses a
  deep, unobstructed opening, thick rim and short walls; Split Face uses one divided face.
  Extrude is a tall prism from one profile; Offset Face separates a lifted face
  from its ghost. Keep these silhouettes distinct in menus and node networks.
- Selection patterns may omit the grid: Checker is contiguous alternating solid
  cells; Random is a sparse, irregular scatter. These selected cells, like the
  existing selected points, use solid ink. Grow and Shrink use two opposing
  arrows at the region edge, with space to read their outward or inward heads.
- Every new filename must have a library-wide unique stem: luce-ui embeds by
  stem, regardless of folder.
- Tool-specific drawings may specify extra normal arrows or analysis fill
  values (for example .15 density and .6 selected centers); those explicit
  exceptions do not change the four default tiers.

#### Five worked examples

1. **Fillet (`3d/cad`):** enlarged radius-10 quarter-round edge, 2.5 px subject
   contour; offset boundary at 1.5 px, shaded strip .3. Chamfer uses the same
   section with a long straight diagonal. No cube, isoline or rolling ball.
   Sketch Fillet and Sketch Chamfer use the corresponding flat, unshaded outline.
2. **Offset Face (`3d/cad`):** a diamond face with fill .45
   and 2 px outline, clearly separated above the original ghost diamond. An
   upward arrow sits beside the gap. No connecting walls: those would turn the
   silhouette back into Extrude's continuous tall prism. Press Pull has its own
   `3d/cad/press-pull.svg`: one upright isometric face with a double-headed arrow
   through its center along the diagonal normal. Move/Copy keeps its four-way cross.
3. **Skin (`3d/surfacing`):** three bold section curves, spaced across a .25
   lofted region, with two lighter boundaries joining their ends. No arrow.
   Rail uses an arched section across two long rails; Profile Sweep uses a square
   profile and a path; Tube uses a broad elbow with round open ends. Align has a
   continuity mark across a seam, Square four bowed boundaries, and Extend a
   lighter continuation beyond the original edge.
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

For a reproducible before/after review of exactly the changed icons, use:

```sh
python3 rounded/scripts/review_changes.py --before-ref 8bfff65 \
  --output-dir /tmp/lucia-round3/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/round3
```

This renders each version with `resvg` at 16, 24, 48 and 96 px in both themes,
enabled and at 35% overall opacity. It writes labelled `round3_before.png` and
`round3_after.png` sheets at native 16/24/48 px, with the identical changed-icon
inventory in each. Newly added icons have a labelled placeholder in the before
sheet. The output directory holds individual PNGs, temporary SVGs, a changed-icon
manifest and a separate reference list. `--names` optionally supplies a preferred
stem order; its list must match exactly the changed inventory. Use a different
baseline and output prefix for subsequent rounds. The script requires `resvg`
and Python 3.9+ only.

Round 4 uses the same 31-icon inventory in both sheets, with side-by-side
comparisons of the confused pairs. Reproduce it with:

```sh
python3 rounded/scripts/review_changes.py --before-ref d602dc6 \
  --names rounded/reviews/round4-icons.txt \
  --pairs rounded/reviews/round4-pairs.txt \
  --output-dir /tmp/lucia-round4/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/round4
```

`--pairs` takes two icon stems per line and can include unchanged family
references, marked with an asterisk. Reblend uses an existing radius with a
resize arrow; Surface Fillet joins two surface sets. Null has an empty center,
and Switch shows two inputs with one selected connection.

Round 5 revises eight icons and adds **Press Pull**. The exact nine-icon
inventory appears in both sheets, with unchanged **Extrude** and **Offset Face**
beside Press Pull in the family comparisons. Reproduce it with:

```sh
python3 rounded/scripts/review_changes.py --before-ref 4b07e9a \
  --names rounded/reviews/round5-icons.txt \
  --pairs rounded/reviews/round5-pairs.txt \
  --output-dir /tmp/lucia-round5/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/round5
```

Trim Curve uses a gap mark and a dashed .45 cutoff. The two curve/mesh
conversions share a clear 2 × 2 quad grid and a balanced S-curve. The pictured
**Convert to Mesh** node uses `3d/nodes/volume-to-mesh.svg`, now a combined soft
volume (.25 fill) and quad grid. Remove Faces uses the full selection-cube
bounds; Shrink shows two inward arrows around its trim boundary and ghosted
control net. UV Project uses a downward arrow over a checker plane, and Blast
shows retained cells beside a ghosted removed cell and an x.

Round 6 revises eleven icons from `88debb5` without changing filenames. The
before/after sheets contain exactly that inventory, with the unchanged Move tool
as the sole reference. All three conversion pairings appear side by side, along
with Press Pull / Move, UV Project / Surface Normal, Shell / Remove Faces, and
Offset Face / Extrude. Reproduce them with:

```sh
python3 rounded/scripts/review_changes.py --before-ref 88debb5 \
  --names rounded/reviews/round6-icons.txt \
  --pairs rounded/reviews/round6-pairs.txt \
  --output-dir /tmp/lucia-round6/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/round6
```

Press Pull uses one .45 face and one double-headed arrow along its normal; its
upright face separates it from Move/Copy's cross at 16 px. UV Project projects a
checker tile onto a surface with two projection lines. Surface Normal uses a
curved patch with short normal arrows and a tick. Trim Curve has a 2.5 px kept
segment, two solid end ticks around the cut gap, and a dashed tail at .6 opacity.
The three conversions consistently put the source left and target right, with
2 px arrows and S-curves, solid grid contours, and a closed volume cloud filled
at .35. Shell has parallel outer and inner cavity edges with short walls;
Remove Faces leaves an unfilled opening with only a ghost outline. Offset Face
separates two matching faces with a gap; Extrude joins its swept face to a flat
base with continuous prism walls. Review at 16/24/48/96 px in both themes,
enabled and at 35%, and with context and ghost strokes hidden.

The offline catalog falls back to selecting the SVG source for manual copying
if clipboard access is unavailable. Individual downloads work offline.

### Stage 6: poly tools

Eight new icons extend the rounded 3D family:

- `primitives/`: `icosphere`, `quad-sphere`, `disc`, `platonic-solid`.
- `curves/`: `helix`.
- `modeling/`: `poly-pen`.
- `modifiers/`: `shrinkwrap`.
- `viewport/`: `snap-target`.

Icosphere uses ten visible triangular facets; Quad Sphere uses a rounded cube
face subdivided into four quads, with eight surrounding quads and no converging
meridian poles. Disc is a filled, flat fan in perspective; Platonic Solid is an
octahedron with four visible faces. Their non-overlapping .2, .3 and .45 fills
separate the lit, side and front faces beneath the solid topology edges.

Helix winds vertically with thinner rear wire segments and a dashed axis, while
Curve Spiral stays planar. Poly Pen places a quad corner with its nib and marks
all four vertices. Shrinkwrap bends a quad strip over a shaded solid, with two
arrows pointing onto the surface. Snap Target puts a four-arm crosshair on the
same curved patch as Snap Surface. No existing icon artwork changes.

Reproduce the review at native 16/24/48 px, both themes, enabled and at 35%
opacity; the render directory also includes individual 96 px images:

```sh
python3 rounded/scripts/review_changes.py --before-ref 51973d0 \
  --names rounded/reviews/stage6-icons.txt \
  --pairs rounded/reviews/stage6-pairs.txt \
  --output-dir /tmp/lucia-stage6/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/stage6
cp /Users/sedov/Dev/luce_work/codex/stage6_after.png \
  /Users/sedov/Dev/luce_work/codex/stage6_sheet.png
```

The sheet pairs the new icons with Sphere, Cube, Curve Spiral, Pen Tool, Shrink
Surface and Snap Surface. The before sheet marks all eight additions as absent
at the baseline and retains the same unchanged neighbours.

### Stage 7: mesh shape, normals and seams

Ten new icons extend the existing categories:

- `modeling/`: `circularize`, `straighten`, `space-evenly`, `make-planar`,
  `recalculate-normals`, `hard-edges`, `soft-edges`, `smooth-by-angle`.
- `shading/`: `mark-seam`, `seams-from-islands`.

Circularize overlays a jagged ghost loop with a clean circle and picked points.
Straighten presses a wavy ghost run onto a straight row of points; Space Evenly
adds equal measurement intervals below its points. Make Planar retains two
coplanar faces beneath the bent ghost, separating it from Flatten and Set Planar.
Recalculate Normals combines two agreeing arrows with a ghost flipped arrow and
a turning arc; this explicit normal illustration uses the extra-arrow exception.

Hard Edges and Soft Edges share the selection cube and .2/.3/.45 values. The hard
corner has a 3.25 px selected edge and flat face values; the soft corner replaces
that edge with a continuous curved value boundary and a thin smooth isoline.
Smooth by Angle separates a shaded patch from its angle arc and threshold tick.
Mark Seam uses full-opacity 2.5 px stitch dashes; Seams from Islands converts an
L-shaped UV boundary into the same seam dashes on a .6-scale selection cube.
Fills are separate, non-overlapping regions beneath the contours. Existing icon
artwork is unchanged.

Reproduce the new-icon and neighbour review at native 16/24/48 px, light and
dark, enabled and at 35% opacity. Individual 96 px renders are also generated:

```sh
python3 rounded/scripts/review_changes.py --before-ref cbc31cb \
  --names rounded/reviews/stage7-icons.txt \
  --pairs rounded/reviews/stage7-pairs.txt \
  --output-dir /tmp/lucia-stage7/renders \
  --sheet-prefix /Users/sedov/Dev/luce_work/codex/stage7
cp /Users/sedov/Dev/luce_work/codex/stage7_after.png \
  /Users/sedov/Dev/luce_work/codex/stage7_sheet.png
```

The comparisons include the existing circle, curve, planar, normal, selection,
shading and UV tools, plus the new hard/soft and seam pairs. Subject-only checks
hide ghost, context and isoline strokes at 16 and 24 px in both themes and states.
No requested icon was skipped or substituted.

## License

Icons by Dy Mokomi. See the repository's [CC BY 4.0 license](../LICENSE) and
[attribution guidance](../README.md#license).
