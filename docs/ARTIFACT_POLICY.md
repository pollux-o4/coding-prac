# Artifact Policy

This is the stable entrypoint that defines the artifact boundary for the
one-month, AI-guided learning system. Every session - whether driven by the
learner alone or paired with an AI tutor - stores its work in one of three
artifact kinds, in one of three canonical locations, and links between them
rather than duplicating content.

The policy is intentionally narrow. It exists so that repeated study
sessions on the same topic accumulate into a sharper topic document and a
growing set of runnable artifacts, instead of into parallel piles of notes
that drift apart.

## The three artifact kinds

The system recognizes exactly three kinds of durable artifact. Every piece
of content produced by a session belongs to exactly one of them, and each
kind has its own canonical location and its own retention rules.

| Artifact kind | What it holds | Canonical location |
|---------------|---------------|--------------------|
| Topic material (explanatory) | Promoted concept notes, rationale, real and easy examples, takeaways, language-comparison notes, interview answers, and the language-coverage table that points at implementation evidence. | `docs/topics/<topic-slug>/README.md` (and `PRACTICE.md` once the split rule in [TOPIC_FORMAT.md](TOPIC_FORMAT.md) fires). |
| Learner implementation code | Runnable, learner-written or learner-and-AI co-developed implementations of the data structure, algorithm, or OS-concept demo that the topic teaches. | `implementations/<language>/<topic-slug>/`, one folder per language in the rotation (Python primary, then Java, C, TypeScript). |
| Problem solution code | Runnable solutions to problem-set questions (LeetCode-style or interview-style) that the topic motivates. | `solutions/<topic-slug>/`, grouped by topic rather than by language so that multiple language attempts at the same problem stay together. |

These three kinds line up with the per-topic definition of done in
[CURRICULUM.md](CURRICULUM.md) (concept explained, language implementations
landed, problems solved) and with the close-out steps in
[LEARNING_FLOW.md](LEARNING_FLOW.md) (promote durable topic material, then
place runnable artifacts in their canonical folders, then record artifact
links).

Two locations referenced elsewhere in the system are intentionally outside
this taxonomy because they are not topic-scoped durable artifacts:

- `docs/sessions/<session-id>.md` is a session summary, not a topic
  artifact. It records what happened in one session and what should become
  the next checkpoint. It is governed by step 4 of the close-out path in
  [LEARNING_FLOW.md](LEARNING_FLOW.md).
- [PROGRESS.md](PROGRESS.md) is the compact index over the three artifact
  kinds. It points at them; it does not contain them. The evidence-link
  boundary defined in `PROGRESS.md` is the read side of the same boundary
  this document defines on the write side.

## Boundary between topic material and code artifacts

Topic material explains; code artifacts run. The boundary is enforced by
where each kind of content lives and by what each kind of content is
allowed to contain.

### What topic material is for

Topic material under `docs/topics/<topic-slug>/` is explanatory. It carries
the five-part teaching structure required by [TOPIC_FORMAT.md](TOPIC_FORMAT.md)
(core claim, rationale, real example, easy example, emphasized takeaways),
the language-coverage table, the linked-artifacts section, and the
practice-and-interview notes.

Topic material is allowed to contain:

- Plain-language explanation of the topic in the five labeled teaching
  parts.
- Short illustrative snippets - the smallest fragment that makes a teaching
  point land, such as a three-line loop showing the index arithmetic of an
  array or a single recursive definition of tree depth. These snippets are
  pedagogical, not runnable; they are not expected to be a complete program
  and are not what `implementations/` exists to hold.
- The language-coverage table listing Python, Java, C, and TypeScript with
  per-language status and a link to each language's implementation folder.
- The linked-artifacts section listing the runnable implementations and
  problem solutions for this topic.
- Sharpened interview answers and recurring problem-solving insights, per
  the practice-and-interview notes rules in [TOPIC_FORMAT.md](TOPIC_FORMAT.md).

Topic material is not allowed to contain:

- A full runnable implementation of the topic. If a code block is large
  enough to compile and run as a program, it belongs under
  `implementations/<language>/<topic-slug>/` and is linked from the topic
  document instead.
- A full problem solution. Even when a topic motivates a specific
  LeetCode-style question, the solution code lives under
  `solutions/<topic-slug>/` and is linked from the topic document.
- Re-pasted copies of code that already exists under `implementations/` or
  `solutions/`. The topic document links to that code; it does not mirror
  it.
- Raw AI transcript, throwaway scratch work, or "just-in-case" alternative
  explanations. Promotion rules in [TOPIC_FORMAT.md](TOPIC_FORMAT.md)
  already forbid these; this policy reinforces that they are also not
  allowed to leak into the topic document as code blocks.

### What learner implementation code is for

`implementations/<language>/<topic-slug>/` holds runnable, learner-authored
or learner-and-AI co-developed implementations of the topic itself - the
data structure, algorithm, or OS-concept demo that the topic teaches.

These artifacts have two non-negotiable properties:

1. **Runnable as study code.** The implementation runs on its own in the
   target language, exercises the topic's main operations, and is shaped
   so the learner can read it back later. It is not just a syntactic copy
   of a reference implementation.
2. **Learner-authored or co-developed, not an answer dump.** The code is
   produced by the learner working through the topic, optionally with AI
   assistance during the session. Code that the learner pasted in without
   working through, or that the AI generated end-to-end without the
   learner stepping through it, is not preserved here. The retention
   criterion is "this is study code the learner can defend on a re-read",
   not "this compiles".

The "co-developed" allowance exists because the curriculum explicitly
assumes AI-assisted study. AI is a legitimate collaborator inside the
session. What the policy forbids is using `implementations/` as a place to
dump AI output that the learner did not engage with. The test is the same
as for topic material: if the learner cannot defend the code on a future
review pass, it does not belong in the durable folder.

One folder per language exists because the curriculum's language rotation
(Python first, then Java, C, TypeScript) is the explicit unit of progress.
Re-implementing the same topic in a second language is a checkpoint, and
the artifact for that checkpoint is the new language folder, not an
addition to the Python folder.

### What problem solution code is for

`solutions/<topic-slug>/` holds runnable solutions to problem-set
questions (LeetCode-style or interview-style) that the topic motivates.

Problem solutions are kept separate from implementation code for two
reasons:

1. The per-topic definition of done in [CURRICULUM.md](CURRICULUM.md)
   counts implementation coverage and problem-solving coverage as
   independent dimensions. Keeping them in separate folders makes the
   counts trivially auditable from `PROGRESS.md`.
2. Problem solutions accumulate per problem, not per language. A single
   problem may be solved in Python, then re-solved in Java as part of a
   later language-rotation pass; grouping by topic-slug keeps the
   different attempts together and avoids forcing the learner to navigate
   four parallel `solutions/<language>/` trees.

Problem solutions follow the same retention rule as implementation code:
they are learner-authored or learner-and-AI co-developed study code. A
pasted answer that the learner did not work through is not a problem
solution under this policy.

## Implementation artifacts: learner-authored or co-developed, not answer dumps

The most common way a learning system silently breaks is by accumulating
code the learner did not actually work through. This policy treats that
failure mode explicitly.

Implementation artifacts and problem solutions are preserved in their
canonical folders only when all of the following hold:

- **Learner engagement.** The learner stepped through the code during the
  session - typed it, refactored it, debugged it, or at minimum read it
  line by line and explained back what each section does. Pure AI output
  the learner watched scroll past is not engagement.
- **Defensibility on review.** The learner expects to be able to re-read
  the file on a later session and reconstruct the reasoning behind the
  non-obvious lines. If the file has a section the learner cannot explain
  the day after the session, that section is either reworked or removed
  before close-out.
- **Topic fit.** The code exercises the topic the session is studying.
  Drive-by snippets from unrelated topics ("here is a quick hash map
  example while we are talking about arrays") are not promoted into the
  topic's implementation folder.
- **Runnable as study code.** The file runs in its language without
  hand-editing and produces an observable result the learner can check
  against the topic's operation profile. A partial sketch that does not
  run is left in the session draft, not promoted.

When a piece of code fails any of these criteria, the close-out path does
not place it in `implementations/<language>/<topic-slug>/` or in
`solutions/<topic-slug>/`. It either stays in the session draft and is
referenced from the session summary, or it is dropped. This is the same
shape of rule that [TOPIC_FORMAT.md](TOPIC_FORMAT.md) applies to topic
material promotion: only learner-validated, structure-fitting work is
preserved.

The "learner-and-AI co-developed" allowance is therefore not a loophole.
AI participation in the session is expected; AI generation that the
learner did not engage with is the failure mode this rule blocks.

## Evidence linking without content duplication

Topic material connects to implementation and solution evidence through
links, not through content duplication. The topic document is the reading
surface; the runnable folders are the evidence; `PROGRESS.md` is the
compact index.

### How topic material links to evidence

The durable topic document at `docs/topics/<topic-slug>/README.md` carries
two structural slots defined by [TOPIC_FORMAT.md](TOPIC_FORMAT.md) that
exist specifically to hold these links:

1. **Language coverage table.** One row per language in the rotation
   (Python primary, then Java, C, TypeScript), each with a status flag and
   a link to that language's folder under
   `implementations/<language>/<topic-slug>/`. The table answers "which
   languages cover this topic and where is each implementation" without
   inlining any code.
2. **Linked artifacts section.** A short list of the implementation files
   and the problem-solution files that belong to this topic. Each entry is
   a path link plus, at most, a one-line description of what the file
   demonstrates. The section is a directory, not a summary; it does not
   restate what the linked file does beyond the one-line label.

When a session promotes new content into the topic document during
close-out, it updates these two slots to point at the new runnable
artifacts it created. The five-part teaching structure (core claim,
rationale, real example, easy example, takeaways) does not absorb the new
code; it absorbs only the explanatory takeaways that working on that code
produced.

### How `PROGRESS.md` links to evidence

[PROGRESS.md](PROGRESS.md) carries three evidence fields per started
topic:

- **Implementation evidence** points at one file per language under
  `implementations/<language>/<topic-slug>/`.
- **Solution evidence** points at the running list under
  `solutions/<topic-slug>/`, with a count.
- **Interview / review evidence** points at the answers and mock-interview
  notes recorded inside `docs/topics/<topic-slug>/README.md` (or
  `PRACTICE.md` once split) or under `docs/sessions/`, with a count.

These three fields are the read-side of the boundary that this policy
defines on the write-side. They are links, not copies, for the same
reason the topic document's linked-artifacts section is links: the
progress document is read at the start of every session, and a document
that copies its evidence drifts from the evidence over time.

### No-duplication rule

The combination of the rules above produces a single, enforceable
no-duplication rule:

- A piece of code exists in exactly one canonical location -
  `implementations/<language>/<topic-slug>/` for implementation code, or
  `solutions/<topic-slug>/` for problem-set solutions.
- A piece of explanatory content exists in exactly one canonical location
  - the topic document at `docs/topics/<topic-slug>/README.md` (or, once
  split, `PRACTICE.md`).
- Everything else that needs to refer to either of the above does so by
  link. The topic document links to runnable artifacts. `PROGRESS.md`
  links to all three artifact kinds plus session summaries. Session
  summaries link to the artifacts the session produced.

A session that finds itself about to paste implementation code into the
topic document, or about to re-explain a topic in a session summary, is
applying the boundary backwards and should link to the canonical artifact
instead.

## How this document is used

- [LEARNING_FLOW.md](LEARNING_FLOW.md) references this policy at step 2 of
  the close-out path ("place runnable artifacts in their canonical
  folders") and at step 3 ("record artifact links"). The close-out path
  uses the three canonical locations and the linking rules defined here.
- [TOPIC_FORMAT.md](TOPIC_FORMAT.md) references this policy for the
  language-coverage table and the linked-artifacts section. Those slots
  hold the links described in "Evidence linking without content
  duplication" above.
- [PROGRESS.md](PROGRESS.md) references this policy for its evidence-link
  boundary. The three evidence fields in `PROGRESS.md` point at the three
  artifact kinds defined here.
- [CURRICULUM.md](CURRICULUM.md) references this policy indirectly through
  its per-topic definition of done: language coverage is satisfied by
  artifacts under `implementations/<language>/<topic-slug>/`, and
  problem-solving counts are satisfied by artifacts under
  `solutions/<topic-slug>/`.

This policy is intentionally stable. Changes to the three artifact kinds,
their canonical locations, or the no-duplication rule are made
deliberately and are reflected across `LEARNING_FLOW.md`,
`TOPIC_FORMAT.md`, and `PROGRESS.md` in a dedicated session, not silently
during a normal topic close-out.
