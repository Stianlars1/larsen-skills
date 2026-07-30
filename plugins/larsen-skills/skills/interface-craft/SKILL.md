---
name: interface-craft
description: >-
  Plan, build, or refine a web interface from product intent through verified
  implementation, applying exact rules for layout, typography, color, surfaces,
  copy, accessibility, and motion. Use when the user asks to create a screen,
  component, flow, landing page, dashboard, or substantial UI improvement and
  expects working code. Do not use for a read-only critique, a motion-only task,
  or choosing a single UI primitive. Triggers on build a component, create a
  page, implement this design, improve this UI, "make this look better", design
  system, landing page, dashboard, form, modal, polish this screen.
license: MIT
---

# Interface Craft

Build an interface whose hierarchy, behavior, visual system, content, and motion
support one coherent product job.

Craft is not a final pass. Every layer below constrains the ones after it, so a
polish decision cannot repair a structural one.

## Quick reference

| Need | Read |
| --- | --- |
| Product job, hierarchy, restraint, rule ownership, working order | `references/interface-principles.md` |
| Semantics, keyboard, focus, names, forms, hit areas, zoom | `references/accessibility-contract.md` |
| Grouping, alignment, spacing, breakpoints, logical properties | `references/layout-structure.md` |
| Labels, errors, empty states, voice and tone | `references/interface-copy.md` |
| Type scale, leading, measure, wrapping, numbers, fonts | `references/typography.md` |
| OKLCH, palettes, contrast thresholds, gamut, appearances | `references/color-and-contrast.md` |
| Radius, optical alignment, elevation, materials, gradients, icons | `references/surfaces-and-depth.md` |
| Whether to animate, easing, duration, interruptibility | `references/motion-principles.md` |
| Drag, swipe, velocity, boundaries, keyboard parity | `references/gesture-physics.md` |
| Evidence boundaries, verification environments, feel checks | `references/evidence-and-verification.md` |

Read the references that own the decisions in scope **before** writing code.
Copy exact values from them; never approximate.

## Working contract

This is an implementation skill. It authorizes in-scope local changes when the
user's request asks to build or change the interface. It does **not** authorize
deployment, publication, package purchases, broad dependency replacement, or
unrelated cleanup.

**Preserve the project's existing system.** Match its styling approach (Tailwind,
plain CSS, CSS Modules, CSS-in-JS), its tokens, its component library, its
density, and its motion language. Never introduce a second styling approach, a
second color notation, or a second animation library to satisfy a rule from this
collection. Extend the project's system instead.

Preserve repository instructions, unrelated user changes, and product constraints
unless the user explicitly wants them replaced.

## 1. Establish the product brief

Discover from the request and the repository:

- primary user and job;
- entry point and desired completion;
- primary and secondary actions;
- content hierarchy and real data shapes;
- required loading, empty, error, partial, success, disabled, and permission
  states;
- **how often the user encounters this surface** — this decides the motion
  budget, the polish budget, and how much attention any element may spend;
- responsive, theme, localization, accessibility, and browser constraints;
- existing components, tokens, dependencies, and implementation conventions;
- acceptance criteria and the verification environment.

Ask only for material decisions that cannot be discovered. If several visual or
interaction directions would produce genuinely different products, describe the
options and stop for the user's choice.

## 2. Audit the current surface

When modifying an existing interface:

1. inspect the relevant source and nearby reusable components;
2. run or open the smallest relevant surface when possible;
3. capture current behavior across representative states;
4. identify what must remain unchanged;
5. separate observed defects from preferences and unverified assumptions.

**Do not redesign because the current implementation differs from personal
taste.** A deliberate, documented project convention is not a defect.

## 3. Write a compact interface spec

Before code:

```markdown
## Product job
## Frequency tier
## Information and action hierarchy
## Component and state model
## Responsive composition
## Interaction and focus behavior
## Visual roles and tokens
## Motion purpose (or: why nothing animates)
## Accessibility contract
## Acceptance checks
```

For a small, well-specified component this can be a short working note. For a
large flow, make the decisions explicit and reviewable.

## 4. Choose the implementation shape

- Reuse semantic native elements and existing primitives first.
- Keep data, state, presentation, and motion responsibilities understandable.
- Prefer composition over one large prop-driven component.
- Avoid introducing a library for a capability the current stack already handles.
- If a primitive choice is genuinely unresolved, use `ui-primitive-picker`.
- If the direction needs exploration, use `prototype-lab` before production
  integration.
- If motion is the main unknown, use `motion-craft`.

Default to the project's existing framework. For React and Next.js, preserve
server and client boundaries, avoid unnecessary client components, and use the
installed motion solution rather than adding another by habit.

## 5. Build in dependency order

Later layers must not compensate for an unresolved earlier one.

1. **Semantic structure and content** — real elements, real copy, meaningful
   reading order.
2. **State and data behavior** — every state in the spec, including the ugly ones.
3. **Layout and responsive recomposition** — grouping by space, shared alignment
   edges, logical properties, container queries where the component adapts to its
   column.
4. **Typography, color roles, and controls** — the type scale, role tokens, and
   controls that look interactive.
5. **Focus, keyboard, announcements, and recovery** — `:focus-visible`, full
   keyboard paths, accessible names, live regions, error recovery.
6. **Motion and micro-interactions** — only after passing the frequency and
   purpose gates.
7. **Visual polish and atmosphere** — radius, elevation, materials, gradients.

Keep changes scoped. Re-inspect the diff after each meaningful layer so later
polish does not hide a behavioral regression.

## Non-negotiables while building

These are the defaults an agent gets wrong most often. Each has full context in
its owning reference.

| Decision | Rule |
| --- | --- |
| Nested rounded surfaces | `outerRadius = innerRadius + padding` |
| Press feedback | `scale(0.96)` on `:active`, 100–160ms `ease-out` |
| Entrance scale | Never `scale(0)`; enter from `0.90–0.97` + opacity |
| Trigger-anchored surfaces | `transform-origin: var(--transform-origin)`; modals stay centered |
| Easing on entrances and exits | `ease-out`, never `ease-in` |
| UI duration | Under 300ms |
| Animated properties | `transform` and `opacity` only; never `transition: all` |
| Rapidly triggered motion | CSS transitions or springs, never keyframes |
| Group gaps | Between groups ≥ 2× within a group |
| Body measure | 60–75 characters |
| Line-height on 3+ wrapped lines | At least `1.4` |
| Changing numeric values | `font-variant-numeric: tabular-nums` |
| Mobile input font size | `16px` — never block zoom to work around it |
| Focus | Style `:focus-visible`; never `outline: none` without a verified replacement |
| Touch targets | 24×24px floor, 44×44px recommended, hit areas never overlap |
| Submit buttons | Stay enabled; validate on submit and focus the first error |
| Status | Never color alone — add an icon, label, or underline |
| Elevation | Layered transparent shadows for depth; keep borders for structure |
| Image outlines | Pure black or pure white at 10%, never a tinted near-black |
| Gradient fades | Fade to the same color at `/ 0`, never to `transparent` |
| Icon stroke | Match adjacent text weight — `1.5px` beside 400, `2px` beside 600 |
| Button labels | Verb-first; confirmations repeat the consequence |
| Motion | Gated behind frequency and purpose before anything else |

## 6. Verify

Use the project's available checks and the actual running interface where
possible.

At minimum:

- initial and material edge states;
- real content lengths, including the longest supported locale;
- narrow and wide layouts, plus 200% zoom and 320px reflow;
- light and dark themes when supported, with contrast measured in both;
- keyboard order, visible focus, control names, and focus restoration;
- reduced motion at load and toggled at runtime;
- repeated and interrupted interactions;
- console errors, layout shifts, and avoidable animation cost;
- type checking, linting, and focused tests.

When motion is in scope, add the feel check: replay at 10% speed and confirm
easing, origin, and property sync.

**If browser or runtime proof is unavailable, say so.** Static source inspection
is not a visual pass.

## Handoff

Lead with the outcome. Include:

- what changed and why;
- decisions the user approved;
- files changed;
- checks run and their results;
- known gaps and environments not verified;
- the smallest useful next decision, if one remains.
