---
name: interface-review
description: >-
  Evidence-based, read-only review of a web interface across product clarity,
  layout, typography, color and contrast, copy, accessibility, surfaces, motion,
  responsiveness, and implementation risk. Coordinates every domain rule in this
  collection into one prioritized verdict. Use for UI or UX audits, design
  critiques, polish reviews, and pre-release interface checks. Do not edit code
  unless the user separately asks for implementation. Triggers on interface
  review, UI audit, UX review, design critique, accessibility audit, polish
  review, "review this screen", "what's wrong with this UI", holistic design
  review.
license: MIT
---

# Interface Review

Review what the interface actually does. Do not invent findings to fill a
checklist, and do not turn preferences into defects.

A strong review is not eleven independent audits stapled together. Let each
domain reference own its rules, then consolidate the evidence into one ranked
verdict.

## Quick reference

| Domain | Read |
| --- | --- |
| Severity, evidence, consolidation, output format, verdict | `references/review-protocol.md` |
| Product job, hierarchy, restraint, rule ownership | `references/interface-principles.md` |
| Semantics, keyboard, focus, names, forms, hit areas, zoom | `references/accessibility-contract.md` |
| Grouping, alignment, spacing, responsive structure, RTL | `references/layout-structure.md` |
| Labels, errors, empty states, voice and tone | `references/interface-copy.md` |
| Type scale, leading, measure, wrapping, numbers | `references/typography.md` |
| OKLCH, palettes, APCA and WCAG thresholds, gamut | `references/color-and-contrast.md` |
| Radius, optical alignment, elevation, materials, gradients, icons | `references/surfaces-and-depth.md` |
| Frequency gate, easing, duration, interruptibility, performance | `references/motion-principles.md` |
| Drag, swipe, velocity, momentum, boundaries | `references/gesture-physics.md` |
| Evidence boundaries and feel-checking | `references/evidence-and-verification.md` |

**Cite exact values from the owning reference.** Never approximate a curve, a
duration, a contrast threshold, or a target size.

## Scope contract

A review is **read-only**. Inspecting source, tests, assets, screenshots, and an
authorized local or live surface is allowed. Do not change code, install
packages, publish findings externally, or deploy a fix without a separate
request.

| Mode | Coverage | Finding cap |
| --- | --- | --- |
| `quick` | Primary journey and highest-traffic states; `HIGH` and `MEDIUM` only | 5 |
| `full` | Entire scope, including empty, loading, error, and narrow-width states | 15 |

Default to `full` unless the user asks for a quick review. If the scope is too
large to inspect credibly, narrow it to the highest-traffic complete flow and
**state the boundary**. Never imply uninspected surfaces were reviewed.

Establish before judging:

- the screen, feature, or journey in scope;
- the intended user and product job;
- **how often the user encounters this surface**;
- the environment to inspect;
- authenticated or destructive flows that must not be exercised;
- target devices, browsers, themes, and locales;
- whether the review is visual, functional, or both.

## Recon before judgment

Identify the framework, styling system, component library, design tokens,
supported viewports, and available preview or test commands. Follow the project's
established conventions.

**A rule violated in service of a documented, deliberate project decision is not
a finding.** Note it and move on.

## Review order

Walk the domains in this order so foundational failures are not hidden by polish.
Assign each finding to the domain that owns the underlying rule and report it
once; name secondary effects in the **Why** cell.

1. **Accessibility** — semantics, keyboard, focus, names, forms, hit areas, zoom
2. **Layout** — grouping, alignment, reading order, responsive structure
3. **Copy** — labels, errors, empty states, terminology
4. **Typography** — scale, hierarchy, leading, measure, wrapping, numbers
5. **Color** — role tokens, measured contrast, gamut, both appearances
6. **Surfaces** — radius, optical alignment, elevation, materials, icons
7. **Motion** — frequency, purpose, easing, duration, interruptibility
8. **Gesture** — direct manipulation, velocity, boundaries, keyboard parity
9. **Product and content** — is the job understandable, is the primary action
   correctly prioritized, are irreversible choices explicit
10. **Implementation risk** — state handling, error recovery, performance cost

In `quick` mode, inspect every domain but spend depth only where the primary flow
has evidence.

## Evidence collection

Inspect the smallest evidence set that can prove the behavior:

1. repository instructions and relevant source;
2. current component and token systems;
3. the running surface at representative sizes;
4. keyboard and focus behavior;
5. reduced-motion behavior;
6. material loading, empty, error, success, and interrupted states;
7. existing tests and documented constraints.

Label every claim **observed**, **inferred**, or **unknown**, and record where and
how each observed issue was reproduced.

**Do not report a code-level finding from appearance alone, or a visual finding
from source alone, when runtime behavior decides the result.** Static source
inspection is not a visual pass.

When motion is in scope, replay it at 10% speed and walk every state — hover,
focus, active, loading, empty. What is wrong at 10% speed is subtly wrong at full
speed.

## Highest-yield checks

Run these first; they account for most real findings.

**Accessibility**

- `outline: none` with no verified replacement
- `<div onClick>` where a `<button>` or `<a href>` belongs
- icon-only controls with no accessible name
- placeholder used as the only label
- submit disabled until the form is valid
- error signalled by border color alone
- targets below the 24×24px floor with no applicable exception

**Layout and typography**

- gap between groups less than 2× the gap within a group
- separator lines doing work that spacing should do
- physical `margin-left` / `padding-right` in a localizable layout
- paragraphs with no measure cap
- `line-height` under `1.4` on text wrapping to three or more lines
- changing numbers without `tabular-nums`
- inputs below `16px` on mobile

**Color and surfaces**

- raw color values bypassing the token system
- a semantic token used outside its role
- contrast verified only in light mode
- equal radii on closely nested surfaces
- borders used purely to fake elevation
- image outlines in a tinted near-black instead of pure black or white

**Motion**

- animation on a keyboard-initiated or 100+/day action
- `ease-in` on UI, `transition: all`, or `scale(0)`
- `transform-origin: center` on a trigger-anchored popover (modals are exempt)
- keyframes on rapidly triggered elements
- movement with no `prefers-reduced-motion` handling

## Consolidate and show restraint

One root cause is one finding; list every confirmed location in the same row. Do
not pad to reach the cap — a short review, or none at all, is a valid result.

**A considered-but-rejected section is required**: 1–3 candidates in `quick`, 2–5
in `full`, each with the reason it was not reported. These must be real
candidates encountered during the review.

Avoid prescribing a redesign when a smaller correction addresses the cause.

## Output

Use `references/review-protocol.md` §8:

1. **Scope and coverage** — mode, exact scope, stack and conventions, boundary,
   and a per-domain coverage table where `Clear` means inspected with no finding
   and `Not reviewed` explains why.
2. **Findings** — one table ordered by severity, then reach and leverage:

   | # | Severity | Domain | Location | Before | After | Why |
   | --- | --- | --- | --- | --- | --- | --- |

3. **Considered but rejected.**
4. **Strengths worth preserving.**
5. **Verification** — each check, the exact command or steps, and the observed
   result; anything unrun marked **Not verified**.
6. **Verdict** — exactly one of `Block` (a `HIGH` remains), `Needs changes` (only
   `MEDIUM`/`LOW` remain), or `Approve` (nothing actionable remains and claimed
   coverage was verified).

Then provide a prioritized, self-contained implementation plan. **A review does
not authorize edits** — do not write the fixes until the user asks.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Domain reports stapled together | One ranked, consolidated findings table |
| The same issue reported by two domains | Assign it to the owner; report once |
| Finding with no exact location | Cite `path/to/file:line` and the current code |
| Visual claim inferred only from source | Inspect the rendered state, or mark it not verified |
| Verification gap presented as a finding | Label it **Not verified** |
| Unlimited low-impact polish | Respect the cap; omit `LOW` in `quick` |
| Silent coverage gaps | Show which domains and states were inspected |
| No rejected candidates | The section is required |
| Preference reported as a defect | Name the violated rule, or drop it |
| Deliberate project convention flagged | Note it; do not report it |
| Review silently edits code | Stay read-only unless implementation was requested |
| `Approve` with pending actionable findings | `Needs changes` or `Block` |
