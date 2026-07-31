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

Automated, and enforced in CI by `.github/workflows/validate.yml`:

```bash
./scripts/sync-skill-references.sh          # regenerate per-skill reference copies
./scripts/validate-repository.py            # manifests, frontmatter, citations, hygiene
./scripts/package-standalone-skills.sh dist/local
./scripts/validate-repository.py dist/local # packages are self-contained
```

`validate-repository.py` checks manifest JSON and version consistency, YAML
frontmatter and `name`-matches-directory, that every `references/…` citation
resolves, that no shared reference is uncited, that references packaged together
can reach each other, balanced code fences and aligned table columns, and the
absence of private paths, secret prefixes, and trailing whitespace.

Still your judgment, because no script can check it:

1. confirm each rule lives in exactly one reference, and that other references
   name only the handoff;
2. confirm prescriptive values are stated exactly, or as a band with the context
   that decides where inside it a decision lands — never as vague guidance;
3. confirm no copied product asset or third-party prose entered the repository;
4. review the workflow for explicit scope, user-selection gates, accessibility,
   performance, and verification;
5. report what was validated and what remains unverified.

Edit only the shared originals in `plugins/larsen-skills/references/`. The
per-skill copies are generated; CI fails if running the sync produces a diff,
because that means an edit was made to a copy the next sync would discard.
