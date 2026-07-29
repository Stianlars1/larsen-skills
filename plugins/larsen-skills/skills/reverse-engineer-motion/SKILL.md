---
name: reverse-engineer-motion
description: >-
  Analyze an authorized local or public reference video frame by frame and turn
  it into an evidence-backed visual and motion specification, implementation
  plan, and optional prototype brief. Use when the user wants to understand or
  recreate the behavior, composition, transitions, perspective, or graphics in
  a recorded interface. Do not use for copying protected assets or for a simple
  animation review of an existing codebase.
license: MIT
---

# Reverse Engineer Motion

Reconstruct the system behind a reference, not merely its most attractive frame.
The deliverable must explain what is observed, what is inferred, and how a new
implementation can achieve the same class of behavior without copying protected
expression.

Read before acting:

- `../../references/evidence-and-verification.md`
- `../../references/motion-principles.md`
- `../../references/interface-principles.md`
- `../../references/visual-systems.md`

## Rights and input gate

Establish:

- exact video path or explicitly authorized URL;
- whether the user owns the recording or has permission to analyze it;
- whether the goal is learning, behavior parity, stylistic direction, or a
  near-match;
- which product assets, names, copy, and imagery must not be reproduced;
- target stack, viewport, input methods, and performance class.

Do not silently download media, bypass access controls, copy branded assets, or
publish extracted frames. If provenance is unresolved, analysis may describe
general principles but must not redistribute source content.

## Create a reproducible analysis run

Use a unique output directory. Preserve the source and prior analyses.

Record:

- source identity and snapshot date;
- container, codec, dimensions, duration, nominal and decoded frame counts, and
  frame rate;
- extraction commands or tools;
- timestamp and frame-number convention;
- sampling strategy;
- known variable-frame-rate, dropped-frame, or editing ambiguity.

Prefer `ffprobe` and `ffmpeg` when available. Use the environment's existing
media tools rather than installing a dependency without permission.

## Inspect in layers

### 1. Orientation pass

Inspect the first frame, final frame, scene boundaries, and a uniform timeline.
Produce one overview contact sheet that reveals the full arc.

### 2. Activity pass

Measure or visually estimate frame-to-frame change to find:

- first visible motion;
- acceleration and peak activity;
- state handoffs;
- settles and exact rest;
- dwell;
- loops or cuts.

Dense frame deltas help locate activity but do not explain the movement.

### 3. Transition pass

Extract denser samples around every material transition. Inspect individual
frames at original resolution where blur, masks, paths, occlusion, or small UI
details matter.

### 4. Interaction pass

If the recording contains input, identify pointer, touch, scroll, drag, keyboard,
or automatic triggers. Distinguish user-driven scrubbing from time-driven
playback.

Never claim every frame was manually reviewed unless it was. State the actual
sampling and measurement method.

## Build the evidence model

Describe:

- canvas, viewport, responsive crop, and safe areas;
- camera, perspective, scale, and depth cues;
- persistent and transient layers;
- typography, color, gradient, material, noise, lighting, and shadow;
- geometric primitives, masks, clipping, negative space, and SVG paths;
- entrance, travel, morph, handoff, follow-through, settle, and dwell;
- occlusion and z-order changes;
- timing, overlap, stagger, easing shape, transform origin, and velocity;
- input and state transitions;
- accessibility and non-motion behavior visible in the evidence.

For every conclusion, label confidence and supporting frames or source lines.

## Write the motion specification

Use this structure:

```markdown
# Reference analysis
## Evidence and limitations
## Visual system
## Layer and state model
## Timeline
## Transition specifications
## Interaction model
## Responsive behavior
## Reduced-motion behavior
## Rendering strategy
## Asset plan
## Performance risks
## Verification matrix
```

Each transition specification should include:

| Field | Content |
| --- | --- |
| Range | Start/end timestamp and frame |
| Trigger | User input, state, scroll, or schedule |
| Elements | Persistent, entering, and exiting layers |
| Properties | Position, scale, rotation, opacity, blur, mask, path, color |
| Motion | Direction, origin, acceleration, overlap, settle |
| Evidence | Frames, runtime observation, or inspected source |
| Confidence | High, medium, or low |
| Implementation | Smallest credible rendering approach |

## Convert analysis into an original implementation plan

Preserve transferable behavior:

- hierarchy;
- spatial relationship;
- temporal rhythm;
- interaction model;
- material qualities;
- accessibility and performance constraints.

Replace protected or product-specific expression:

- logos and brand assets;
- copy;
- illustrations and imagery;
- exact ornamental styling;
- any implementation code without established reuse rights.

When multiple explanations fit the evidence, propose alternatives and ask the
user which one to prototype.

## Deliverables

Produce, as applicable:

- `evidence.json` with source metadata and sampled frame references;
- contact sheets and selected high-resolution frames;
- `motion-spec.md`;
- a component/state/timeline implementation plan;
- a verification matrix;
- an optional concise generation prompt derived from the specification.

Do not begin production integration until the user approves the reconstructed
direction. A prototype should use replaceable assets and remain isolated.
