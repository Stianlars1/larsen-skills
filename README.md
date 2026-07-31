<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="plugins/larsen-skills/assets/larsen-mark-on-dark.png">
    <img src="plugins/larsen-skills/assets/larsen-mark-on-light.png" alt="" width="88" height="88">
  </picture>
</p>

<h1 align="center">Larsen Skills</h1>

<p align="center">
  A focused collection of Agent Skills for building thoughtful web interfaces:
  UI/UX, motion, accessibility, visual analysis, prototyping, liquid effects,
  and animated brand systems.
</p>

<p align="center">
  <sub>An open-source project by Larsen Utvikling.</sub>
</p>

<p align="center">
  <a href="https://github.com/Stianlars1/larsen-skills/releases/latest"><img src="https://img.shields.io/github/v/release/Stianlars1/larsen-skills?display_name=tag" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/Stianlars1/larsen-skills/actions/workflows/validate.yml"><img src="https://github.com/Stianlars1/larsen-skills/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
</p>

Use the complete collection as a Codex or Claude Code plugin, or install only
the skills you need in any client that supports the
[Agent Skills standard](https://agentskills.io/).

## Install

### Any supported coding agent

The open [`skills`](https://github.com/vercel-labs/skills) installer supports
Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, OpenCode, and many other
agents.

Browse the available skills and choose where to install them:

```bash
npx skills add Stianlars1/larsen-skills
```

List the collection without installing:

```bash
npx skills add Stianlars1/larsen-skills --list
```

Install one skill globally:

```bash
npx skills add Stianlars1/larsen-skills \
  --skill animated-logo-cycle \
  --global
```

Install the complete collection:

```bash
npx skills add Stianlars1/larsen-skills --skill '*'
```

### GitHub CLI

GitHub CLI 2.90.0 or newer can discover and install the published collection:

```bash
gh skill install Stianlars1/larsen-skills
```

Install one skill directly:

```bash
gh skill install Stianlars1/larsen-skills motion-craft
```

Preview a skill before installing it:

```bash
gh skill preview Stianlars1/larsen-skills motion-craft
```

### Codex plugin

Install all skills as one namespaced Codex plugin:

```bash
codex plugin marketplace add Stianlars1/larsen-skills
codex plugin add larsen-skills@larsen-skills
```

Refresh the marketplace before installing a newer version:

```bash
codex plugin marketplace upgrade larsen-skills
```

### Claude Code plugin

Install all skills as one namespaced Claude Code plugin:

```bash
claude plugin marketplace add Stianlars1/larsen-skills
claude plugin install larsen-skills@larsen-skills
```

The equivalent commands inside Claude Code are:

```text
/plugin marketplace add Stianlars1/larsen-skills
/plugin install larsen-skills@larsen-skills
/reload-plugins
```

### ChatGPT, Claude.ai, and desktop apps

Download the ZIP for the skill you want from the
[latest GitHub release](https://github.com/Stianlars1/larsen-skills/releases/latest).
Each ZIP contains one self-contained skill with its references, templates, and
license.

- **ChatGPT:** Open **Plugins → Skills → Create → Upload from your computer**.
- **Claude.ai / Claude Desktop:** Open **Customize → Skills**, then upload the
  ZIP.

Skill availability can depend on your plan and workspace settings.

## Skills

| Skill | Use it when you want to… |
| --- | --- |
| [`interface-craft`](plugins/larsen-skills/skills/interface-craft/SKILL.md) | Plan, build, or refine a complete interface from product intent through verified implementation. |
| [`interface-review`](plugins/larsen-skills/skills/interface-review/SKILL.md) | Review UI, UX, content, accessibility, responsiveness, motion, and implementation risk without silently changing code. |
| [`motion-craft`](plugins/larsen-skills/skills/motion-craft/SKILL.md) | Find worthwhile animation opportunities, write motion specifications, or improve existing animation. |
| [`reverse-engineer-motion`](plugins/larsen-skills/skills/reverse-engineer-motion/SKILL.md) | Analyze an authorized reference video frame by frame and convert it into an evidence-backed motion specification. |
| [`liquid-interface`](plugins/larsen-skills/skills/liquid-interface/SKILL.md) | Create accessible liquid, metaball, magnetic, or gooey interactions around real DOM controls. |
| [`prototype-lab`](plugins/larsen-skills/skills/prototype-lab/SKILL.md) | Compare genuinely different interface or motion concepts before choosing a production direction. |
| [`ui-primitive-picker`](plugins/larsen-skills/skills/ui-primitive-picker/SKILL.md) | Choose the smallest dependable native element, project primitive, or UI library component for a specific need. |
| [`animated-logo-cycle`](plugins/larsen-skills/skills/animated-logo-cycle/SKILL.md) | Turn a logo, SVG mark, app icon, or family of brand variants into a detailed geometry-led loader and animated identity cycle. |
| [`motion-vocabulary`](plugins/larsen-skills/skills/motion-vocabulary/SKILL.md) | Put the exact name to a motion or material effect you can describe but cannot name, so you can brief it precisely. |

## Shared references

The skills share one rule set. Each reference owns its domain, so a rule is
defined once and every skill that needs it cites the same values.

| Reference | Owns |
| --- | --- |
| [`interface-principles`](plugins/larsen-skills/references/interface-principles.md) | Product job, hierarchy, restraint, working order, and which reference owns what |
| [`accessibility-contract`](plugins/larsen-skills/references/accessibility-contract.md) | Semantics, keyboard, focus, names, forms, hit areas, zoom |
| [`layout-structure`](plugins/larsen-skills/references/layout-structure.md) | Grouping, alignment, spacing, breakpoints, logical properties |
| [`typography`](plugins/larsen-skills/references/typography.md) | Type scale, leading, measure, wrapping, numbers, fonts |
| [`color-and-contrast`](plugins/larsen-skills/references/color-and-contrast.md) | OKLCH, palettes, APCA and WCAG thresholds, gamut, appearances |
| [`surfaces-and-depth`](plugins/larsen-skills/references/surfaces-and-depth.md) | Radius, optical alignment, elevation, materials, gradients, icons |
| [`interface-copy`](plugins/larsen-skills/references/interface-copy.md) | Labels, errors, empty states, voice and tone |
| [`motion-principles`](plugins/larsen-skills/references/motion-principles.md) | Whether to animate, easing, duration, choreography, interruptibility |
| [`gesture-physics`](plugins/larsen-skills/references/gesture-physics.md) | Direct manipulation, velocity, momentum, boundaries, recognition |
| [`review-protocol`](plugins/larsen-skills/references/review-protocol.md) | Severity, evidence, consolidation, output format, verdict |
| [`evidence-and-verification`](plugins/larsen-skills/references/evidence-and-verification.md) | Evidence boundaries, verification environments, feel checks |

Standalone skill packages are self-contained: `scripts/sync-skill-references.sh`
copies each shared reference into every skill that cites it, so a single
extracted skill still works on its own.

## Use

Installed standalone skills are selected automatically when your prompt matches
their description. Clients with explicit skill invocation can also run them by
name.

Codex plugin examples:

```text
$larsen-skills:interface-review full checkout flow
$larsen-skills:motion-craft opportunities dashboard
$larsen-skills:animated-logo-cycle /absolute/path/to/logo.svg
```

Claude Code plugin examples:

```text
/larsen-skills:interface-review full checkout flow
/larsen-skills:motion-craft opportunities dashboard
/larsen-skills:animated-logo-cycle /absolute/path/to/logo.svg
```

Natural-language examples:

```text
Review this checkout flow across layout, content, accessibility, and motion.

Analyze this interaction recording frame by frame and write an implementation
spec without copying its branded assets.

Inspect this SVG logo, propose four geometry-led animation concepts, and stop
for my selection before prototyping.
```

## How the collection works

The skills share a small set of interface, visual-system, motion, and evidence
principles. They are designed to:

- begin with the product job rather than surface styling;
- separate observed evidence, inference, and unknowns;
- preserve semantic controls, keyboard access, visible focus, and reduced
  motion;
- treat easing, interruption, lifecycle, and performance as part of motion
  quality;
- ask for user selection when several directions would create materially
  different products;
- distinguish source inspection, local runtime checks, deployment, and live
  verification.

Review skills are read-only by default. Implementation skills change code only
when the request authorizes implementation.

## Compatibility

The individual skills use portable `SKILL.md` files with supporting Markdown
resources. They can be installed through the open `skills` CLI in clients that
implement Agent Skills.

The repository also includes native marketplace manifests for:

- Codex: `.agents/plugins/marketplace.json`
- Claude Code: `.claude-plugin/marketplace.json`

The complete plugin is namespaced as `larsen-skills`. Standalone installs use
the individual skill names.

## Development

Clone the repository:

```bash
git clone https://github.com/Stianlars1/larsen-skills.git
cd larsen-skills
```

After changing a shared reference, refresh the self-contained skill copies:

```bash
./scripts/sync-skill-references.sh
```

Build self-contained skill folders and ZIP archives:

```bash
./scripts/package-standalone-skills.sh
```

Validate the Claude marketplace and plugin manifests:

```bash
claude plugin validate . --strict
claude plugin validate ./plugins/larsen-skills --strict
```

See [AGENTS.md](AGENTS.md) for repository contribution rules.

## Sources and license

This collection is an original synthesis of public design-engineering
principles and user-owned case studies. It does not mirror another skill
repository, article collection, paid course, prompt, or product asset library.

See [SOURCES.md](SOURCES.md) for provenance and reuse boundaries.

Larsen Skills is available under the [MIT License](LICENSE). The Larsen
Utvikling brand marks remain reserved and are not relicensed under MIT; see
[NOTICE.md](NOTICE.md).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="plugins/larsen-skills/assets/larsen-lockup-on-dark.png">
    <img src="plugins/larsen-skills/assets/larsen-lockup-on-light.png" alt="Larsen Utvikling" width="220">
  </picture>
</p>

<p align="center">
  <sub>Created and maintained by Larsen Utvikling.</sub>
</p>
