---
name: motion-craft
description: >-
  Find, specify, review, or improve motion in a web interface using explicit
  purpose, frequency, choreography, easing, interruption, accessibility, and
  performance rules. Use when the main task is animation or interaction motion.
  Supports brief, opportunities, review, and improve modes. Do not use for
  reverse engineering a reference video or an animated logo identity.
license: MIT
---

# Motion Craft

Motion must clarify change, provide feedback, preserve continuity, or express a
deliberate product character. Motion without a defined job is a candidate for
removal.

Read before acting:

- `../../references/motion-principles.md`
- `../../references/interface-principles.md`
- `../../references/evidence-and-verification.md`

## Select one mode

- `brief`: turn an idea into an exact motion specification.
- `opportunities`: find places that genuinely benefit from motion and explicitly
  identify what should remain static.
- `review`: assess existing motion without changing code.
- `improve`: produce prioritized, self-contained correction plans. Implement
  only after the user selects or approves them.

If no mode is given, infer it only when the user's verb is unambiguous. Otherwise
ask which result they want.

## Shared intake

Establish:

- user task and interface state change;
- trigger, frequency, and input method;
- target elements and spatial relationship;
- desired motion character;
- current framework and installed animation tools;
- browser, device, and performance constraints;
- reduced-motion requirement;
- reference material and whether it is directional or pixel-exact.

Inspect existing motion tokens and component conventions before proposing new
ones.

## Purpose gate

For each candidate animation, complete:

```text
Purpose:
Frequency:
User benefit:
Cost or risk:
Static/reduced alternative:
Decision: keep | change | remove | prototype
```

Reject motion that delays frequent tasks, competes with content, makes position
ambiguous, repeats without value, or duplicates feedback already communicated
more clearly.

## Brief mode

Produce:

1. before and after state;
2. trigger and completion condition;
3. element hierarchy;
4. choreography phases;
5. per-property timing and easing;
6. transform origin and spatial path;
7. interruption and reversal;
8. responsive and reduced-motion variants;
9. implementation strategy;
10. verification cases.

Use numeric values as testable starting points, not universal truths. Name the
perceived quality alongside the values.

## Opportunities mode

Inspect the actual journey and return three groups:

- `high-value`: motion likely improves understanding or control;
- `prototype`: promising but needs comparison;
- `keep static`: motion would add cost, delay, noise, or accessibility risk.

Rank by product value, not spectacle. For each opportunity, include purpose,
frequency, choreography summary, implementation surface, and validation method.

## Review mode

Observe at normal speed, slow speed, repeated input, keyboard use, and reduced
motion. Inspect the controller code separately.

Review:

- purpose and frequency;
- duration, easing, delay, and stagger;
- continuity and transform origin;
- gesture thresholds and velocity;
- interruption, reversal, and cleanup;
- layout, paint, and compositing cost;
- hidden-tab, offscreen, hover, and focus behavior;
- reduced-motion behavior.

Report only proven findings, ordered by impact.

## Improve mode

For every approved issue, write a self-contained plan:

```markdown
### Motion change
- Current evidence:
- Desired behavior:
- Exact choreography:
- Files or components:
- Implementation constraints:
- Accessibility:
- Performance:
- Tests:
- Visual acceptance:
```

Do not bundle unrelated animation changes into one broad task.

## Implementation selection

Choose the smallest tool that fits:

- CSS transitions/keyframes for bounded state motion;
- Web Animations API for direct lifecycle control without a framework dependency;
- the project's existing motion library for stateful orchestration, layout
  continuity, gestures, or spring behavior;
- SVG path/mask animation when geometry requires it;
- canvas/WebGL only when the visual model cannot be expressed efficiently with
  DOM/SVG.

Do not add a second animation library to solve a local effect without an explicit
compatibility and maintenance justification.

## Verification

Test exact rest states, repeated triggers, mid-flight reversal, resize,
navigation/unmount, hidden-tab recovery, runtime motion-preference changes,
keyboard and touch, and representative performance. Report source checks,
automated tests, and visual runtime proof separately.
