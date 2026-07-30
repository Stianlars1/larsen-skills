---
name: animated-logo-cycle
description: >-
  Turn an existing logo, app icon, SVG mark, or set of brand variants into a
  geometry-led animated identity: first analyze the logo's parts and negative
  space, then propose distinct loader and motion concepts, prototype the
  selected directions, and build a polished looping logo cycle. Use when the
  user asks for an animated logo, logo cycle, branded loader or spinner, logo
  morph, app-icon theme cycle, or wants several creative motion directions
  derived from the logo itself. Do not use for static logo design, generic
  loading indicators with no brand asset, or decorative motion unrelated to a
  logo.
license: MIT
---

# Animated Logo Cycle

Create motion that could only belong to the supplied logo. The logo's geometry,
negative space, material variants, and visual rhythm must determine the
choreography. A fade, scale, blur, or rotation is a supporting technique, not a
concept by itself.

## Quick reference

| Need | Read |
| --- | --- |
| Motion families the logo's own geometry can support | `references/choreography-guide.md` |
| Worked examples of geometry-led cycles | `references/logo-cycle-case-studies.md` |
| The specification format for the chosen cycle | `templates/motion-spec.md` |
| Easing, springs, ambient-sequence rules, performance, reduced motion | `references/motion-principles.md` |
| Decorative-duplicate naming, reduced motion as a requirement | `references/accessibility-contract.md` |
| Evidence boundaries, frame analysis, feel checks | `references/evidence-and-verification.md` |

**An ambient brand loop is not UI feedback.** The sub-300ms budget does not apply
to it — see `references/motion-principles.md` §9 for the rules that do. Everything
else in that file, especially the performance and reduced-motion sections, applies
in full.

## Non-negotiable workflow

Do not jump from an asset to production code.

1. Establish the intended use and constraints.
2. Inspect the real assets and any reference recording.
3. Write a logo-anatomy model.
4. Propose genuinely different concepts.
5. Stop and let the user select directions.
6. Prototype the selected directions in isolation.
7. Stop and let the user select the final choreography.
8. Implement, verify, and document the chosen cycle.

The two selection gates are required. The user owns the creative choice.

## 1. Establish the brief

Ask for every decision that cannot be proven from the project. Keep related
questions together, but do not silently choose defaults for brand decisions.

Required decisions:

- **Context:** navbar identity, loader, onboarding, launch page, app icon,
  splash screen, or another placement.
- **Frequency:** continuous ambient loop, occasional cycle, user-triggered
  replay, or loading-state motion.
- **Exploration count:** how many concepts to prototype. Recommend 3–5 when the
  user has no preference.
- **Color policy:** preserve one color, cycle supplied brand variants, or
  explore a user-approved palette.
- **Motion character:** restrained, precise, elastic, playful, mechanical,
  liquid, dimensional, or another defined quality.
- **Implementation target:** framework, rendering environment, supported
  browsers, expected display sizes, and whether a motion library is already in
  use.
- **Source of truth:** which SVG, raster exports, icon variants, design tokens,
  or reference videos are authoritative.

Also establish whether the animation is decorative or communicates state. That
determines accessible naming and whether a static alternative is sufficient.

## 2. Inspect before imagining

Inspect repository instructions, current dependencies, existing logo usage, and
dirty work before touching code. Preserve unrelated changes.

For every supplied asset, record:

- file type, dimensions, viewBox, aspect ratio, alpha/background behavior;
- light, dark, monochrome, tinted, material, and size variants;
- fill and stroke ownership;
- SVG groups, paths, primitive shapes, masks, clip paths, and filters;
- repeated modules, symmetry, diagonals, axes, corners, and optical center;
- negative-space shapes that must remain legible;
- raster variants that share an identical crop and can be layered safely;
- SVG paths that are structurally compatible for interpolation;
- protected invariants: clear space, proportions, corner radii, stroke weight,
  brand colors, and the exact resting silhouette.

Render and inspect the logo at its real target sizes. A concept that works at
128px can become noise at 20px.

### Logo-anatomy output

Write a compact table:

| Part | Geometry | Relationship | Motion affordances | Must preserve |
| --- | --- | --- | --- | --- |
| Example: small square | Rounded rectangle | Carves the large square | Orbit, corner travel, size trade | Gap and size ratio |

Separate observations from interpretations:

- **Observed:** directly supported by source assets or code.
- **Inferred:** a plausible design reading that still needs user approval.
- **Unknown:** information that cannot be established from the available
  evidence.

## 3. Analyze reference motion

When a video or frame sequence is supplied:

1. Probe duration, dimensions, frame rate, and decoded frame count.
2. Preserve first and last frames.
3. Inspect the complete arc with contact sheets.
4. Inspect every transition at a denser sampling rate.
5. Step through frames around anticipation, peak velocity, handoff, and settle.
6. Compare the recording with current source code independently.

Never treat current code as proof of what an older recording shows, or a video
as proof of the current implementation.

Extract:

- resting poses and dwell lengths;
- beat boundaries and overlaps;
- transform origin and optical pivot;
- acceleration, peak velocity, and deceleration;
- swaps hidden by blur, occlusion, edge-on rotation, masks, or peak motion;
- camera/crop changes used to make room for transformed geometry;
- exact loop seam and whether the final frame equals the first;
- frame drops, flashes, size pops, and other visible defects.

If shared `reverse-engineer-motion` tooling is available, use it for frame
extraction and evidence packaging. Otherwise create a new non-destructive
analysis directory; never overwrite the user's frames.

## 4. Generate geometry-led concepts

Propose the user-approved number of concepts. Each must have a different motion
grammar, not merely different colors, easing, or duration.

For each concept include:

- a short, memorable name;
- the specific logo property that inspired it;
- a one-sentence purpose or emotional reading;
- its loader/spinner form;
- its complete cycle form;
- the ordered beats;
- color behavior;
- the likely rendering strategy;
- risks at small sizes, reduced motion, or loop boundaries.

Useful starting families are listed in `references/choreography-guide.md`. Use
only the families supported by the actual logo.

Reject concepts that:

- would work unchanged for almost any logo;
- obscure the mark for most of the cycle;
- depend on random motion;
- break the logo's protected proportions without a purposeful recovery;
- require illegible sub-pixel detail at the target size;
- cannot return to the exact resting frame;
- differ from another proposal only through surface styling.

## 5. Selection gate: concepts

Present the concepts together so the user can compare them. Recommend one, with
reasons, but do not make the decision for the user.

Do not write production integration code until the user selects which concepts
to prototype.

## 6. Prototype selected directions

Build selected concepts in an isolated harness with an instant variant switcher.
Keep production components untouched during exploration.

The prototype must provide:

- replay and pause;
- normal speed and slow motion;
- light and dark backgrounds;
- the real target sizes;
- reduced-motion preview;
- visible variant name;
- an exact static rest frame for comparison.

Three variants means three different choreographies. Do not create one
animation with three parameter presets.

## 7. Write the motion specification

Use `templates/motion-spec.md`. Define the whole cycle before polishing code.

Every timeline must include:

1. **Rest** — recognizable static identity.
2. **Anticipation** — optional wind-up that prepares the main move.
3. **Primary action** — the clearest geometry-led transformation.
4. **Handoff** — the identity or material swap, ideally hidden at peak motion
   or by the logo's own geometry.
5. **Follow-through** — secondary parts resolve after the main mass.
6. **Settle** — return to exact resting geometry.
7. **Dwell** — sufficient stillness before repetition.

Sub-beats may overlap. Overlap often turns several visible tricks into one
continuous action.

### Timing and easing

| Beat | Easing | Note |
| --- | --- | --- |
| Entrance, exit, settle | `ease-out` — `cubic-bezier(0.23, 1, 0.32, 1)` | Arrival reads as decisive |
| On-screen travel between poses | `ease-in-out` — `cubic-bezier(0.77, 0, 0.175, 1)` | Visible departure and arrival |
| Autonomous wind-up before a fast handoff | `ease-in` | Legitimate here **only** because no user input is waiting |
| Constant travel (continuous orbit, uniform path) | `linear` | Never for a beat with a destination |
| Material settle, elastic character | Spring, `bounce: 0` default | `0.1–0.3` only if a preceding beat carried momentum |
| User-triggered replay control | Immediate response, 100–160ms | This part *is* UI and obeys the UI budget |

- **Do not apply sub-300ms UI timing to an ambient brand sequence.** An ambient
  loop is not feedback; it is governed by `references/motion-principles.md` §9.
- **Preserve forward velocity across a visual swap.** If the incoming layer
  represents the same moving object, it must not restart from zero.
- **Give the cycle stillness.** A detailed loop needs contrast between motion and
  rest. Dwell is a designed value, not leftover time.

Specify the numeric values only after observing the prototype at target size —
duration and easing are design variables here. The *shape* of the choice above is
not: an entrance still uses `ease-out` whatever its duration turns out to be.

## 8. Choose the rendering strategy

Choose the simplest strategy that preserves the concept.

| Situation | Preferred strategy | Reason |
| --- | --- | --- |
| Predetermined SVG choreography | CSS keyframes on nested groups | Stable under main-thread load |
| Several same-size raster/material variants | Layered images plus WAAPI or CSS | Clean handoffs without redrawing assets |
| Distinct choreography for each state hop | WAAPI with a small scheduler | Per-hop control and explicit cleanup |
| Interactive, gesture-led, or interruptible motion | Motion/springs | Carries velocity and retargets naturally |
| Compatible vector silhouettes | SVG path interpolation | True shape morph when topology permits |
| Incompatible paths | Masks, clip paths, transforms, or crossfade | Avoids broken path interpolation |
| Complex authored illustration with no DOM requirement | Rive/Lottie or a verified frame sequence | Use only when simpler web primitives cannot reproduce it |

Keep transform functions in the same order across keyframes so browsers
interpolate them predictably. Use wrapper groups when camera framing, rotation,
and part transforms would otherwise compete for one `transform`.

## 9. Build the cycle controller

The visual timeline and lifecycle controller are separate concerns.

The controller must:

- render an exact static rest state before hydration;
- preload or decode every required raster layer before the first handoff;
- prevent duplicate loops;
- finish the current cycle rather than cutting it off when practical;
- defer future cycles while the document is hidden;
- optionally defer while the pointer is over a small identity mark;
- react if reduced-motion preference changes during the session;
- cancel animations, timers, and listeners on unmount;
- restart from a known resting state after cancellation or error.

For reduced motion, keep the static logo. If the motion communicates state,
provide a non-spatial state indication rather than silently removing meaning.

Use `aria-hidden="true"` for a decorative duplicate whose surrounding link or
heading already names the brand. Otherwise expose one stable accessible name;
never let each animated layer announce itself.

## 10. Performance and fidelity

- **Prefer `transform` and `opacity`.** Never `transition: all`, never
  layout-driven animation.
- Use `clip-path` and masks when they express the logo's own geometry;
  `clip-path` is compositor-friendly and causes no layout shift.
- **Keep blur under 20px** and brief. Verify Safari and low-power hardware
  specifically — filter cost there is materially higher.
- Apply `will-change` only to `transform`, `opacity`, or `filter`, only around
  active motion, and remove it after. Never `will-change: all`.
- **Avoid JavaScript per-frame rendering for a predetermined timeline.** CSS and
  WAAPI run off the main thread and stay smooth while the page is loading; a
  `requestAnimationFrame` loop does not. This matters most for a logo, which
  typically animates *during* page load.
- Keep the logo's optical centre stable unless displacement is intentional.
- Verify edge-on 3D frames do not expose a flash or a mirrored intermediate.
- **Ensure filters, masks, and SVG IDs stay correct with multiple instances on
  one page.** Duplicate IDs are the most common cause of a second logo rendering
  wrong.

## 11. Selection gate: final choreography

Show the prototypes at normal speed and slow motion. Let the user choose one
direction or explicitly combine named beats from multiple directions.

Only then integrate the final component.

## 12. Verification

Verify behavior, not just compilation:

- compare first and final frames with a pixel diff;
- inspect the whole cycle frame by frame;
- review at 0.25× and 0.5× speed;
- test every target size, theme, and device-pixel ratio;
- test hidden-tab, hover/pause, unmount, and repeat behavior;
- test initial load with a busy main thread;
- test `prefers-reduced-motion` before mount and when changed at runtime;
- inspect for dropped frames and expensive paint/filter work;
- confirm the logo never flashes unloaded content;
- confirm no visual size pop occurs at the cycle seam.

Unit tests should cover scheduling and lifecycle. Browser tests or recorded
frames must cover visual choreography; timer tests alone cannot prove motion
quality.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| A concept that would work for any logo | Derive it from this logo's geometry and negative space |
| Three parameter presets presented as three concepts | Three different choreographies, or say there are fewer |
| Production integration before the selection gates | Both gates are required; the user owns the creative choice |
| Sub-300ms UI budget applied to an ambient loop | Ambient sequences follow `motion-principles.md` §9 |
| `ease-in` used to delay a user-triggered replay | `ease-in` is only for autonomous wind-up |
| Incoming layer restarts from zero mid-swap | Preserve forward velocity across the handoff |
| Loop seam pops or flashes | Final frame must equal the first, exactly |
| Concept verified only at 128px | Render and inspect at every real target size |
| rAF loop driving a predetermined timeline | CSS or WAAPI, so it survives page load |
| Reduced motion removes a state signal silently | Keep the static logo; signal state non-spatially |
| Every animated layer announces itself | One stable accessible name, or `aria-hidden` on decorative duplicates |
| Duplicate SVG filter/mask IDs across instances | Namespace the IDs per instance |
| Cycle keeps running in a hidden tab | Defer future cycles on `visibilitychange` |

## Required deliverables

End with:

1. brief and confirmed decisions;
2. logo-anatomy table;
3. concept comparison, including rejected ideas;
4. selected motion specification;
5. isolated prototype location;
6. implementation notes and source files;
7. verification evidence and remaining uncertainties.
