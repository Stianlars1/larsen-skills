---
name: reverse-engineer-motion
description: >-
  Analyze an authorized local or public reference video frame by frame and turn
  it into an evidence-backed visual and motion specification, implementation
  plan, and optional prototype brief. Use when the user wants to understand or
  recreate the behavior, composition, transitions, perspective, or graphics in
  a recorded interface. Do not use for copying protected assets or for a simple
  animation review of an existing codebase. Triggers on reverse engineer, recreate
  this animation, analyze this video, frame by frame, "how did they build this",
  motion spec from a recording, extract frames.
license: MIT
---

# Reverse Engineer Motion

Reconstruct the system behind a reference, not merely its most attractive frame.
The deliverable must explain what is observed, what is inferred, and how a new
implementation can achieve the same class of behavior without copying protected
expression.

## Quick reference

| Need | Read |
| --- | --- |
| Evidence boundaries, verification environments, reproducibility, feel checks | `references/evidence-and-verification.md` |
| Easing vocabulary, duration budgets, springs, interruptibility, performance | `references/motion-principles.md` |
| Direct manipulation, velocity, momentum projection, rubber-banding | `references/gesture-physics.md` |
| Typography, color, radius, elevation, materials, gradients in the visual model | `references/surfaces-and-depth.md` |
| Product job, hierarchy, restraint, working order | `references/interface-principles.md` |

**Naming the observed effect precisely makes the specification portable.** Use
`motion-vocabulary` when the right term for a behavior is unclear — a spec that
says "shared element transition" is executable; one that says "the thing where it
grows into the page" is not.

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

### Judge the reference before reproducing it

A reference being attractive is not proof it is correct. Before recommending
parity, run the observed behavior through the frequency and purpose gates in
`references/motion-principles.md`:

- A 400ms transition captured in a polished product demo may still be wrong for a
  surface your user hits fifty times a day.
- Marketing and explanatory motion is allowed to be slower and showier than the
  same effect would be inside a product.
- A recording cannot show `prefers-reduced-motion`, keyboard operation, focus
  behavior, or the non-pointer path. Those are **unknown**, not absent — say so,
  and specify them yourself rather than shipping a gap.
- A recording shows one viewport, one theme, and one device-pixel ratio. Do not
  infer responsive behavior from a single capture.

Where the reference violates a rule this collection treats as non-negotiable,
say so explicitly and specify the corrected version alongside the observed one.
The user can then choose parity or correctness knowingly.

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

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Claiming every frame was reviewed | State the actual sampling and measurement method |
| Current code cited as proof of what an old recording shows | Compare the two independently; neither proves the other |
| Inference stated with the confidence of an observation | Label every conclusion observed, inferred, or unknown |
| A single attractive frame reconstructed as the system | Reconstruct the whole arc, including rest and dwell |
| Reproducing the reference's rule violations uncritically | Run it through the frequency and purpose gates first |
| Reduced motion or keyboard treated as absent | They are **unknown** from a recording — specify them yourself |
| Responsive behavior inferred from one capture | One viewport proves one viewport |
| Frames overwritten into a previous analysis directory | Unique output directory per run; never overwrite the source |
| Brand assets or copy carried into the implementation | Preserve behavior, replace protected expression |
| Media downloaded or frames published without authorization | Resolve provenance at the rights gate first |
