#!/usr/bin/env python3
"""Scaffold placeholder slots for a curriculum topic.

This script prepares the *empty containers* that the learning system needs
before a study session reaches a topic. It deliberately creates placeholders
only - no completed teaching content, no runnable code, no pre-generated
explanations.

The slots produced follow the canonical locations defined in
`docs/ARTIFACT_POLICY.md`:

  - `docs/topics/<slug>/README.md`              (durable topic document)
  - `implementations/<lang>/<slug>/README.md`   (learner implementation slot)
  - `solutions/<slug>/README.md`                (problem solution slot)

The topic document placeholder carries the seven structural slots required by
`docs/TOPIC_FORMAT.md` (title and one-line scope, curriculum anchor, required
five-part teaching structure, language coverage table, linked artifacts,
practice and interview notes, last-promoted marker), each marked with a
`<!-- TODO: ... -->` comment so it is unmistakably empty.

Rerun safety: if any target file already exists, the script *skips* it. The
script will never overwrite filled study content. This is the safe default
and there is no `--force` flag - filling a placeholder is the job of a study
session, not of this scaffold.

Usage:

    python scripts/scaffold_topic.py <topic-slug>
    python scripts/scaffold_topic.py <topic-slug> --languages python,java

Run from the repository root so the canonical relative paths resolve.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

DEFAULT_LANGUAGES: Tuple[str, ...] = ("python", "java", "c", "typescript")


def topic_readme_placeholder(slug: str, languages: Iterable[str]) -> str:
    """Build the placeholder content for the durable topic document.

    Every slot required by `docs/TOPIC_FORMAT.md` is present and explicitly
    marked as a TODO. No teaching content is generated.
    """

    rows = "\n".join(
        f"| {lang} | not started | <!-- TODO: link to implementations/{lang}/{slug}/ once it exists --> |"
        for lang in languages
    )

    return f"""# {slug}

<!-- TODO: replace the slug above with the topic title, and add a one-line scope statement here per docs/TOPIC_FORMAT.md item 1. -->

## Curriculum anchor

<!-- TODO: cite the week and priority tier from docs/CURRICULUM.md (item 2 of the topic contract). -->

## Core claim or concept

<!-- TODO: single plain-language statement of what this topic is and why it exists (teaching structure part 1). -->

## Rationale

<!-- TODO: why the core claim holds, Big O for common operations, trade-offs against neighboring topics (teaching structure part 2). -->

## Real example

<!-- TODO: realistic non-toy use case a working engineer would recognize (teaching structure part 3). -->

## Easy example

<!-- TODO: smallest example that strips the topic down to its core mechanic (teaching structure part 4). -->

## Emphasized takeaways

<!-- TODO: short list of points the learner must retain a week later (teaching structure part 5). -->

## Language coverage

| Language | Status | Implementation |
|----------|--------|----------------|
{rows}

<!-- TODO: update the status column (`done` / `draft` / `not started`) and link each row to its implementation file as it lands. -->

## Linked artifacts

<!-- TODO: list runnable implementations under implementations/<lang>/{slug}/ and problem solutions under solutions/{slug}/ as they are produced. One line per entry. -->

## Practice and interview notes

<!-- TODO: sharpened interview answers and recurring problem-solving insights for this topic. Stays inline until the split rule in docs/TOPIC_FORMAT.md fires. -->

## Last promoted

<!-- TODO: record the docs/sessions/<session-id>.md entry that produced the most recent promotion into this document. -->
"""


def implementation_readme_placeholder(slug: str, lang: str) -> str:
    """Placeholder for `implementations/<lang>/<slug>/README.md`.

    The placeholder restates the learner-authored / co-developed contract from
    `docs/ARTIFACT_POLICY.md` so a future session does not accidentally treat
    this folder as a dumping ground for AI-generated code.
    """

    return f"""# {slug} - {lang} implementation slot

<!-- TODO: replace this placeholder with the learner-authored or learner-and-AI co-developed {lang} implementation of `{slug}`. -->

This folder is a placeholder slot created by `scripts/scaffold_topic.py`. It
exists so the canonical location for the {lang} implementation of `{slug}` is
ready when a study session reaches it.

Contract (see `docs/ARTIFACT_POLICY.md`):

- Code in this folder must be **runnable as study code** in {lang}.
- Code in this folder must be **learner-authored or learner-and-AI
  co-developed**, not an unread AI answer dump.
- Code in this folder must exercise the topic `{slug}` specifically.

Pre-generation is explicitly forbidden by `docs/LEARNING_FLOW.md`. Fill this
slot inside the study session that needs it, not before.
"""


def solution_readme_placeholder(slug: str) -> str:
    """Placeholder for `solutions/<slug>/README.md`."""

    return f"""# {slug} - problem solutions slot

<!-- TODO: replace this placeholder with the learner-authored or learner-and-AI co-developed solutions to problems that the `{slug}` topic motivates. -->

This folder is a placeholder slot created by `scripts/scaffold_topic.py`. It
exists so the canonical location for problem solutions tied to `{slug}` is
ready when a study session reaches it.

Solutions are grouped per-topic (not per-language) per `docs/ARTIFACT_POLICY.md`,
so multiple language attempts at the same problem live alongside each other
inside this folder.

Contract (see `docs/ARTIFACT_POLICY.md`):

- Each solution must be **runnable as study code**.
- Each solution must be **learner-authored or learner-and-AI co-developed**.
- Each solution must correspond to a problem the topic `{slug}` motivates.

Do not pre-generate solutions. Fill this slot when a session actually works
through the problem.
"""


def _write_if_absent(path: Path, content: str, created: List[Path], skipped: List[Path]) -> None:
    """Write `content` to `path` only if `path` does not already exist.

    Always ensures the parent directory exists. Records the path into either
    `created` or `skipped` for the run summary.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        skipped.append(path)
        return
    path.write_text(content, encoding="utf-8")
    created.append(path)


def scaffold(slug: str, languages: Iterable[str], root: Path) -> Tuple[List[Path], List[Path]]:
    """Create placeholder slots for `slug` under `root`.

    Returns `(created, skipped)` lists of absolute paths so callers (and the
    test suite) can assert on the outcome.
    """

    languages = tuple(languages)
    created: List[Path] = []
    skipped: List[Path] = []

    topic_doc = root / "docs" / "topics" / slug / "README.md"
    _write_if_absent(
        topic_doc,
        topic_readme_placeholder(slug, languages),
        created,
        skipped,
    )

    for lang in languages:
        impl_doc = root / "implementations" / lang / slug / "README.md"
        _write_if_absent(
            impl_doc,
            implementation_readme_placeholder(slug, lang),
            created,
            skipped,
        )

    solution_doc = root / "solutions" / slug / "README.md"
    _write_if_absent(
        solution_doc,
        solution_readme_placeholder(slug),
        created,
        skipped,
    )

    return created, skipped


def _parse_languages(raw: str) -> Tuple[str, ...]:
    items = tuple(part.strip().lower() for part in raw.split(",") if part.strip())
    if not items:
        raise argparse.ArgumentTypeError("at least one language must be supplied")
    return items


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create placeholder slots for a curriculum topic. "
            "Generates empty containers only; never overwrites filled content."
        )
    )
    parser.add_argument(
        "slug",
        help="Topic slug (matches docs/topics/<slug>/, implementations/<lang>/<slug>/, solutions/<slug>/).",
    )
    parser.add_argument(
        "--languages",
        type=_parse_languages,
        default=DEFAULT_LANGUAGES,
        help=(
            "Comma-separated list of language folders to scaffold under "
            "implementations/. Defaults to the curriculum rotation: "
            f"{','.join(DEFAULT_LANGUAGES)}."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root to scaffold under (defaults to the current working directory).",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = _build_parser().parse_args(list(argv) if argv is not None else None)

    created, skipped = scaffold(args.slug, args.languages, args.root)

    print(f"Scaffolded topic slot: {args.slug}")
    print(f"  Root:      {args.root}")
    print(f"  Languages: {', '.join(args.languages)}")
    if created:
        print(f"  Created ({len(created)}):")
        for path in created:
            print(f"    + {path.relative_to(args.root)}")
    if skipped:
        print(f"  Skipped existing ({len(skipped)}):")
        for path in skipped:
            print(f"    = {path.relative_to(args.root)}")
    if not created and not skipped:
        print("  (nothing to do)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
