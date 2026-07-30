---
name: ui-primitive-picker
description: >-
  Select one appropriate native element, existing project primitive, headless
  component, or UI library for a specific interface need, after inspecting the
  real stack and current authoritative documentation. Use when the user asks
  which component or library to use. Do not use for broad design-system
  selection or for silently installing a dependency. Triggers on which library,
  which component, should I use, headless UI, dialog library, toast library,
  drag and drop, virtualization, date picker, combobox, "build or buy".
license: MIT
---

# UI Primitive Picker

Choose the smallest dependable primitive that satisfies the actual interaction
contract. **Return one recommendation, not an unranked catalog.**

The two failure modes this skill exists to prevent are hand-rolling a component
whose accessibility contract is genuinely hard (dialogs, comboboxes, toasts,
virtualization), and installing a dependency for something the platform or the
current stack already does.

## Quick reference

| Need | Read |
| --- | --- |
| Semantics, keyboard patterns, focus management, names, forms | `references/accessibility-contract.md` |
| Product job, rule ownership, restraint | `references/interface-principles.md` |
| Exit presence, interruptibility, motion library selection | `references/motion-principles.md` |
| Drag, swipe, velocity, gesture recognition | `references/gesture-physics.md` |
| Evidence boundaries and verification | `references/evidence-and-verification.md` |

## Scope

This is a research and recommendation skill by default. It does **not** authorize
package installation, code changes, migration, or removal of an existing
dependency unless the user explicitly asks for implementation.

**Component libraries, versions, browser APIs, and maintenance status change.**
Verify current claims against official documentation and the package's primary
repository, and record the access date. Do not rely on a remembered library list
— a recommendation from memory is the most common way this skill goes wrong.

## Inspect the project first

Establish:

- framework and exact relevant versions;
- current component system and package manager;
- **existing primitives that already solve part or all of the need**;
- styling and token approach;
- server/client, bundle, and rendering constraints;
- accessibility and interaction requirements;
- target browsers and devices;
- appetite for a new dependency, and who will own it.

**Inspect lockfiles and actual imports.** A package listed in a manifest is not
proof the project uses it for the target surface. If a competitor of the obvious
recommendation is already installed, flag the mismatch — do not churn the
dependency without being asked.

## Define the primitive contract

Describe, before naming any candidate:

- semantic role;
- controlled and uncontrolled state needs;
- **keyboard interaction and focus management** — name the ARIA APG pattern this
  widget promises;
- pointer, touch, drag, or gesture behavior;
- layering, portal, collision, scroll, and positioning needs;
- form integration;
- animation and exit-presence requirements;
- composability and styling requirements;
- localization, right-to-left, and responsive concerns;
- testability.

**Do not select a library before this contract is explicit.** Most bad picks are
contracts that were never written down.

## Evaluate in dependency order

Stop at the first level that satisfies the contract.

1. **A correct native HTML element.** `<dialog>` with `showModal()` supplies the
   focus trap, inert background, and Escape handling; `<details>` supplies
   disclosure; `<select>` supplies a listbox. The platform is the cheapest
   dependency you will ever have.
2. **An existing project primitive.**
3. **A small framework or platform primitive already installed.**
4. **A focused headless component** that owns behavior and leaves styling to you.
5. **A broader UI library**, only when the product needs its system.

For credible candidates, verify:

- official compatibility with the project's exact versions;
- **accessibility model and documented keyboard behavior** — against the APG
  pattern named in the contract, not the marketing copy;
- maintenance and release activity;
- bundle and runtime implications;
- styling ownership and design-system fit;
- composition limits and escape hatches;
- test strategy;
- migration and removal cost;
- license.

Reject candidates that duplicate the current stack, force a conflicting style
system, hide required behavior behind an unreachable API, or carry an
unacceptable maintenance boundary.

## Where hand-rolling is usually wrong

These contracts are harder than they look. A hand-rolled version almost always
ships without the focus, dismissal, or virtualization behavior users expect:

- modal dialogs, popovers, menus, comboboxes — focus trapping, dismissal
  layering, collision positioning;
- toasts — stacking, timer pausing, swipe dismissal, live-region announcement;
- drag and drop, reordering — pointer capture, keyboard parity, auto-scroll;
- long lists and large tables — virtualization;
- one-time-code inputs — paste handling, autofill, per-character focus;
- date and time pickers — locale, calendar keyboard model, timezone.

Conversely, a hover state, a fade, a simple accordion, or a conditional render
does not need a library. Plain CSS is the right tool there.

## Return one decision

```markdown
# Recommendation

## Choose
One primitive, with its exact source or package and version.

## Why it fits
Evidence tied to the contract and the inspected stack.

## Why not the alternatives
Only the strongest rejected candidates, each with the decisive reason.

## Integration shape
Component boundary, state ownership, styling, accessibility, and tests.

## Risks
Version, maintenance, bundle, API, or migration concerns.

## Verification sources
Official documentation, primary repository, inspected local files, access date.
```

If no candidate satisfies the contract, **recommend a small local primitive and
define its responsibility** rather than choosing the least unsuitable library.

## Implementation gate

Ask for approval before adding a dependency when the request was only to choose.
If implementation is authorized, use the project's package manager, make the
smallest integration, and verify behavior against the primitive contract —
especially the keyboard model.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Recommending from memory | Verify against current official documentation; record the date |
| Naming a library before writing the contract | Contract first, always |
| Manifest treated as proof of use | Inspect lockfiles and actual imports |
| Skipping the native element | `<dialog>`, `<details>`, `<select>` first |
| Hand-rolling a dialog or combobox | Use a primitive that owns the APG keyboard model |
| Installing a library for a fade | Plain CSS |
| Presenting an unranked menu of options | One recommendation, with rejected alternatives named |
| Churning an installed competitor | Flag the mismatch; do not swap unasked |
| Installing without approval | The implementation gate is required |
| Accessibility claimed from marketing copy | Verify the documented keyboard behavior |
