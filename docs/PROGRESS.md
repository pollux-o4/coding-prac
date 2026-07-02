# Progress

This file is the source of truth for learner progress. Every later learning
session, every AI tutor pass, and every visualization derives current study
state from this document. Topic folders, session summaries, implementation
code, and solution files are the durable artifacts; this document is the
compact index over them.

The local derived view entrypoint is [progress.html](progress.html).
`progress.html` is regenerated from this file and must never lead.

## Contract

The progress contract has three parts.

1. **This document is the current-state source of truth.** When a later
   session or visualization needs to know "where is the learner right now,
   on which topic, in which language, with what next step", it reads this
   document and nothing else. If this document disagrees with any other
   artifact (a topic `README.md`, a session summary, a derived view), this
   document wins and the other artifact is corrected to match.
2. **This document is compact.** It records the minimum per-topic fields
   defined below and links out to detailed artifacts. It does not copy
   topic explanations, full session transcripts, or implementation code.
   Anything large lives in its own durable location and is referenced from
   here by link.
3. **This document is updated only through the
   [LEARNING_FLOW.md](LEARNING_FLOW.md) close-out path.** Step 5 of Phase 3
   ("Update `PROGRESS.md`") is the single supported write path. Ad-hoc
   edits outside the close-out flow are not part of the contract.

## Minimum per-topic fields

Every topic that has been started carries the following seven fields. Topics
that have not been started yet do not appear; the
[CURRICULUM.md](CURRICULUM.md) ordering implies them. A topic is considered
"started" the first time the close-out path writes any of these fields for
it.

| Field | What it records | Why later sessions need it |
|-------|-----------------|----------------------------|
| Current state | Where this topic stands against its per-topic definition of done in [CURRICULUM.md](CURRICULUM.md): concept understood yes/no, which languages are covered, problem and interview counts so far. | Lets Phase 1 of the next session decide whether the topic is finished or still needs another pass without re-reading the topic folder. |
| Next checkpoint | A single, written-down next checkpoint for this topic: the artifact the next session intends to produce and the acceptance criterion that will mark it done. Mirrors the Phase 1 output described in [LEARNING_FLOW.md](LEARNING_FLOW.md). | Lets the next session honor the "next checkpoint" rule in Phase 1 without re-deriving it. |
| Topic material | Link to `docs/topics/<topic-slug>/README.md` (and the folder beneath it). The promoted concept notes, language-comparison notes, and interview answers live there. | Lets the next session locate existing durable material instead of regenerating it. |
| Latest session | Link to the most recent session summary under `docs/sessions/` that worked on this topic, plus its date. Older sessions remain in the folder; only the latest pointer lives here. | Lets the next session pick up the previous session's context without scanning all session summaries. |
| Implementation evidence | Links to the implementation files added so far for this topic, grouped by language (Python primary, then Java / C / TypeScript). One link per language is enough; the file itself is the evidence. | Lets the next session see language coverage against the rotation in [CURRICULUM.md](CURRICULUM.md). |
| Solution evidence | Links to the problem-set solutions written so far for this topic under `solutions/<topic-slug>/`, with a running count. | Lets the next session check the problem-solving counts that the per-topic definition of done and weekly checkpoints require. |
| Interview / review evidence | Links to the interview-style answers and any mock-interview notes recorded so far for this topic, with a running count. Lives inside the topic `README.md` or under `docs/sessions/`; this field is the pointer. | Lets the next session check the interview-question counts that the per-topic definition of done requires. |

A row whose value is "none yet" is acceptable as long as the field is
present. Missing fields are not acceptable; they break the contract.

In addition to the per-topic rows, this document carries two top-level
fields that the next session reads first:

- **Current week.** Which week of [CURRICULUM.md](CURRICULUM.md) the
  learner is in. Phase 1 uses this to locate the current position.
- **Current topic.** Which topic is active. Phase 1 honors this together
  with the topic's "next checkpoint" field before consulting the
  curriculum.

## Evidence-link boundary

The progress document points at evidence; it does not contain it. The
boundary is:

- **In this document.** Status flags, counts, the next-checkpoint
  description, the current week and topic, and one link per piece of
  evidence. Roughly one short table row per started topic.
- **Not in this document.** Topic explanations, full implementation code,
  problem solutions, raw AI transcripts, full session narratives. Each of
  these stays in its own durable location:
  - Topic material - `docs/topics/<topic-slug>/README.md` and the rest of
    that folder.
  - Implementation code - `implementations/<language>/<topic-slug>/`.
  - Problem solutions - `solutions/<topic-slug>/`.
  - Session summaries - `docs/sessions/`.
  - Curriculum and definition of done - [CURRICULUM.md](CURRICULUM.md).
  - Per-session flow - [LEARNING_FLOW.md](LEARNING_FLOW.md).
  - Topic note shape - [TOPIC_FORMAT.md](TOPIC_FORMAT.md).

The reason for this boundary is that the progress document is read at the
start of every session and rendered into [progress.html](progress.html).
If it copies content from its evidence sources, it drifts from them and
stops being a reliable source of truth. Links are stable; copies are not.

## How this document is updated

This document is written by the close-out path in
[LEARNING_FLOW.md](LEARNING_FLOW.md), Phase 3, step 5. Each close-out:

1. Updates the affected topic's row, touching only the fields that
   changed.
2. Sets that topic's "next checkpoint" field to the value the session
   summary identified.
3. Updates the top-level current week and current topic if the session
   crossed a boundary.
4. Triggers regeneration of [progress.html](progress.html) as the next
   step of the close-out.

Sessions do not edit this document outside the close-out path, and they do
not move content from this document into a topic `README.md` or a session
summary - the direction of the link is always from this document outward.

## Current state

**Current week:** Week 1 - Foundations and linear structures.
**Current topic:** Array.

### Big O notation and the memory model

| Field | Value |
|-------|-------|
| Current state | Concept and memory model both covered as of 2026-07-02: complexity-class intuition (O(1), O(n), O(n^2), O(n^3), O(log n), O(n log n)) plus stack/heap, references, and allocation/deallocation. 3/3 code snippets correctly classified by Big O as hands-on practice (after self-correction). This is a prep topic, not a core data structure, so no implementation/problem/interview evidence is expected per its curriculum entry. Checkpoint closed; moving to Array. |
| Next checkpoint | none - checkpoint closed. |
| Topic material | [docs/topics/big-o/README.md](topics/big-o/README.md) |
| Latest session | [2026-07-02 session summary](sessions/2026-07-02-big-o-memory-model-and-practice.md) - 2026-07-02 |
| Implementation evidence | none yet |
| Solution evidence | none yet (0 problems solved) |
| Interview / review evidence | none yet (0 interview-style answers) |

### Array

| Field | Value |
|-------|-------|
| Current state | Concept covered as of 2026-07-02. Python implementation covered as of 2026-07-02. Java implementation also covered as of 2026-07-03: `MyArray` class with `data` (fixed-size array) + `size` (used-count) fields, `get`/`set` (O(1)), `insert`/`delete` (O(n)), and `grow()` for capacity doubling; `get`/`set`/`delete` hand-typed by the learner, `insert`/`grow` co-developed and verified by the learner via debugger stepping. Learner stated the Python-vs-Java trade-off unprompted (Java needs manual capacity management via `grow()`; Python's list hides this). No C/TypeScript implementation, no problems solved, no interview-style answers yet. |
| Next checkpoint | Solve the first Array practice problem end-to-end under `solutions/array/`, with the learner explaining their approach and stating its time complexity. Acceptance criterion: one problem solved and its complexity correctly stated by the learner. |
| Topic material | [docs/topics/array/README.md](topics/array/README.md) |
| Latest session | [2026-07-03 session summary](sessions/2026-07-03-array-java-impl.md) - 2026-07-03 |
| Implementation evidence | [Python](../implementations/python/array/my_array.py), [Java](../implementations/java/array/MyArray.java) |
| Solution evidence | none yet (0 problems solved) |
| Interview / review evidence | none yet (0 interview-style answers) |
