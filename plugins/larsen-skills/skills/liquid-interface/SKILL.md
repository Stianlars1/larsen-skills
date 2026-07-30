---
name: liquid-interface
description: >-
  Design and implement a liquid or metaball-style interface where nearby
  rounded DOM elements visually merge while remaining real, accessible
  controls. Use for draggable liquid cards, magnetic clusters, blob bridges,
  gooey navigation, or SDF-driven union effects. Do not use for native Apple
  Liquid Glass, a generic backdrop blur, or a static gradient blob. Triggers on
  metaball, gooey effect, blob merge, liquid UI, magnetic cards, SDF, smooth
  union, marching squares, "make these elements merge".
license: MIT
---

# Liquid Interface

Create a visual material layer that responds to semantic DOM geometry. The
effect must never replace the real controls, text, focus model, or interaction
contract.

**The two-layer architecture is the whole discipline.** A liquid effect that
absorbs the semantics it decorates is a regression no amount of visual quality
redeems.

## Quick reference

| Need | Read |
| --- | --- |
| Drag, pointer capture, velocity, boundaries, keyboard parity, cleanup | `references/gesture-physics.md` |
| Semantics, focus, names, hit areas, keyboard patterns | `references/accessibility-contract.md` |
| Radius, elevation, materials, translucency, gradients | `references/surfaces-and-depth.md` |
| Easing, duration, interruptibility, motion performance, reduced motion | `references/motion-principles.md` |
| Product job, hierarchy, restraint | `references/interface-principles.md` |
| Evidence boundaries and verification | `references/evidence-and-verification.md` |

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

Full drag mechanics live in `references/gesture-physics.md`. The requirements
this skill will not ship without:

- **pointer capture** via `setPointerCapture`, so tracking survives the pointer
  leaving the element;
- **the grab offset preserved** — never snap the element's centre to the pointer;
- **multi-touch protection** — ignore extra touch points after a drag begins;
- **rubber-banding at bounds**, never a hard stop;
- **velocity-based commit**, not distance alone (~`0.11` px/ms as a starting
  threshold), with the velocity *sign* at release deciding reverse versus commit;
- **touch support that does not block unrelated page scroll** — scope
  `touch-action` to the handle, not the page;
- **keyboard movement or an equivalent control**, with Escape to cancel or
  restore;
- **current position or state exposed** when it carries meaning;
- **visible focus above the liquid layer**;
- **full teardown** — pointer capture, observers, and scheduled frames released
  on unmount.

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

## Performance budget

The union layer is the most expensive thing on the page. Treat these as hard
limits rather than aspirations:

- **Bound the sampled region** to the union of shapes plus the maximum bridge
  range — never the viewport, never the document.
- **Allocate the grid once** and reuse it. A fresh typed array every frame is the
  most common cause of jank here.
- **One scheduled frame per update**, with all `getBoundingClientRect` reads in a
  single read phase before any write.
- **Recompute only while geometry or parameters change.** A static cluster costs
  zero frames.
- **Pause when hidden or off-screen** via `visibilitychange` and an
  `IntersectionObserver`.
- **Keep blur under 20px** and verify Safari specifically — filter cost there is
  materially higher.
- **Clamp resolution × element count.** Expose the tradeoff to the user rather
  than silently allowing a combination that drops frames.
- Reduced motion keeps the merged *shape* and removes the ambient movement; the
  material is information, the drift is decoration.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| The visual layer replaces the real controls | Two layers: semantic DOM under, decorative union behind |
| Decorative layer reachable by pointer or screen reader | `pointer-events: none` and `aria-hidden="true"` |
| Draggable element is a non-focusable `<div>` | Real control, visible focus, keyboard path |
| Sampling the whole page | Bound to the shape union plus bridge range |
| New grid allocated every frame | Allocate once, reuse |
| Reads and writes interleaved per element | One read phase, then one write phase |
| Effect keeps running in a hidden tab | Pause on `visibilitychange` and off-screen |
| Blend parameter copied between differently scaled formulas | Keep shape units and screen units explicit |
| Contour left open at high DPI | Verify stitching and closure at every device-pixel ratio |
| Text illegible mid-merge | Check legibility across the whole transition, not just the endpoints |
| Reduced motion disables the whole effect | Keep the shape, drop the ambient drift |

## Verification

Test:

- clearly separate, near, first bridge, merged, and separating states;
- slow drags and fast flicks, in both directions;
- release while reversing, to confirm the velocity sign decides the outcome;
- over-drag past every boundary;
- keyboard-only and touch operation;
- focus visibility and semantic names in the accessibility tree;
- resize, scroll, zoom to 200%, and responsive recomposition;
- high-DPI edges and contour closure;
- reduced motion;
- hidden-tab pause and full teardown on unmount;
- text legibility throughout the merge, not only at rest;
- representative CPU/GPU cost at the worst allowed settings, on low-power
  hardware rather than a desktop demo.

Record whether the reference behavior, local implementation, and deployed surface
were each actually observed. Gesture feel cannot be verified from source alone —
state plainly when only source was inspected.
