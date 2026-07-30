---
name: motion-vocabulary
description: >-
  Turn a vague description of a web interface motion or material effect into its
  exact term, so the user can ask for it precisely. Use when the user asks
  "what's it called when…", describes an effect they cannot name, or needs the
  right word to brief a designer or another agent. This skill names effects; it
  does not design, specify, or build them. Triggers on what is it called, what's
  the name for, the effect where, "that thing where it", name this animation,
  motion terminology, animation glossary.
license: MIT
---

# Motion Vocabulary

Name the effect. A precise term is the difference between a brief another agent
can execute and one it has to guess at.

This skill is a lookup, not a design tool. Once the effect has a name, hand off:
`motion-craft` to specify or review it, `reverse-engineer-motion` to reconstruct
it from a recording, `prototype-lab` to compare directions.

## How to answer

1. **Read for the sensation, not the keywords.** People describe what they see
   and feel — "springy", "it peels away", "it draws itself in" — not the
   technical name. Map the sensation to the glossary.
2. **Lead with the term.** One bold name, one sentence of definition. A naming
   question wants a name, not an essay.
3. **Disambiguate close neighbours.** When two terms compete, give the best match
   first, then one or two alternates with the single distinction that separates
   them.
4. **Say when nothing matches.** Name the closest term and call it an
   approximation, or describe the effect as a composite in this vocabulary —
   "that is a *stagger* of *scale-in* entrances". Do not invent a term.
5. **Add the rule only when it changes the ask.** If the named effect is one this
   collection restricts — anything gated by frequency, or `ease-in` on UI — say so
   in one line so the user does not brief something they should not ship.

Answer format:

```text
**Term** — one-sentence definition.

Close alternates:
- **Other term** — the one distinction that separates it.
```

## Glossary

### Entrances and exits

- **Fade in / fade out** — appears or disappears by opacity alone.
- **Slide in** — enters by translating from off-screen along one axis.
- **Scale in** — grows from smaller to full size, usually paired with a fade.
- **Pop in** — appears with a slight overshoot, as if bouncing into place.
- **Reveal** — uncovered progressively, typically by animating a `clip-path` or
  mask rather than by moving the element.
- **Materialize** — a translucent surface arrives by animating blur and scale
  together, so it reads as a material rather than an opacity fade.
- **Enter / exit** — the animation an element plays when it is added to or
  removed from the tree.

### Sequencing and timing

- **Keyframes** — defined points in a timeline that the browser interpolates
  between.
- **Interpolation / tween** — generating the in-between values so motion is
  continuous.
- **Stagger** — animating several items one after another with a small delay,
  producing a cascade.
- **Orchestration** — timing several animations so they read as one coordinated
  motion.
- **Delay** — time before an animation starts.
- **Duration** — how long an animation takes.
- **Dwell** — deliberate stillness inside a loop, so the resting state is
  readable between transitions.
- **Fill mode** — whether an element keeps its first or last frame's styles
  outside the animation's active period.
- **Stepped animation** — motion divided into discrete jumps rather than
  continuous interpolation, like a ticking second hand.

### Movement and transforms

- **Translate** — move along an axis.
- **Scale** — resize. Note that `scale()` also scales an element's children.
- **Rotate** — spin around a point.
- **Skew** — shear out of the rectangular grid along an axis.
- **3D tilt / flip** — rotate in three dimensions (`rotateX`, `rotateY`) for
  depth.
- **Perspective** — how strongly the 3D effect reads; a lower value exaggerates
  depth.
- **Transform origin** — the anchor point a scale or rotation acts from.
- **Origin-aware animation** — an element animates out of its trigger rather than
  its own centre, so a popover appears to grow from the button that opened it.

### Transitions between states

- **Crossfade** — one element fades out as another fades in, in the same place.
- **Continuity transition** — a change that keeps the user oriented by visually
  connecting before and after.
- **Morph** — one shape smoothly becomes another shape.
- **Shared element transition** — an element travels and transforms from one
  position into another, like a thumbnail expanding into a detail view.
- **Layout animation** — when an element's size or position changes, it animates
  to the new geometry instead of snapping. Usually implemented with FLIP.
- **FLIP** — First, Last, Invert, Play: measure both states, apply an inverting
  transform, then animate it away. The technique underneath most layout
  animations.
- **View transition** — the browser itself morphs between two document states,
  connecting elements it can pair.
- **Accordion / collapse** — a section expands and collapses its height to show
  or hide content.
- **Direction-aware transition** — content slides one way going forward and the
  other going back, so navigation carries a sense of direction.

### Scroll

- **Scroll reveal** — elements animate in as they enter the viewport.
- **Scroll-driven animation** — progress tied directly to scroll position rather
  than to time.
- **Parallax** — foreground and background move at different rates, implying
  depth.
- **Sticky / pinned section** — an element holds position while content scrolls
  past it.
- **Scroll snap** — scrolling settles on defined points rather than anywhere.
- **Scroll edge effect** — a blur or gradient mask where content meets floating
  chrome, replacing a hard divider.
- **Page transition** — an animation when navigating between routes.

### Feedback and interaction

- **Hover effect** — a visual change while the pointer is over an element.
- **Press feedback** — a subtle scale-down on press, so the control feels
  physical.
- **Hold to confirm** — a progress fill while a button is held, guarding a
  destructive action.
- **Drag** — moving an element by grabbing it, usually with momentum on release.
- **Drag to reorder** — dragging items in a list while the others shift to make
  room.
- **Swipe to dismiss** — dragging an element off-screen to close it.
- **Rubber-banding** — progressive resistance and snap-back when dragging past a
  boundary.
- **Momentum projection** — using release velocity to predict where a flick was
  going, then snapping to the nearest target from *there*.
- **Velocity handoff** — starting the post-gesture animation at the finger's exact
  release velocity, so there is no seam between dragging and animating.
- **Hysteresis** — a small movement threshold before a gesture commits to a
  direction.
- **Shake / wiggle** — a quick lateral jitter signalling rejected input.
- **Ripple** — a circle expanding from the point of contact.

### Easing

- **Easing** — how speed changes across an animation.
- **Ease-out** — starts fast, ends slow. The default for UI and anything
  responding to the user.
- **Ease-in** — starts slow, ends fast. Avoided on UI; it delays the moment the
  user is watching.
- **Ease-in-out** — slow, fast, slow. For elements already on screen moving
  between poses.
- **Linear** — constant speed. Reserved for spinners, marquees, and scrubbing.
- **Cubic-bezier** — a custom curve defined by two control points.
- **Asymmetric easing** — accelerating and decelerating at different rates; reads
  as more alive than a symmetric curve.
- **Asymmetric timing** — a different *duration* for each direction: slow where
  the user is deciding, fast where the system responds.

### Springs and physics

- **Spring** — motion driven by physics rather than a fixed duration.
- **Stiffness / tension** — how strongly the spring pulls toward its target;
  higher is snappier.
- **Damping** — how quickly it settles; lower means more oscillation.
- **Damping ratio** — the normalized form: `1.0` is critically damped with no
  overshoot, below `1.0` overshoots.
- **Response** — how quickly the value reaches its target, in seconds. Not the
  same as duration; a spring has no fixed end.
- **Mass** — how heavy the element feels; more mass is slower and more sluggish.
- **Bounce** — overshoot before settling.
- **Perceptual duration** — how long a spring *feels* finished, while it is still
  micro-settling underneath.
- **Momentum** — motion carrying velocity, especially after a drag.
- **Interruptible animation** — one that can be redirected mid-flight instead of
  finishing first.
- **Additive animation** — blending a new animation onto the current one so
  velocity carries through a reversal instead of hard-cutting.
- **Presentation value** — the value currently on screen, as distinct from the
  logical target. Interruptions must start from it.

### Looping and ambient motion

- **Marquee** — content scrolling continuously in a loop.
- **Loop** — an animation that repeats.
- **Alternate (yoyo)** — a loop that reverses each iteration instead of jumping
  back to the start.
- **Orbit** — one element circling another on a continuous path.
- **Pulse** — a gentle repeating scale or opacity change that draws attention.
- **Float** — a slow continuous drift that makes a static element feel alive.
- **Idle animation** — subtle motion while an element waits to be used.
- **Loop seam** — the join between the last and first frame of a cycle. A visible
  seam is the usual cause of a "jumpy" loop.

### Material and effects

- **Blur** — softens an element, or bridges two states during a crossfade.
- **Clip-path** — clips an element to a shape; the standard tool for reveals,
  wipes, and comparison sliders.
- **Mask** — like clip-path, but with soft, fadeable edges.
- **Metaball / gooey effect** — nearby rounded shapes visually merging into one
  continuous silhouette.
- **Signed distance field (SDF)** — representing shapes as distance functions so
  they can be blended mathematically; how a metaball merge is usually computed.
- **Smooth union** — the blend function that merges two distance fields into one
  rounded silhouette instead of a hard intersection.
- **Marching squares** — extracting a contour line from a sampled scalar field;
  how an SDF becomes a renderable path.
- **Backdrop blur** — blurring whatever sits behind a translucent surface.
- **Vibrancy** — adjusting foreground text over a translucent surface so it stays
  legible against changing content.
- **Line drawing** — an SVG path that draws itself in, as if traced.
- **Text morph** — text animating character by character as it changes.
- **Number ticker** — digits rolling or counting toward a value.
- **Skeleton / shimmer** — a placeholder with a travelling sheen shown while
  content loads.
- **Typewriter** — text appearing one character at a time.
- **Before/after slider** — a draggable divider wiping between two overlaid
  images.

### Performance

- **Frame rate (FPS)** — frames drawn per second; 60 is the baseline, 120 on
  newer displays.
- **Jank** — visible stutter when the browser misses frame deadlines.
- **Dropped frame** — a single missed frame deadline.
- **Compositing** — letting the GPU move or fade an element on its own layer
  without redoing layout or paint.
- **Layout thrashing** — interleaving reads and writes, or animating layout
  properties, so the browser recalculates every frame.
- **will-change** — a hint that an element is about to animate, so the browser can
  promote it to its own layer in advance.

### Principles

- **Purposeful animation** — motion that orients, gives feedback, or shows a
  relationship, rather than decorating.
- **Frequency of use** — the more often an animation is seen, the shorter and
  subtler it must be, until at high enough frequency it should not exist.
- **Anticipation** — a small wind-up opposite the coming motion.
- **Follow-through** — secondary parts settling after the main mass stops.
- **Squash and stretch** — deforming to convey weight and speed.
- **Perceived performance** — the right motion making an interface feel faster
  than it measurably is.
- **Spatial consistency** — an element keeping its identity and place across
  states, so users never lose track of where things went.
- **Reduced motion** — honoring the user's preference with a gentler variant, not
  an absent one.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Answering with an essay | Lead with the term; expand only if asked |
| Inventing a term that sounds plausible | Name the closest match and say it is an approximation |
| One term offered where two genuinely compete | Give both, with the single distinction between them |
| Naming an effect this collection restricts, silently | Add one line on the rule so the brief is not wrong from the start |
| Paraphrasing the definition loosely | Keep definitions stable, so briefs stay consistent between sessions |
| Designing the animation instead of naming it | Hand off to `motion-craft` |
