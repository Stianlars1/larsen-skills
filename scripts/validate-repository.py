#!/usr/bin/env python3
"""Validate the repository's manifests, skills, and shared references.

Run with no arguments to check the working tree:

    ./scripts/validate-repository.py

Pass a built output directory to also verify that every standalone package is
self-contained:

    ./scripts/validate-repository.py dist/larsen-skills-0.2.0

Exits non-zero on the first failing category so CI fails loudly. Uses only the
standard library; PyYAML is used for frontmatter when available and a structural
check is used when it is not.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore

    HAVE_YAML = True
except ImportError:  # pragma: no cover - depends on the runner
    HAVE_YAML = False

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "larsen-skills"
SHARED_REFERENCES = PLUGIN / "references"
SKILLS = PLUGIN / "skills"

MANIFESTS = (
    ROOT / ".claude-plugin" / "marketplace.json",
    PLUGIN / ".claude-plugin" / "plugin.json",
    PLUGIN / ".codex-plugin" / "plugin.json",
)

REQUIRED_FRONTMATTER = ("name", "description", "license")

# Patterns that must never reach a published package.
FORBIDDEN = (
    ("/Users/", "absolute home path"),
    ("/home/runner/", "absolute runner path"),
    ("sk-ant-", "Anthropic key prefix"),
    ("ghp_", "GitHub token prefix"),
    ("github_pat_", "GitHub token prefix"),
    ("AKIA", "AWS access key prefix"),
    ("-----BEGIN", "embedded private key"),
)

CITATION = re.compile(r"`((?:references|templates)/[a-z0-9-]+\.md)`")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
TABLE_SEPARATOR = re.compile(r"^\|[\s:|-]+\|\s*$")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def skill_directories() -> list[Path]:
    return sorted(p for p in SKILLS.iterdir() if p.is_dir())


def check_manifests(report: Report) -> None:
    versions: dict[str, str] = {}

    for manifest in MANIFESTS:
        if not manifest.exists():
            report.fail(f"missing manifest: {relative(manifest)}")
            continue
        try:
            data = json.loads(manifest.read_text())
        except json.JSONDecodeError as error:
            report.fail(f"invalid JSON in {relative(manifest)}: {error}")
            continue

        if "plugins" in data:
            for entry in data["plugins"]:
                versions[f"{relative(manifest)}:{entry['name']}"] = entry["version"]
                source = entry.get("source")
                if isinstance(source, str):
                    target = (manifest.parent.parent / source).resolve()
                    if not target.is_dir():
                        report.fail(
                            f"{relative(manifest)} points at a missing plugin source: {source}"
                        )
        else:
            versions[relative(manifest)] = data.get("version", "")

    distinct = set(versions.values())
    if len(distinct) > 1:
        detail = ", ".join(f"{k} = {v}" for k, v in sorted(versions.items()))
        report.fail(f"version mismatch across manifests: {detail}")
    elif distinct:
        report.note(f"version {distinct.pop()} consistent across {len(versions)} manifests")


def parse_frontmatter(text: str, path: Path, report: Report) -> dict[str, str] | None:
    match = FRONTMATTER.match(text)
    if not match:
        report.fail(f"{relative(path)}: missing or malformed YAML frontmatter")
        return None

    block = match.group(1)

    if HAVE_YAML:
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError as error:
            report.fail(f"{relative(path)}: invalid YAML frontmatter: {error}")
            return None
        if not isinstance(parsed, dict):
            report.fail(f"{relative(path)}: frontmatter is not a mapping")
            return None
        return {str(k): str(v) for k, v in parsed.items()}

    # Structural fallback: top-level `key:` entries only.
    fields: dict[str, str] = {}
    for line in block.splitlines():
        key = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if key:
            fields[key.group(1)] = key.group(2)
    return fields


def check_skills(report: Report) -> None:
    directories = skill_directories()
    if not directories:
        report.fail("no skills found")
        return

    cited_shared: set[str] = set()

    for directory in directories:
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            report.fail(f"{relative(directory)}: missing SKILL.md")
            continue

        text = skill_file.read_text()
        fields = parse_frontmatter(text, skill_file, report)
        if fields is None:
            continue

        for key in REQUIRED_FRONTMATTER:
            if not fields.get(key, "").strip():
                report.fail(f"{relative(skill_file)}: frontmatter missing '{key}'")

        name = fields.get("name", "").strip()
        if name and name != directory.name:
            report.fail(
                f"{relative(skill_file)}: frontmatter name '{name}' "
                f"does not match directory '{directory.name}'"
            )

        if "../../references/" in text:
            report.fail(
                f"{relative(skill_file)}: non-portable reference path "
                "(would break a standalone package)"
            )

        for citation in sorted(set(CITATION.findall(text))):
            if not (directory / citation).exists():
                report.fail(f"{relative(skill_file)}: cites {citation}, which does not exist")
            if citation.startswith("references/"):
                cited_shared.add(citation.split("/", 1)[1])

    shared = {p.name for p in SHARED_REFERENCES.glob("*.md")}
    for orphan in sorted(shared - cited_shared):
        report.fail(f"shared reference cited by no skill: references/{orphan}")

    report.note(f"{len(directories)} skills, {len(shared)} shared references")


def check_reference_graph(report: Report) -> None:
    """Every path a reference points at must exist beside it in each skill."""
    for directory in skill_directories():
        local = directory / "references"
        if not local.is_dir():
            continue
        for reference in sorted(local.glob("*.md")):
            for citation in sorted(set(CITATION.findall(reference.read_text()))):
                if not (directory / citation).exists():
                    report.fail(
                        f"{relative(reference)}: cites {citation}, "
                        "which is not packaged with it"
                    )


def check_markdown(report: Report) -> None:
    files = sorted(PLUGIN.rglob("*.md")) + [
        ROOT / "README.md",
        ROOT / "AGENTS.md",
        ROOT / "SOURCES.md",
    ]

    for path in files:
        if not path.exists():
            continue
        text = path.read_text()

        if text.count("```") % 2:
            report.fail(f"{relative(path)}: unbalanced code fence")

        if not text.endswith("\n"):
            report.fail(f"{relative(path)}: missing trailing newline")

        if re.search(r"[ \t]+$", text, re.MULTILINE):
            report.fail(f"{relative(path)}: trailing whitespace")

        lines = text.split("\n")
        in_fence = False
        for index, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not line.startswith("|"):
                continue
            following = lines[index + 1] if index + 1 < len(lines) else ""
            if TABLE_SEPARATOR.match(following) and line.count("|") != following.count("|"):
                report.fail(
                    f"{relative(path)}:{index + 1}: table header has "
                    f"{line.count('|') - 1} columns, separator has "
                    f"{following.count('|') - 1}"
                )


def check_hygiene(report: Report) -> None:
    files = (
        sorted(PLUGIN.rglob("*.md"))
        + sorted((ROOT / "scripts").glob("*"))
        + sorted(ROOT.glob("*.md"))
        + [p for m in MANIFESTS for p in [m] if m.exists()]
    )

    this_file = Path(__file__).resolve()

    for path in files:
        if not path.is_file():
            continue
        # This file necessarily contains every pattern it searches for.
        if path.resolve() == this_file:
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        for needle, description in FORBIDDEN:
            if needle in text:
                report.fail(f"{relative(path)}: contains {description} ('{needle}')")


def check_packages(output_root: Path, report: Report) -> None:
    skills_output = output_root / "skills"
    if not skills_output.is_dir():
        report.fail(f"{relative(output_root)}: no skills/ directory to verify")
        return

    packaged = sorted(p for p in skills_output.iterdir() if p.is_dir())
    expected = {p.name for p in skill_directories()}
    if {p.name for p in packaged} != expected:
        report.fail(
            f"packaged skills {sorted(p.name for p in packaged)} "
            f"do not match source skills {sorted(expected)}"
        )

    for package in packaged:
        if not (package / "LICENSE").exists():
            report.fail(f"{relative(package)}: package is missing LICENSE")
        for document in sorted(package.rglob("*.md")):
            for citation in sorted(set(CITATION.findall(document.read_text()))):
                if not (package / citation).exists():
                    report.fail(
                        f"{relative(document)}: cites {citation}, "
                        "which is missing from the standalone package"
                    )

    report.note(f"{len(packaged)} standalone packages verified self-contained")


def main() -> int:
    report = Report()

    check_manifests(report)
    check_skills(report)
    check_reference_graph(report)
    check_markdown(report)
    check_hygiene(report)

    if len(sys.argv) > 1:
        check_packages(Path(sys.argv[1]).resolve(), report)

    mode = "PyYAML" if HAVE_YAML else "structural (PyYAML unavailable)"
    report.note(f"frontmatter validated via {mode}")

    for note in report.notes:
        print(f"  {note}")

    if report.failures:
        print(f"\n{len(report.failures)} failure(s):", file=sys.stderr)
        for failure in report.failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print("\nRepository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
