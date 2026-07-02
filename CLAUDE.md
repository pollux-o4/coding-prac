# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`coding-prac` is not a software product — it is a one-month, AI-guided CS
interview-prep learning system. The "code" in this repo is mostly tooling
that scaffolds a documentation/artifact structure; the actual deliverables
of a session are Markdown notes and small study implementations. When
working in this repo, Claude Code is usually acting as the AI tutor/guide
described in `docs/LEARNING_FLOW.md`, not as a general software engineer.

Read `docs/CURRICULUM.md`, `docs/PROGRESS.md`, and `docs/LEARNING_FLOW.md`
before doing anything else in a session — they are the durable entrypoints
that define what to work on next and how.

## Document language

Documents the learner actually reads and reviews — topic material
(`docs/topics/<slug>/README.md`) and session summaries (`docs/sessions/*.md`)
— are written in Korean. The system/process docs that define the operating
contract itself (`CURRICULUM.md`, `LEARNING_FLOW.md`, `TOPIC_FORMAT.md`,
`ARTIFACT_POLICY.md`, `PROGRESS.md`, `SESSION_SUMMARY_FORMAT.md`, this file)
stay in English as already written. Inside Korean docs, code, identifiers,
and file paths stay untranslated.

## Commands

There is no build step, linter, or package manifest in this repo. The only
runnable code is the scaffold script and its test suite (stdlib only, no
dependencies to install).

```bash
# Run the scaffold script's tests
python scripts/test_scaffold_topic.py

# Scaffold placeholder slots for a new curriculum topic (default languages: python,java,c,typescript)
python scripts/scaffold_topic.py <topic-slug>
python scripts/scaffold_topic.py <topic-slug> --languages python,java
```

Run a single test case with unittest's `-k`/method selection, e.g.:

```bash
python -m unittest scripts.test_scaffold_topic.ScaffoldTopicTests.test_rerun_does_not_overwrite_filled_content
```

## Architecture: the session flow and artifact contract

Five documents under `docs/` define a closed system that every session
(human- or AI-driven) must follow. Understanding how they reference each
other is more important than any single file's contents:

- **`CURRICULUM.md`** — the fixed study order (DS&A ~70%, OS ~15%, interview
  practice ~15%), the Python → Java → C → TypeScript language rotation per
  topic, and the per-topic "definition of done".
- **`PROGRESS.md`** — the single source of truth for current state (current
  week/topic, per-topic status, next checkpoint, evidence links). It is
  compact by design: it links to evidence, it never copies content. It may
  only be edited via the close-out path below, not ad hoc.
- **`LEARNING_FLOW.md`** — the 3-phase session flow every session follows:
  1. **Select the next checkpoint** by reconciling `PROGRESS.md` against
     `CURRICULUM.md`.
  2. **Just-in-time generation** — create only the topic material the
     selected checkpoint needs, at the granularity it needs. Pre-generating
     material for topics/sections not currently checkpointed is explicitly
     forbidden — this is the single most important constraint in the system.
  3. **Close-out** — promote durable content, place runnable artifacts in
     canonical folders, record links, write a session summary, update
     `PROGRESS.md`, regenerate `progress.html`. A session that doesn't reach
     the last close-out step is treated as not having happened.
- **`TOPIC_FORMAT.md`** — the contract every `docs/topics/<slug>/README.md`
  must satisfy: title+scope, curriculum anchor, a *five-part* teaching
  structure in fixed order (core claim, rationale, real example, easy
  example, emphasized takeaways), a language-coverage table, linked
  artifacts, practice/interview notes, and a last-promoted marker. Only
  learner-validated, stable content gets promoted into this file; the
  practice/interview notes section splits out into a sibling `PRACTICE.md`
  only once it grows past ~10 entries.
- **`ARTIFACT_POLICY.md`** — defines the three kinds of durable artifact and
  their canonical, non-overlapping locations. Content must live in exactly
  one place and be linked from everywhere else, never duplicated:
  - Topic material (explanatory) → `docs/topics/<topic-slug>/README.md`
  - Learner implementation code → `implementations/<language>/<topic-slug>/`
  - Problem-solution code → `solutions/<topic-slug>/` (grouped by topic, not
    by language, so multiple language attempts at one problem stay together)
  - Session summaries (`docs/sessions/<date>-<topic-slug>-<short-slug>.md`,
    format defined in `SESSION_SUMMARY_FORMAT.md`) are a separate, non-topic
    artifact kind.
  Code/notes are preserved in these folders only if the learner actually
  engaged with them (typed/refactored/debugged/explained) — unread AI output
  is not retained as study material. Raw AI transcripts are never stored
  anywhere in the repo.
- **`SESSION_SUMMARY_FORMAT.md`** — every session close-out writes exactly
  one summary file with five required fields in order: learned scope,
  blockers/confusion, changed artifacts, next step, evidence links. The
  "next step" here and `PROGRESS.md`'s "next checkpoint" for that topic must
  agree — they're written in the same close-out step.

`docs/progress.html` is a derived, read-only view generated from
`PROGRESS.md` at load time; it must never hard-code progress state itself,
only structural HTML/labels/loader logic (see the boundary comment at the
top of that file).

`scripts/scaffold_topic.py` creates only the empty placeholder slots (all
`<!-- TODO -->` markers, no content) for a new topic across the three
canonical artifact locations, and is safe to rerun — it skips any file that
already exists rather than overwriting filled-in content.

As of the last commit, `docs/topics/big-o/` (Big O notation and the memory
model) is the only closed-out topic; `implementations/` and `solutions/`
don't exist yet since that topic didn't require code. Current topic per
`docs/PROGRESS.md` is Array (Week 1, Day 3-5), concept stage.
