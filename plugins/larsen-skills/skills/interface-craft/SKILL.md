---
name: interface-craft
description: >-
  Plan, build, or refine a web interface from product intent through verified
  implementation. Use when the user asks to create a screen, component, flow,
  landing page, dashboard, or substantial UI improvement and expects working
  code. Do not use for a read-only critique, a motion-only task, or choosing a
  single UI primitive.
license: MIT
---

# Interface Craft

Build an interface whose hierarchy, behavior, visual system, content, and motion
support one coherent product job.

Read before acting:

- `../../references/interface-principles.md`
- `../../references/visual-systems.md`
- `../../references/motion-principles.md`
- `../../references/evidence-and-verification.md`

## Working contract

This is an implementation skill. It authorizes in-scope local changes only when
the user's request asks to build or change the interface. It does not authorize
deployment, publication, package purchases, broad dependency replacement, or
unrelated cleanup.

Preserve existing design systems, repository instructions, user changes, and
product constraints unless the user explicitly wants to replace them.

## 1. Establish the product brief

Discover from the request and repository:

- primary user and job;
- entry point and desired completion;
- primary and secondary actions;
- content hierarchy and real data shapes;
- required loading, empty, error, partial, success, disabled, and permission
  states;
- responsive, theme, localization, accessibility, and browser constraints;
- existing components, tokens, dependencies, and implementation conventions;
- acceptance criteria and verification environment.

Ask only for material decisions that cannot be discovered. If several visual or
interaction directions would produce different products, describe the options
and stop for the user's choice.

## 2. Audit the current surface

When modifying an existing interface:

1. inspect the relevant source and nearby reusable components;
2. run or open the smallest relevant surface when possible;
3. capture current behavior across representative states;
4. identify what must remain unchanged;
5. separate observed defects from preferences and unverified assumptions.

Do not redesign merely because the current implementation differs from a
personal taste.

## 3. Write a compact interface spec

Before code, define:

```markdown
## Product job
## Information and action hierarchy
## Component and state model
## Responsive composition
## Interaction and focus behavior
## Visual roles and tokens
## Motion purpose
## Accessibility contract
## Acceptance checks
```

For a small, well-specified component, this can be a short working note. For a
large flow, make the decisions explicit and reviewable.

## 4. Choose the implementation shape

- Reuse semantic native elements and existing primitives first.
- Keep data, state, presentation, and motion responsibilities understandable.
- Prefer composition over a large prop-driven component.
- Avoid introducing a new library for a capability the current stack already
  handles well.
- If a primitive choice is genuinely unresolved, use `ui-primitive-picker`.
- If the direction needs exploration, use `prototype-lab` before production
  integration.
- If motion is the main unknown, use `motion-craft`.

Default to the project's existing framework. For React/Next.js, preserve server
and client boundaries, avoid unnecessary client components, and use the
installed motion solution rather than adding another by habit.

## 5. Build in dependency order

Implement:

1. semantic structure and content;
2. state and data behavior;
3. layout and responsive recomposition;
4. typography, color roles, and controls;
5. focus, keyboard, announcements, and recovery;
6. motion and micro-interactions;
7. visual polish and atmosphere.

Keep changes scoped. Reinspect the diff after each meaningful layer so later
polish does not hide a behavioral regression.

## 6. Verify

Use the project's available checks and the actual running interface where
possible.

At minimum verify:

- initial and material edge states;
- real content lengths;
- narrow and wide layouts;
- light and dark themes when supported;
- keyboard order, visible focus, and control names;
- reduced motion;
- repeated and interrupted interactions;
- console errors, layout shifts, and avoidable animation cost;
- type checking, linting, and focused tests.

If browser or runtime proof is unavailable, say so. Static source inspection is
not a visual pass.

## Handoff

Lead with the outcome. Include:

- what changed and why;
- important decisions the user approved;
- files changed;
- checks run and results;
- known gaps or environments not verified;
- the smallest useful next decision, if one remains.
