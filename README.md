# Larsen Skills

A curated collection of Agent Skills for design engineering: interfaces, UI/UX,
motion, visual analysis, accessibility, and frontend implementation.

The repository has two distribution formats:

- one marketplace plugin for Codex and Claude Code;
- self-contained skill folders and ZIP files for clients that support the open
  Agent Skills format.

## Status

This repository contains the published `0.1.0` source.

- GitHub repository:
  [`Stianlars1/larsen-skills`](https://github.com/Stianlars1/larsen-skills)
- Visibility: public
- Default branch: `main`
- GitHub Release: not created yet
- License: [MIT](LICENSE)
- Core guidance: framework-agnostic
- Primary v1 adapter: React/Next.js and Motion when already used by the project

## Skills

| Skill | Purpose |
| --- | --- |
| [`interface-craft`](plugins/larsen-skills/skills/interface-craft/SKILL.md) | Plan, build, and refine an interface from product intent to verified implementation. |
| [`interface-review`](plugins/larsen-skills/skills/interface-review/SKILL.md) | Perform an evidence-based review of UI, UX, content, accessibility, and motion. |
| [`motion-craft`](plugins/larsen-skills/skills/motion-craft/SKILL.md) | Find, specify, review, and improve animations with an explicit purpose. |
| [`reverse-engineer-motion`](plugins/larsen-skills/skills/reverse-engineer-motion/SKILL.md) | Analyze a video frame by frame and turn it into an implementable motion specification. |
| [`liquid-interface`](plugins/larsen-skills/skills/liquid-interface/SKILL.md) | Build accessible liquid and metaball-style unions around real DOM elements. |
| [`prototype-lab`](plugins/larsen-skills/skills/prototype-lab/SKILL.md) | Compare genuinely different, isolated concepts before selecting a production direction. |
| [`ui-primitive-picker`](plugins/larsen-skills/skills/ui-primitive-picker/SKILL.md) | Select one suitable UI primitive or library solution from the actual project stack. |
| [`animated-logo-cycle`](plugins/larsen-skills/skills/animated-logo-cycle/SKILL.md) | Derive a detailed, geometry-led animated cycle from a logo or logo family. |

## Compatibility

The table describes the supported installation route for this repository, not
every extension format a product may support.

| Host | Complete plugin | Standalone skills | Recommended route |
| --- | --- | --- | --- |
| Codex CLI and desktop | Yes | Yes | Codex marketplace |
| Claude Code | Yes | Yes | Claude marketplace |
| ChatGPT | No direct repository marketplace install | Yes | Upload one packaged skill |
| Claude.ai and Claude Desktop | No direct repository marketplace install | Yes | Upload one packaged ZIP |
| Cursor editor and CLI | Not with the current manifests | Yes | Copy to a skills directory |
| GitHub Copilot | Not with the current manifests | Yes | Copy to a Copilot skills directory |
| Gemini CLI | Not with the current manifests | Yes | Link or copy a packaged skill |
| OpenCode | Not with the current manifests | Yes | Copy to an OpenCode skills directory |
| Google Antigravity | Not with the current manifests | Yes | Copy to an Agent Skills directory |

Product support changes over time. These instructions were checked against the
official documentation on 2026-07-29.

## Repository structure

```text
.agents/plugins/marketplace.json        Codex marketplace
.claude-plugin/marketplace.json         Claude Code marketplace
plugins/larsen-skills/
  .codex-plugin/plugin.json             Codex plugin manifest
  .claude-plugin/plugin.json            Claude Code plugin manifest
  skills/                               Canonical shared Agent Skills source
  references/                           Shared interface and motion guidance
scripts/package-standalone-skills.sh    Standalone folder and ZIP builder
LICENSE                                 MIT License
SOURCES.md                              Provenance and reuse boundaries
NOTICE.md                               Copyright and third-party notes
AGENTS.md                               Repository development rules
```

The plugin is the canonical source. The packaging script copies only the shared
references needed by each skill and rewrites those links inside the generated
bundle. This keeps the maintained source DRY without shipping incomplete skills
to standalone hosts.

## Install in Codex CLI or Codex desktop

Codex CLI and the Codex desktop app use the Codex plugin marketplace format.

### Test the local checkout

```bash
codex plugin marketplace add /absolute/path/to/larsen-skills
codex plugin add larsen-skills@larsen-skills
```

Restart or refresh Codex after installation. Invoke a skill with its plugin
namespace:

```text
$larsen-skills:interface-review full checkout flow
$larsen-skills:motion-craft opportunities dashboard
$larsen-skills:animated-logo-cycle /absolute/path/to/logo.svg
```

### Install from GitHub after publication

```bash
codex plugin marketplace add Stianlars1/larsen-skills
codex plugin add larsen-skills@larsen-skills
```

Refresh the marketplace before installing an updated plugin version:

```bash
codex plugin marketplace upgrade larsen-skills
```

See the official
[OpenAI plugin documentation](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex).

## Install in Claude Code

### Test without installing

From the repository root:

```bash
claude --plugin-dir ./plugins/larsen-skills
```

Invoke a plugin skill with its namespace:

```text
/larsen-skills:interface-review full checkout flow
/larsen-skills:motion-craft opportunities dashboard
```

### Install from the local checkout

```bash
claude plugin marketplace add /absolute/path/to/larsen-skills
claude plugin install larsen-skills@larsen-skills
```

### Install from GitHub after publication

```bash
claude plugin marketplace add Stianlars1/larsen-skills
claude plugin install larsen-skills@larsen-skills
```

The equivalent interactive commands are:

```text
/plugin marketplace add Stianlars1/larsen-skills
/plugin install larsen-skills@larsen-skills
/reload-plugins
```

To install only one standalone skill for all local Claude Code projects, build
the packages and copy its complete directory:

```bash
mkdir -p ~/.claude/skills
cp -R dist/larsen-skills-0.1.0/skills/animated-logo-cycle ~/.claude/skills/
```

See the official
[Claude Code skills](https://code.claude.com/docs/en/skills) and
[plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
documentation.

## Build standalone skills

Run the deterministic packager from the repository root:

```bash
./scripts/package-standalone-skills.sh
```

It creates:

```text
dist/larsen-skills-0.1.0/
  skills/                         Self-contained skill directories
  zips/                           One upload-ready ZIP per skill
    SHA256SUMS                    Archive checksums
```

The script refuses to overwrite an existing build. Pass a different output
directory when you want another build:

```bash
./scripts/package-standalone-skills.sh /absolute/path/to/new-output
```

Review the generated skill before installing or uploading it. Agent Skills can
contain instructions, resources, and executable scripts; this repository's
current standalone bundles contain instructions, references, and templates, but
no executable skill scripts.

## Install in ChatGPT

ChatGPT supports personal Agent Skills for eligible plans and workspaces.
Availability and sharing controls may be managed by a workspace administrator.

1. Build the standalone packages.
2. In ChatGPT, open **Plugins** in the sidebar.
3. Select **Skills**, then **Create**.
4. Select **Upload from your computer**.
5. Select the required self-contained bundle from
   `dist/larsen-skills-0.1.0/`. The build provides both a skill folder and a
   ZIP; use the format accepted by the current upload picker.
6. Review the scan result before enabling the skill.

ChatGPT skills may need to be added separately on desktop and web/mobile because
personal skills do not automatically sync between those surfaces. See
[Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/).

## Install in Claude.ai or Claude Desktop

1. Build the standalone packages.
2. Open **Customize**, then **Skills**.
3. Upload one ZIP from `dist/larsen-skills-0.1.0/zips/`.
4. Enable the skill and verify it appears in the skills list.

Each archive contains one skill directory at the ZIP root, including every
referenced file. Plan availability, code-execution requirements, and workspace
admin controls can differ. See Anthropic's
[skill usage guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
and
[custom skill packaging guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Install in Cursor editor or Cursor CLI

Cursor supports Agent Skills in both the editor and CLI. This repository does
not claim Cursor plugin-manifest compatibility; use standalone skill folders.

For one project:

```bash
mkdir -p /path/to/project/.cursor/skills
cp -R dist/larsen-skills-0.1.0/skills/animated-logo-cycle \
  /path/to/project/.cursor/skills/
```

For all projects:

```bash
mkdir -p ~/.cursor/skills
cp -R dist/larsen-skills-0.1.0/skills/animated-logo-cycle ~/.cursor/skills/
```

Cursor also recognizes the shared project and user locations
`.agents/skills/` and `~/.agents/skills/`. Restart or reload the agent session,
then invoke the skill from the slash-command menu or describe a task matching
its frontmatter. See Cursor's
[Agent Skills documentation](https://cursor.com/docs/skills) and
[2.4 release notes](https://cursor.com/changelog/2-4).

## Install for GitHub Copilot

GitHub Copilot discovers project skills from `.github/skills/`,
`.claude/skills/`, or `.agents/skills/`. It discovers personal skills from
`~/.copilot/skills/` or `~/.agents/skills/`.

For one repository:

```bash
mkdir -p /path/to/project/.github/skills
cp -R dist/larsen-skills-0.1.0/skills/interface-review \
  /path/to/project/.github/skills/
```

For personal use:

```bash
mkdir -p ~/.copilot/skills
cp -R dist/larsen-skills-0.1.0/skills/interface-review ~/.copilot/skills/
```

GitHub CLI also offers `gh skill` in public preview, but it requires GitHub CLI
2.90.0 or newer. Direct `gh skill install Stianlars1/larsen-skills ...` is not
documented here until this repository's nested marketplace layout has been
tested with that command. Manual installation of the generated folder is the
verified repository-independent route.

See
[Adding Agent Skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Install in Gemini CLI

Build the standalone packages, then link one local skill during development:

```bash
gemini skills link \
  ./dist/larsen-skills-0.1.0/skills/animated-logo-cycle
```

Alternatively, copy a packaged skill to:

- `~/.gemini/skills/` or `~/.agents/skills/` for all projects;
- `.gemini/skills/` or `.agents/skills/` for one workspace.

Inside Gemini CLI, use `/skills list` to verify discovery and `/skills reload`
after changes. See
[Managing Agent Skills in Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/).

## Install in OpenCode

Copy a packaged skill to one supported location:

- `.opencode/skills/<name>/` for one project;
- `~/.config/opencode/skills/<name>/` for all projects;
- `.agents/skills/<name>/` or `~/.agents/skills/<name>/` for a shared,
  cross-client location.

Example:

```bash
mkdir -p ~/.config/opencode/skills
cp -R dist/larsen-skills-0.1.0/skills/motion-craft \
  ~/.config/opencode/skills/
```

See the official [OpenCode Agent Skills guide](https://opencode.ai/docs/skills).

## Install in Google Antigravity

Use a standalone folder:

- `.agents/skills/<name>/` for one project;
- `~/.gemini/config/skills/<name>/` for global Antigravity use.

Example:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R dist/larsen-skills-0.1.0/skills/interface-craft \
  /path/to/project/.agents/skills/
```

See Google's
[Antigravity skills guide](https://codelabs.developers.google.com/getting-started-agy-ide#11).

## Generic Agent Skills clients

For another client that implements the
[Agent Skills standard](https://agentskills.io/), start with a generated
self-contained folder. Place the complete `<skill-name>/` directory in the
client's documented skills location. Do not copy only `SKILL.md`; supporting
references and templates are part of the skill.

The shared `.agents/skills/` location is supported by several clients, but it is
not universal. Verify the target client's current documentation before using
that path.

## GitHub authentication for maintainers

Verify the active GitHub CLI account before repository maintenance:

```bash
gh auth status
```

If the credential is invalid, reauthenticate with GitHub's browser flow:

```bash
gh auth login --hostname github.com --git-protocol https --web --clipboard
gh auth status
```

The first command copies the one-time code and opens the browser authorization
flow. Complete it as `Stianlars1`, return to the terminal, and confirm that
`gh auth status` reports a valid active account.

If the browser flow keeps selecting the wrong account, explicitly remove only
the stale `Stianlars1` credential and repeat the login:

```bash
gh auth logout --hostname github.com --user Stianlars1
gh auth login --hostname github.com --git-protocol https --web --clipboard
```

Clone the published repository with:

```bash
git clone https://github.com/Stianlars1/larsen-skills.git
```

## Usage principles

Activate the narrowest skill that covers the task.

`interface-review` is read-only by default. Implementation skills pause at
material design decisions, ask the user to select a direction, and then
implement and verify only the approved scope.

## Source and license policy

This repository is an original synthesis of studied principles and user-owned
case studies. It is not a mirror of another repository, article collection,
course, prompt, or product asset library.

See [SOURCES.md](SOURCES.md) for provenance, influence, and reuse boundaries.
Original repository content is licensed under the [MIT License](LICENSE).
External names, trademarks, links, and referenced assets remain subject to
their respective owners' terms.

## Release follow-up

The repository source is public. The next release tasks are:

1. local end-to-end installation tests in Codex and Claude Code;
2. installation tests of representative standalone packages;
3. a tagged GitHub Release with the standalone ZIP files;
4. optional plugin artwork and screenshots.
