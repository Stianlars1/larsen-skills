---
name: ui-primitive-picker
description: >-
  Select one appropriate native element, existing project primitive, headless
  component, or UI library solution for a specific interface need after
  inspecting the real stack and current authoritative documentation. Use when
  the user asks which component or library to use. Do not use for broad design
  system selection or silently installing a dependency.
license: MIT
---

# UI Primitive Picker

Choose the smallest dependable primitive that satisfies the actual interaction
contract. Return one recommendation, not an unranked catalog.

Read before acting:

- `../../references/interface-principles.md`
- `../../references/evidence-and-verification.md`

## Scope

This is a research and recommendation skill by default. It does not authorize
package installation, code changes, migration, or removal of an existing
dependency unless the user explicitly asks for implementation.

Component libraries, versions, browser APIs, and maintenance status change.
Verify current claims with official documentation and the package's primary
repository. Do not rely on a remembered library list.

## Inspect the project first

Establish:

- framework and exact relevant versions;
- current component system and package manager;
- existing primitives that solve part or all of the need;
- styling and token approach;
- server/client, bundle, and rendering constraints;
- accessibility and interaction requirements;
- target browsers and devices;
- appetite for a new dependency and ownership cost.

Inspect lockfiles and actual imports. A package listed in a manifest is not proof
that the project uses it for the target surface.

## Define the primitive contract

Describe:

- semantic role;
- controlled and uncontrolled state needs;
- keyboard interaction and focus management;
- pointer, touch, drag, or gesture behavior;
- layering, portal, collision, scroll, and positioning needs;
- form integration;
- animation and exit-presence requirements;
- composability and styling requirements;
- localization, right-to-left, and responsive concerns;
- testability.

Do not select a library before this contract is explicit.

## Evaluate in dependency order

Consider:

1. a correct native HTML element;
2. an existing project primitive;
3. a small framework or platform primitive already installed;
4. a focused headless component;
5. a broader UI library only when the product needs its system.

For credible candidates, verify:

- official compatibility with the project's versions;
- accessibility model and documented keyboard behavior;
- maintenance and release activity;
- bundle and runtime implications;
- styling ownership and design-system fit;
- composition limits and escape hatches;
- test strategy;
- migration and removal cost;
- license.

Reject candidates that duplicate the current stack, force a conflicting style
system, hide required behavior, or have an unacceptable maintenance boundary.

## Return one decision

Use:

```markdown
# Recommendation

## Choose
One primitive and exact source/package.

## Why it fits
Evidence tied to the contract and inspected stack.

## Why not the alternatives
Only the strongest rejected candidates and the decisive reason.

## Integration shape
Component boundary, state ownership, styling, accessibility, and tests.

## Risks
Version, maintenance, bundle, API, or migration concerns.

## Verification sources
Official documentation, primary repository, inspected local files, and access
date.
```

If no candidate satisfies the contract, recommend a small local primitive and
define its responsibility rather than choosing the least unsuitable library.

## Implementation gate

Ask for approval before adding a new dependency when the user's request was only
to choose. If implementation is authorized, use the project's package manager,
make the smallest integration, and verify behavior against the primitive
contract.
