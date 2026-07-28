#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and agents/openai.yaml interface metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = PROJECT_ROOT / "SKILL.md"
OPENAI_YAML = PROJECT_ROOT / "agents" / "openai.yaml"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
INTERFACE_PATTERN = re.compile(
    r'^\s{2}(display_name|short_description|default_prompt):\s*"([^"]+)"\s*$'
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    """Parse the constrained two-field frontmatter used by Codex skills."""
    findings: list[str] = []
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter"]

    closing = normalized.find("\n---\n", 4)
    if closing == -1:
        return {}, ["SKILL.md frontmatter has no closing delimiter"]

    block = normalized[4:closing]
    keys = re.findall(r"^([a-z][a-z0-9_-]*):", block, flags=re.MULTILINE)
    if set(keys) != {"name", "description"} or len(keys) != 2:
        findings.append("SKILL.md frontmatter must contain only name and description")

    name_match = re.search(r"^name:\s*(\S+)\s*$", block, flags=re.MULTILINE)
    description_match = re.search(
        r"^description:\s*(?:>-\s*\n)?(?P<value>(?:[ \t]+.+(?:\n|$))+|.+$)",
        block,
        flags=re.MULTILINE,
    )
    metadata = {
        "name": name_match.group(1).strip() if name_match else "",
        "description": (
            " ".join(line.strip() for line in description_match.group("value").splitlines())
            if description_match
            else ""
        ),
    }
    return metadata, findings


def parse_interface(text: str) -> dict[str, str]:
    """Read the three required quoted interface fields."""
    return {
        match.group(1): match.group(2)
        for line in text.splitlines()
        if (match := INTERFACE_PATTERN.match(line))
    }


def run_checks() -> list[str]:
    findings: list[str] = []
    metadata, parse_findings = parse_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    findings.extend(parse_findings)

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        findings.append("Skill name must use lowercase letters, digits, and hyphens")
    if name != PROJECT_ROOT.name:
        findings.append(f"Skill name '{name}' must match folder '{PROJECT_ROOT.name}'")
    if not description:
        findings.append("Skill description must not be empty")
    if len(SKILL_MD.read_text(encoding="utf-8").splitlines()) > 500:
        findings.append("SKILL.md must stay within the 500-line progressive-disclosure limit")

    interface = parse_interface(OPENAI_YAML.read_text(encoding="utf-8"))
    required = {"display_name", "short_description", "default_prompt"}
    missing = required - interface.keys()
    if missing:
        findings.append(f"agents/openai.yaml is missing: {', '.join(sorted(missing))}")
        return findings

    short_description = interface["short_description"]
    if not 25 <= len(short_description) <= 64:
        findings.append("short_description must contain 25-64 characters")
    if f"${name}" not in interface["default_prompt"]:
        findings.append(f"default_prompt must explicitly mention ${name}")

    return findings


def main() -> int:
    findings = run_checks()
    if findings:
        print("Skill metadata validation failed:")
        for finding in findings:
            print(f"  [FAIL] {finding}")
        return 1

    print("Skill metadata validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
