#!/usr/bin/env python3
"""Validate the public Atropos Command skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "templates/mission-brief.md",
    "references/persona-and-command.md",
    "references/orchestration-protocol.md",
    "references/anti-bloat-and-context.md",
    "references/evidence-and-impossibility.md",
    "references/agent-motivation-and-command.md",
    "references/leadership-canon.md",
    "examples/software-release.md",
)
FORBIDDEN_PUBLIC_PATTERNS = (
    "/Users/",
    "BEGIN PRIVATE KEY",
    "api_key=",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r'^---\nname: "([^"]+)"\ndescription: "([^"]+)"\n---\n', skill)
    if not match:
        fail("SKILL.md must begin with exact name and description frontmatter")

    name, description = match.groups()
    if name != "atropos-command":
        fail(f"unexpected skill name: {name}")
    if len(name) > 64:
        fail("skill name exceeds 64 characters")
    if len(description) > 1024:
        fail("skill description exceeds 1024 characters")
    if "Use" not in description and "use" not in description:
        fail("description must explain when to use the skill")

    public_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]
    for path in public_files:
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ""}:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PUBLIC_PATTERNS:
            if pattern in text:
                fail(f"private pattern {pattern!r} found in {path.relative_to(ROOT)}")

    print("PASS: Atropos Command package is complete, generic, and public-safe.")


if __name__ == "__main__":
    main()
