---
name: prototype-lab
description: >-
  Explore a material interface or motion decision through several genuinely
  different, isolated prototypes and a user selection gate before production
  integration. Use when the user wants variants, creative directions,
  experiments, a playground, or is unsure which interaction concept to build.
  Do not use when the final direction and acceptance criteria are already fixed.
license: MIT
---

# Prototype Lab

Prototypes answer decisions. They are not low-quality versions of production and
not a collection of minor style tweaks.

Read before acting:

- `../../references/interface-principles.md`
- `../../references/visual-systems.md`
- `../../references/motion-principles.md`
- `../../references/evidence-and-verification.md`

## Define the decision

Establish:

- the product question the prototypes must answer;
- what is fixed: content, brand, layout, technology, accessibility, and
  performance constraints;
- what may vary;
- target device and input method;
- expected fidelity;
- how many directions to explore. Recommend 3–5 when the user has no preference;
- evaluation criteria and who chooses.

Do not start until the variants can be compared against the same question.

## Create distinct hypotheses

Each direction must differ in its underlying interaction, hierarchy, spatial
model, or material logic.

Weak variation:

- same component with different accent colors;
- same motion with small duration changes;
- same layout with a different radius.

Strong variation:

- direct manipulation versus state-triggered transformation;
- spatial continuity versus deliberate cut;
- geometry-led morph versus layered material transition;
- compact disclosure versus persistent overview;
- restrained functional motion versus rare expressive choreography.

Name each concept by its hypothesis, not an adjective such as "modern".

## Write concept cards

Before code:

```markdown
### Concept name
- Hypothesis:
- User benefit:
- Interaction model:
- Visual and motion model:
- What stays fixed:
- Main risk:
- What the prototype must prove:
```

Reject redundant concepts before implementation.

## Build an isolated lab

- Keep prototypes outside production routing and state unless the user asks
  otherwise.
- Reuse the product's tokens and primitives when they are part of the question.
- Use realistic content and target dimensions.
- Give every variant the same baseline constraints.
- Add a simple switcher with stable concept IDs.
- Preserve selected concept and controls in URL/query state when sharing or
  repeatable comparison matters.
- Include reset, pause, reduced-motion, and replay controls when motion is under
  evaluation.
- Show key parameters only; do not turn every constant into a control.

Avoid premature abstraction between variants. Duplication is acceptable while
the concepts are intentionally diverging; extract shared code after selection.

## Verify every concept

For each variant, capture:

- normal-speed behavior;
- slow or stepped inspection where useful;
- keyboard and touch behavior;
- reduced-motion version;
- narrow and wide layout;
- interrupted and repeated interaction;
- known performance cost;
- limitations and unresolved questions.

Do not polish one favorite concept more than the others before comparison.

## Selection gate

Present a comparison:

| Concept | Product benefit | Character | Accessibility | Performance | Complexity | Main risk |
| --- | --- | --- | --- | --- | --- | --- |

Give a recommendation and the evidence behind it, but ask the user to select the
direction. Do not silently promote a prototype into production code.

After selection:

1. record the chosen concept and rejected alternatives;
2. define the production acceptance criteria;
3. identify prototype shortcuts that must be replaced;
4. move only the selected behavior into the product;
5. remove or archive the lab only with user approval.
