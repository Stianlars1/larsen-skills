# Sources and provenance

This repository is an original synthesis. Sources are used to learn principles,
vocabulary, review methods, and implementation constraints. Source code,
articles, prompts, and assets must not be copied wholesale into this repository.

| Source | Status observed | How it informed this repository | Reuse boundary |
| --- | --- | --- | --- |
| [Jakub Krehel's skills](https://github.com/jakubkrehel/skills), [jakub.kr](https://jakub.kr/skills), and [interfaces.dev](https://interfaces.dev/) | Public repository marked MIT, re-reviewed 2026-07-30 | Interface hierarchy, typography, OKLCH color and contrast, layout and grouping, interface copy, accessibility engineering, surface polish, gradients, shared layout, and the rule-ownership discipline that keeps one rule in one place | Principles were re-expressed, reorganized into this repository's own reference structure, and merged with other sources; no article or skill is mirrored verbatim |
| [Emil Kowalski's skills](https://github.com/emilkowalski/skills), [emilkowal.ski](https://emilkowal.ski/skill), and [animations.dev](https://animations.dev/) | Public repository marked MIT, re-reviewed 2026-07-30 | Motion purpose and the frequency gate, easing selection, duration budgets, physicality and origin, interruptibility, spring configuration, gesture momentum and velocity handoff, translucent materials, reduced motion, motion terminology, and the discipline of stating exact values rather than guidance | Only public material reviewed; paid course content is excluded. Values are cited as bands with their governing context and combined with other sources, not reproduced as a rule list |
| [Arlan's Liquid UI](https://www.arlan.me/vault/liquid-ui) | Public page marked MIT when reviewed | SDF-based merging, marching-squares contours, interaction modes, and the distinction between a visual layer and semantic DOM | This repository specifies an original implementation; it does not copy the page's source or prompt |
| Station logo-cycle implementation and recording | User-owned local source, reviewed 2026-07-29 | Multi-asset transitions, Web Animations lifecycle, spring-derived easing, dwell, hover defer, visibility handling, and reduced motion | No Station logo assets or production code are redistributed |
| Tinify logo-cycle implementation and recording | User-owned local source, reviewed 2026-07-29 | Geometry-led transformation, masks, optical centering, CSS timeline design, and lifecycle tests | No Tinify logo assets or production code are redistributed |
| Larsen Utvikling brand identity | First-party assets supplied and approved by the owner, reviewed 2026-07-29 | Publisher attribution for Larsen Skills, plugin presentation, and repository sharing | Included only for this project's identity; the marks are not relicensed under MIT |
| Local `scroll-video-skill-bundle` | Provenance and license unresolved | The general idea of extracting frames from a video and producing a reproducible motion specification | Its code and text are excluded until provenance and reuse rights are established |
| Apple WWDC design sessions, as distilled in public secondary writing | Public talks; distillation reviewed 2026-07-30 | Fluid-interface behavior: response on pointer-down, 1:1 tracking with grab offset, interruption from the presentation value, velocity handoff, exponential momentum projection, rubber-banding, damping-and-response spring framing, and translucent material hierarchy | Behavior and published formulas are restated in this repository's own words and web idiom; no session transcript, slide, or sample-code file is reproduced |
| W3C WCAG 2.2 and the APCA contrast work | Public standards and drafts, reviewed 2026-07-30 | Contrast thresholds, target-size minimums and their exceptions, reflow and zoom requirements, autoplay and timed-UI rules, and label-in-name | Normative thresholds are facts, cited with their source standard; specification text is not reproduced |
| MDN and the CSS/OpenType specifications | Public documentation, reviewed 2026-07-30 | Property behavior for `clip-path`, `@starting-style`, gradient interpolation spaces, `text-box`, logical properties, variable-font axes, and OpenType feature tags | Behavior is described, not quoted; examples are written for this repository |

## Source discipline

When extending this repository:

1. record the source and access date;
2. verify the source's current license before copying any protectable expression;
3. prefer original synthesis over close paraphrase;
4. distinguish public, user-owned, proprietary, paid, and unknown-provenance
   material;
5. never redistribute product assets merely because they were available locally;
6. document important divergence from a source instead of silently implying
   equivalence.

Licenses and web content can change. Recheck them at publication time.
