# Reference case studies

These case studies describe reusable patterns observed in two existing,
user-owned implementations. They are not templates to copy verbatim.

## Layered material cycle

### Asset model

- Six 128×128 raster exports share an identical crop.
- The order forms a material journey: dark, clear-dark, clear-light, default
  color, light tint, dark tint, then back to dark.
- Every asset remains a real image layer. Motion hides the handoff instead of
  attempting to redraw Icon Composer materials in CSS.

### Choreography model

Each hop has a motion derived from the relationship between the two materials:

- a liquid squash and blur drains color into a clear state;
- a 3D edge flip changes the apparent glass face;
- a circular reveal blooms color from the center;
- a continuous spin swaps layers near peak velocity;
- a diagonal clip follows the mark's stripe axis;
- a zoom/blur dissolve returns to the home material.

The transitions share an easing family and a common rest pose, so different
effects still read as one curated cycle.

### Runtime model

- Web Animations API controls each hop.
- Raster layers decode before the first transition.
- `will-change` is set only around active animation.
- The cycle waits between hops.
- Hidden documents and pointer inspection defer the next hop.
- Reduced motion leaves the static first state.
- Unmount cancels animations, listeners, and timers.

### Lesson

Use layered raster variants when the material rendering is valuable and the
geometry/crop is already aligned. The unique choreography belongs in the
handoffs, not in an attempt to approximate the materials.

## Decomposed SVG cycle

### Asset model

- The mark consists of a large rounded square, a smaller rounded square, and a
  carved negative-space relationship.
- Separate SVG groups own camera framing, rotation, large-part transform,
  small-part transform, and mask/carve transform.
- One padded coordinate system contains both the static logo crop and every
  loader pose.

### Choreography model

One continuous timeline:

1. holds the resting logo;
2. compresses the large part while the small part gains mass;
3. moves the compressed cluster to its optical pivot;
4. completes a full turn while small;
5. pulls the framing back to expose a larger travel canvas;
6. sends the small part and its carve through the canvas corners;
7. trades the relative size of the two parts;
8. settles into the exact original crop.

Related phases overlap. A single timeline per SVG group avoids an easing reset
between internal beats.

### Runtime model

- CSS keyframes carry the predetermined visual timeline.
- JavaScript only schedules cycles and handles lifecycle state.
- The static resting geometry is present before the playing class is added.
- Hidden documents, pointer inspection, reduced motion, and unmount are handled
  outside the keyframes.
- Unit tests verify scheduling, but visual frames are still required to verify
  choreography.

### Lesson

Decompose an SVG when its parts and negative space provide meaningful motion.
Use nested groups to keep camera, pivot, and part transforms independent. A
single overlapping timeline often feels more cohesive than several loaders
played end to end.

## Shared lessons

- The logo's structure chooses the effects.
- Resting identity and loop seam are hard invariants.
- Long ambient sequences need stillness.
- Lifecycle behavior is part of motion quality.
- CSS is strong for predetermined vector choreography under load.
- WAAPI is strong for curated state-to-state handoffs.
- Source code and a recorded frame sequence are separate evidence sources and
  may represent different revisions.
