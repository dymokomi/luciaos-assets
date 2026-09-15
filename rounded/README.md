# GFX Rounded

**144 editable SVG icons** for graphics editing, 3D applications, and code editors.

## Browse

- [Searchable catalog](catalog.html): search names and keywords, filter by domain, change theme and size, copy SVG source, or download an individual icon. Open it locally; it has no network dependencies.
- [Selected icons](preview.png) · [Dark preview](preview-dark.png)
- [Full icon index](ICONS.md)
- [Metadata](catalog.json): stable IDs, names, domains, categories, search keywords, and file paths.

| Domain | Count | Full previews |
| --- | ---: | --- |
| Graphics & shared controls | 67 | [1](previews/graphics-01.png), [2](previews/graphics-02.png), [3](previews/graphics-03.png) |
| 3D tools | 40 | [1](previews/3d-01.png), [2](previews/3d-02.png) |
| Code editor | 37 | [1](previews/code-01.png), [2](previews/code-02.png) |

Each preview page also has an editable `.svg` version and a `-dark` version. Actual-size samples: [graphics](previews/graphics-sizes.png), [3D](previews/3d-sizes.png), and [code](previews/code-sizes.png).

## Design

- **Canvas:** 24 × 24; transparent backgrounds.
- **Base stroke:** 2 px, with rounded ends and joins, fuller corners, and gently bowed contours.
- **Color:** `currentColor`. Selected faces use a translucent fill; playback indicators use solid shapes; Edge selection uses a heavier line to identify the selected edge.
- **Geometry:** native paths and shapes. No icon fonts, raster images, or external references.
- **Scale:** reviewed at 16, 20, 24, and 48 px. Prefer 24 px for detailed tools; small indicators and internal divisions become less distinct at 16 px.

The original 23 icon IDs remain available, including `magic-wand-tool`, `selection-tool`, separate `snap` and `grid`, and all eight alignment/distribution controls.

## Use inline SVG

Copy any file from `icons/` into your markup. The icon inherits CSS `color`. Set `width` and `height` to the desired size. An SVG loaded through `<img>` does not inherit the surrounding page's CSS color; use inline SVG, the sprite, or a CSS mask for theme-aware color.

## Use the symbol sprite

Serve `sprite.svg` with your app and reference a symbol by its filename stem:

```html
<button type="button" aria-label="Extrude selected faces" style="color: #7276df">
  <svg width="24" height="24" aria-hidden="true" focusable="false">
    <use href="/icons/sprite.svg#extrude"></use>
  </svg>
</button>
```

Adjust the URL to match where you serve the sprite. External sprite references should use the same origin. For a self-contained page, insert the sprite markup in the document with `style="display: none"` on its outer SVG, and reference `href="#extrude"`.

Individual SVGs have no fixed IDs or titles, so they can be repeated safely. Put an accessible name on icon-only buttons and hide their decorative SVGs with `aria-hidden="true"`. A standalone meaningful inline SVG can use `role="img"` and an appropriate `aria-label`.

Clipboard access in the catalog depends on the browser. If clipboard access is unavailable, the catalog selects the source text for manual copying. Individual SVG downloads work offline.

## Naming conventions

- IDs use lowercase kebab-case, matching the filename: `brush-tool.svg`, `vertex-select.svg`, `git-branch.svg`.
- Tool names generally end in `-tool`; actions and objects use descriptive names.
- `align-vertical-center` aligns center Y positions around a horizontal guide. `align-horizontal-center` aligns center X positions around a vertical guide.
- Graphics includes shared controls such as Save, Undo, Zoom, Lock, and Visibility; these can be reused in the other applications.

## Rebuild previews and catalog

Edit the SVGs in `icons/`, then run:

```sh
python3 scripts/build_previews.py
```

The script uses only Python's standard library. It rebuilds `sprite.svg`, `catalog.html`, the SVG previews, and the preview index from `catalog.json` and the source SVGs. When adding an icon, add its metadata to `catalog.json` as well.

PNG previews and ZIP archives are snapshots; regenerate them after editing. The raw SVGs are the editable originals.
