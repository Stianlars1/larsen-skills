---
name: interface-review
description: >-
  Perform an evidence-based, read-only review of a web interface across product
  clarity, layout, visual polish, interaction, content, accessibility, motion,
  responsiveness, and implementation risk. Use for UI or UX audits, design
  critiques, polish reviews, and pre-release interface checks. Do not edit code
  unless the user separately asks for implementation.
license: MIT
---

# Interface Review

Review what the interface actually does. Do not invent findings to fill a
checklist, and do not turn preferences into defects.

Read before reviewing:

- `references/interface-principles.md`
- `references/visual-systems.md`
- `references/motion-principles.md`
- `references/evidence-and-verification.md`

## Modes

- `quick`: primary journey, top risks, and highest-leverage corrections.
- `full`: representative states, breakpoints, input methods, motion preferences,
  and source/runtime evidence.

Default to `full` unless the user explicitly asks for a quick review.

## Scope contract

A review is read-only. Inspecting source, tests, assets, screenshots, and a local
or authorized live surface is allowed. Do not change code, install packages,
publish findings externally, or deploy a fix without a separate request.

Establish:

- screen, feature, or journey in scope;
- intended user and product job;
- environment to inspect;
- authenticated or destructive flows that must not be exercised;
- target devices, browsers, themes, and locales;
- whether the review is visual, functional, or both.

## Evidence collection

Inspect the smallest evidence set that can prove the behavior:

1. repository instructions and relevant source;
2. current component and token systems;
3. running surface at representative sizes;
4. keyboard and focus behavior;
5. reduced-motion behavior;
6. material loading, empty, error, success, and interrupted states;
7. existing tests and known constraints.

Label findings as observed, inferred, or unknown. Record where and how each
observed issue was reproduced.

## Review lenses

### Product and content

- Is the page's job understandable?
- Is the primary action clear and correctly prioritized?
- Does copy explain state, consequence, and recovery?
- Are irreversible or costly choices explicit?

### Structure and layout

- Does reading order match visual order?
- Are groups, alignment, spacing, density, and disclosure coherent?
- Does the interface recompose at narrow widths?
- Are real content lengths handled?

### Visual system

- Are typography, colors, gradients, radii, borders, shadows, icons, and images
  role-based and consistent?
- Is contrast preserved in every state?
- Does polish support hierarchy instead of competing with it?

### Interaction and accessibility

- Are controls semantic, named, focused, and keyboard-operable?
- Are touch targets, validation, announcements, and focus restoration sound?
- Can the flow recover from error without losing work?
- Are pointer gestures optional?

### Motion

- Does each animation have a product purpose proportional to its frequency?
- Is it interruptible, performant, and reduced-motion aware?
- Do shared objects preserve continuity?
- Does ambient motion pause and dwell appropriately?

## Findings format

Order findings by user impact, not by page position.

```markdown
### [P1–P3] Concise finding

- Evidence:
- User impact:
- Recommendation:
- Verification:
- Confidence: high | medium | low
```

- `P1`: blocks a primary task, creates a serious accessibility failure, or risks
  destructive user harm.
- `P2`: materially degrades comprehension, completion, or a common interaction.
- `P3`: meaningful polish or resilience issue with lower immediate impact.

For visual refinements, add a compact `Current / Proposed / Why` comparison.
Avoid prescribing a full redesign when a smaller correction addresses the cause.

## Report

Lead with a verdict:

- `pass`: no material issue established in scope;
- `partial`: usable, with specific issues or unverified areas;
- `fail`: a primary journey or release-critical contract is broken.

Then provide:

1. findings;
2. strengths worth preserving;
3. rejected ideas or non-issues when useful;
4. evidence boundary and unverified environments;
5. a prioritized, self-contained implementation plan.

Do not write the fixes until the user authorizes implementation.
