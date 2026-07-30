# Repository instructions

## Purpose

Maintain a focused, original Codex plugin for interface design, motion,
accessibility, visual analysis, and frontend implementation.

## Working rules

- Read the target skill completely before using or changing it.
- Read every shared reference explicitly linked by that skill.
- Keep each skill narrow. Put cross-cutting principles in `references/`.
- Preserve the distinction between observed evidence, inference, and unknowns.
- Inspect the user's actual repository, design system, assets, and runtime before
  recommending implementation details.
- Ask for decisions that materially affect product direction. Do not block on
  details that can be discovered safely from the scoped workspace.
- Separate review from implementation. A review does not authorize edits.
- Create genuinely different concepts before asking a user to choose.
- Prefer semantic HTML, real controls, keyboard access, reduced-motion support,
  interruption-safe animation, and measurable verification.
- Follow KISS and DRY. Avoid premature abstractions and monolithic skill files.
- Do not copy external skills, articles, prompts, paid material, or local product
  assets into this repository.
- Update `SOURCES.md` when a new external source materially influences a skill.
- Do not publish, license, create a remote, deploy, or install the plugin without
  explicit current authorization.

## Quality gate

Before considering a change complete:

1. validate JSON and YAML frontmatter;
2. verify every referenced local file exists;
3. run `scripts/sync-skill-references.sh`, then `--check`, and confirm it passes.
   Every shipped reference must be cited by its `SKILL.md`; an uncited one is a
   failure, not a leftover;
4. confirm each rule lives in exactly one reference, and that other references
   name only the handoff;
5. confirm prescriptive values are stated exactly, or as a band with the context
   that decides where inside it a decision lands — never as vague guidance;
6. scan for hard-coded private paths, secrets, and copied product assets;
7. check whitespace and naming consistency;
8. review the workflow for explicit scope, user-selection gates, accessibility,
   performance, and verification;
9. report what was validated and what remains unverified.
