---
name: liquid-interface
description: >-
  Design and implement a liquid or metaball-style interface where nearby
  rounded DOM elements visually merge while remaining real, accessible
  controls. Use for draggable liquid cards, magnetic clusters, blob bridges,
  gooey navigation, or SDF-driven union effects. Do not use for native Apple
  Liquid Glass, a generic backdrop blur, or a static gradient blob.
license: MIT
---

# Liquid Interface

Create a visual material layer that responds to semantic DOM geometry. The
effect must never replace the real controls, text, focus model, or interaction
contract.

Read before acting:

- `../../references/interface-principles.md`
- `../../references/visual-systems.md`
- `../../references/motion-principles.md`
- `../../references/evidence-and-verification.md`

## Establish the brief

Ask or discover:

- which elements merge and what remains visually separate;
- whether the interaction is drag, proximity, hover, scroll, state change, or
  ambient motion;
- desired character: geometric, viscous, soft, elastic, glassy, or restrained;
- target element count and maximum region size;
- target browsers, devices, frame budget, and fallback requirement;
- keyboard and touch alternative;
- reduced-motion behavior;
- whether text and controls stay visually present during the merge.

If the user has not selected a visual direction, use `prototype-lab` to compare
distinct material models before production work.

## Preserve a two-layer architecture

### Semantic layer

Use real DOM elements for:

- text;
- buttons, links, sliders, and draggable handles;
- focus, hover, press, disabled, and selected states;
- accessible names, descriptions, and keyboard behavior.

### Visual union layer

Render the shared silhouette behind or around the semantic layer. Set decorative
output to ignore pointer events and accessibility APIs. Synchronize geometry
without duplicating semantic content.

## Recommended SDF contour model

For a small set of rounded rectangles:

1. measure each relevant DOM box relative to one bounded effect container;
2. represent each box as a signed-distance rounded rectangle;
3. combine nearby distances with a smooth-min function;
4. optionally add capsule-like bridges when the interaction calls for more
   directed connection;
5. sample the combined field on an adaptive grid;
6. extract the zero contour with marching squares;
7. linearly interpolate edge crossings;
8. stitch ordered segments into closed contours;
9. smooth only enough to remove grid artifacts;
10. render one or more SVG paths behind the real elements.

This is a model, not permission to copy a reference implementation.

### Conceptual functions

```text
d_box(p, box, radius) -> signed distance
smooth_union(a, b, blend) -> combined distance
sample(field, bounds, cell_size) -> scalar grid
march(grid, iso = 0) -> edge segments
stitch(segments) -> closed contours
smooth(contour, passes) -> renderable path
```

Keep shape units and screen units explicit. A larger smooth-union parameter does
not mean the same thing across differently scaled formulas.

## Geometry and update lifecycle

- Measure with `getBoundingClientRect` in one read phase.
- Convert coordinates once into container-local space.
- Bound the sampled region to the union of shapes plus the maximum bridge range.
- Update through one scheduled animation frame.
- Observe resize and relevant layout changes.
- Recompute only while geometry or effect parameters change.
- Pause when hidden or outside the relevant viewport.
- Clean up pointer capture, observers, and scheduled frames.

Do not sample the whole page or allocate a large new grid every frame.

## Interaction contract

For draggable elements:

- use pointer capture;
- preserve the grab offset;
- define bounds and resistance;
- support touch without blocking unrelated page scroll outside the handle;
- provide keyboard movement or equivalent controls;
- expose current position or meaningful state when it matters;
- make Escape cancel or restore when appropriate;
- retain visible focus above the liquid layer.

A non-focusable draggable square is not an acceptable final control.

## Material controls

Expose a small, meaningful parameter set:

- merge/blend distance;
- contour resolution;
- corner radius;
- bridge bias;
- smoothing passes;
- fill, border, shadow, and optional blur;
- motion response.

Presets such as `geometric` and `viscous` should alter the model coherently, not
just recolor it. Clamp expensive combinations and explain the quality/performance
tradeoff.

## Alternative rendering strategies

Choose deliberately:

- CSS/SVG filter goo: quick atmospheric effect, less geometric control;
- SVG masks/filters: bounded DOM-adjacent material;
- SDF + SVG contour: precise small interactive clusters;
- canvas: many shapes or direct pixel rendering;
- WebGL shader: large continuous fields with a justified GPU pipeline.

Keep a static rounded-surface fallback for unsupported or constrained contexts.

## Verification

Test:

- clearly separate, near, first bridge, merged, and separating states;
- slow and fast dragging;
- keyboard-only and touch operation;
- focus visibility and semantic names;
- resize, scroll, zoom, and responsive recomposition;
- high-DPI edges and contour closure;
- reduced motion;
- hidden-tab pause and teardown;
- text legibility throughout the merge;
- representative CPU/GPU cost at worst allowed settings.

Record whether the reference behavior, local implementation, and deployed
surface were each actually observed.
