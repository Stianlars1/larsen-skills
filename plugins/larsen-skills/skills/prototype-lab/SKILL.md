---
name: prototype-lab
description: >-
  Explore a material interface or motion decision through several genuinely
  different, isolated prototypes behind a variant switcher, with a user
  selection gate before production integration. Use when the user wants
  variants, creative directions, experiments, a playground, or is unsure which
  interaction concept to build. Do not use when the final direction and
  acceptance criteria are already fixed. Triggers on prototype, variants,
  explore directions, playground, "show me a few options", "which one feels
  better", design exploration, concept comparison.
license: MIT
---

# Prototype Lab

Prototypes answer decisions. They are not low-quality versions of production and
not a collection of minor style tweaks.

**The entire value of this skill is divergence.** Three tints of one idea waste
the switcher — the user learns nothing by flipping between them.

## Quick reference

| Need | Read |
| --- | --- |
| Product job, hierarchy, restraint, working order | `references/interface-principles.md` |
| Radius, optical alignment, elevation, materials, gradients, icons | `references/surfaces-and-depth.md` |
| Whether to animate, easing, duration, interruptibility | `references/motion-principles.md` |
| Drag, swipe, velocity, boundaries | `references/gesture-physics.md` |
| Semantics, keyboard, focus, hit areas | `references/accessibility-contract.md` |
| Evidence boundaries and feel checks | `references/evidence-and-verification.md` |

**Divergence is not permission to drop the craft bar.** Every variant
individually meets the non-negotiables — correct easing, sub-300ms UI motion,
correct `transform-origin`, `transform`/`opacity` only, real focus states,
reduced motion handled. A sloppy variant does not widen the exploration; it
loses on execution and teaches nothing about the direction it represents.

## Define the decision

Establish:

- the product question the prototypes must answer;
- what is fixed — content, brand, layout, technology, accessibility, and
  performance constraints;
- what may vary;
- target device and input method;
- **how often the user will encounter this surface** — it bounds how far the
  boldest variant may go;
- the product's personality: a crisp daily-use tool earns quieter variants than a
  playful consumer app;
- expected fidelity;
- how many directions to explore — recommend 3, up to 5 when the space is
  genuinely wide. More than 5 dilutes the comparison;
- evaluation criteria, and who chooses.

Do not start until the variants can be compared against the same question.

**One thing per run.** If the description spans several components, narrow it:
pick the single highest-leverage piece, say which and why, and offer the rest as
follow-up runs.

## Create distinct hypotheses

Each direction must differ in its underlying interaction, hierarchy, spatial
model, or material logic. **State each variant's axis in a phrase before building
anything.** No two variants may share an axis position.

| Weak variation | Strong variation |
| --- | --- |
| Same component, different accent color | Direct manipulation vs. state-triggered transformation |
| Same motion, small duration change | Spatial continuity vs. a deliberate cut |
| Same layout, different radius | Geometry-led morph vs. layered material transition |
| Same structure, different copy | Compact disclosure vs. persistent overview |
| | Restrained functional motion vs. rare expressive choreography |

Name each concept by its hypothesis — "Quiet", "Editorial", "Dense", "Direct" —
never "Option A/B/C" and never an adjective like "modern".

Sharing the project's tokens is not convergence. Variants *should* look like they
could ship in this product tomorrow.

## Write concept cards

Before code:

```markdown
### Concept name
- Hypothesis:
- Axis it explores:
- User benefit:
- Interaction model:
- Visual and motion model:
- What stays fixed:
- Main risk:
- What the prototype must prove:
```

Reject redundant concepts before implementation. If two converge while you build
them, cut one and say so — two truly distinct directions beat three padded ones.

## Build an isolated lab

- **Never touch production code during exploration.** Keep prototypes outside
  production routing and state unless the user asks otherwise.
- Reuse the product's tokens and primitives when they are part of the question.
- **Use realistic content** — actual product-shaped copy, plausible names and
  numbers, target dimensions. No lorem ipsum, no dead buttons, no "imagine this
  part".
- Give every variant the same baseline constraints.
- Add a switcher with stable concept IDs. **Switching is instant** — flipping is
  a high-frequency action within the session, so by the frequency gate the
  variant swap itself gets no animation.
- **Render one variant at a time, full size, in realistic surrounding context** —
  a toast needs a page behind it, a card needs siblings, a button needs a form.
  Side-by-side thumbnails distort spacing and scale.
- Preserve the selected concept in URL state when sharing or repeatable
  comparison matters.
- Include reset, pause, replay, and reduced-motion controls when motion is under
  evaluation.
- Show key parameters only; do not turn every constant into a control.

Avoid premature abstraction between variants. Duplication is acceptable while the
concepts are intentionally diverging; extract shared code after selection.

## Verify every concept

For each variant, capture:

- normal-speed behavior;
- slow or stepped inspection where motion is under evaluation;
- keyboard and touch behavior, including visible focus;
- the reduced-motion version;
- narrow and wide layout;
- interrupted and repeated interaction;
- known performance cost;
- limitations and unresolved questions.

**Flip through every variant yourself before showing the user.** Confirm each
renders, each interaction responds, and the console is clean.

**Do not polish one favorite more than the others before comparison.** An unfair
comparison answers the wrong question.

## Selection gate

Present the comparison and stop. The choice belongs to the user.

| Concept | Axis | When it wins | What it costs | Accessibility | Performance | Complexity |
| --- | --- | --- | --- | --- | --- | --- |

Sell each variant honestly — one line on when it is the right choice, one on what
it costs. **Never pre-pick a favorite inside the table.** If the user asks which
you would choose, answer with a reason rooted in the product's personality and
frequency of use, not aesthetics alone.

Close with where the lab is running and how to flip between variants.

**Do not silently promote a prototype into production code.**

## After selection

1. record the chosen concept and the rejected alternatives;
2. define the production acceptance criteria;
3. identify prototype shortcuts that must be replaced;
4. move only the selected behavior into the product, following the project's
   existing conventions;
5. remove or archive the lab only with user approval.

If the user wants another round instead, keep the harness and diverge *around*
the direction they gravitated toward.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Three variants of one idea | State each axis first; no two share a position |
| Variants named "Option A/B/C" | Name by hypothesis |
| One favorite polished more than the rest | Equal effort until the comparison |
| Lorem ipsum or dead buttons | Realistic content, working interactions |
| Side-by-side thumbnails | One variant at a time, full size, in context |
| Animated variant switching | Instant — it is a high-frequency action |
| Craft bar dropped "because it's a prototype" | Every variant meets the non-negotiables |
| Shared abstraction extracted too early | Duplicate while diverging; extract after selection |
| Prototype promoted without asking | The selection gate is required |
| Lab left in the repo silently | Remove or archive only with approval |
