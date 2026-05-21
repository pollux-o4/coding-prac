# Learning Flow

This is the stable entrypoint for the AI-guided learning session flow. Every
session - whether driven by the learner alone or paired with an AI tutor -
follows the same shape: choose the next checkpoint, generate only the topic
material that the checkpoint needs, then close with durable artifacts and a
refreshed progress view.

The flow is intentionally short. It exists so that two consecutive sessions
do not invent two different ways of working, and so that just-in-time material
generation never drifts into pre-generation.

## Inputs to every session

A session does not start from scratch. It opens against four stable inputs:

1. The curriculum in [CURRICULUM.md](CURRICULUM.md) - study order, weekly
   path, language rotation (Python primary, then Java / C / TypeScript), and
   the per-topic definition of done.
2. The progress state in [PROGRESS.md](PROGRESS.md) - current week, current
   topic, language coverage so far, evidence links, and the next checkpoint
   recorded at the end of the previous session.
3. Any durable topic material already accumulated under `docs/topics/` -
   concept explanations, language-comparison notes, and links from prior
   sessions on the same topic.
4. The topic format in [TOPIC_FORMAT.md](TOPIC_FORMAT.md) - the shape any
   newly written topic material must conform to before it is promoted.

If any of these inputs is missing or inconsistent, the session resolves that
first and does not start studying.

## Phase 1 - Select the next checkpoint

The session selects exactly one next checkpoint by reconciling the curriculum
with the current progress state. The intent is to make this step mechanical
so the learner does not have to re-plan at the start of every session.

The selection rules, applied in order:

1. **Honor the "next checkpoint" field in `PROGRESS.md`** if it is present
   and still valid against the curriculum. The previous session is the
   authority on what comes next.
2. **Otherwise, locate the current position in the curriculum.** Use the
   current week from `PROGRESS.md` and walk the week's day-range from
   [CURRICULUM.md](CURRICULUM.md) until the first item whose definition of
   done is not yet satisfied.
3. **Apply the per-topic definition of done** from `CURRICULUM.md` to decide
   whether the current topic is finished or whether it still needs another
   pass (for example, a missing secondary-language implementation, or fewer
   than three interview-style answers).
4. **Respect the language rotation.** Within a topic, concept comes first,
   then Python, then one of Java / C / TypeScript. A session does not jump
   ahead to a new topic while the current topic's Python implementation is
   missing.
5. **Prefer the smallest unit of progress that still advances a weekly
   checkpoint.** If the week's checkpoint requires "at least five tree
   traversal problems solved", the next checkpoint is the next single problem
   or the next single missing language implementation, not the full
   checkpoint at once.
6. **Fall back to the curriculum's priorities** (data structures and
   algorithms first, OS as a supporting topic, interview practice as the
   third track) when more than one candidate checkpoint exists.

The output of this phase is a single, written-down next checkpoint: a topic,
the artifact the session intends to produce (a concept note, a Python
implementation, a re-implementation in another language, a set of problem
solutions, or an interview-question pass), and the acceptance criterion that
will mark this checkpoint as done.

## Phase 2 - Just-in-time topic material generation

Topic material is generated only when the next checkpoint actually needs it,
and only at the granularity the checkpoint requires. This is the single most
important constraint of the system, because pre-generating material is how
learning systems silently turn into reference manuals nobody reads.

### Where just-in-time generation happens

Just-in-time generation runs inside the session, after Phase 1 has fixed the
next checkpoint and before any implementation or problem solving begins.

For the selected topic:

- If a `docs/topics/<topic-slug>/` folder already exists, the session reads
  the existing material first and only generates the missing slice that the
  current checkpoint needs - for example, a Java re-implementation note when
  Python and the concept already exist.
- If the topic folder does not yet exist, the session creates it from the
  scaffold (minimal `README.md` placeholder following
  [TOPIC_FORMAT.md](TOPIC_FORMAT.md)) and then generates only the section
  that supports the current checkpoint (typically the concept explanation
  plus the first language - Python - that the topic is being studied in).
- Generated content is staged as draft inside the session. Promotion to the
  topic's durable `README.md` happens in Phase 3, after the learner has
  worked with it.

### What must not be pre-generated

The following are explicitly out of scope for just-in-time generation in this
flow, even when it would be cheap to ask the AI to produce them:

- Topic material for topics that are not the current next checkpoint. The
  scaffold creates folders and placeholders, not bodies of explanation.
- Sections of the current topic that the current checkpoint does not need -
  for example, the Java and C re-implementations when the checkpoint is only
  to land the Python implementation.
- Interview questions and problem sets for topics the learner has not yet
  studied at the concept level.
- "Just-in-case" alternative explanations, extra examples, or extended
  trade-off discussion beyond what the checkpoint's acceptance criterion
  requires.
- Bulk batches of topic material across multiple weeks of the curriculum at
  once. The curriculum is the schedule; the topic folders are not a
  pre-built textbook.

If the learner wants more depth than the current checkpoint requires, that
becomes its own next checkpoint in a future session, not an expansion of the
current generation step.

## Phase 3 - Close-out path

A session is only "closed" when it has turned its in-session work into
durable artifacts and a refreshed progress view. Closing is not optional and
is not a free-form summary - it follows a fixed sequence so that the next
session can rely on the same inputs described above.

The close-out steps, in order:

1. **Promote durable topic material.** Take the in-session draft generated
   in Phase 2 and merge into `docs/topics/<topic-slug>/README.md` only the
   parts that meet the promotion criteria: explanations that survived the
   learner's questions, corrected misconceptions, reusable examples,
   implementation insights, recurring mistakes, sharpened interview answers,
   and notes the learner expects to need on next review. Raw AI transcript,
   throwaway scratch work, and one-off rephrasings are not promoted.
2. **Place runnable artifacts in their canonical folders.** Implementation
   code goes under `implementations/<language>/<topic-slug>/`. Problem-set
   solutions go under `solutions/<topic-slug>/`. Topic explanation,
   implementation, and problem-solving artifacts stay separated so the
   topic `README.md` does not become a code dump.
3. **Record artifact links.** From the topic `README.md`, link to the
   relevant implementation files and solution files added in this session,
   so a future session can find them without searching.
4. **Write a session summary.** Create a short entry under `docs/sessions/`
   (one file per session) covering: which checkpoint was worked, what was
   learned or implemented, what was blocked or left open, and what should
   become the next checkpoint. Raw AI transcript is not saved here either.
5. **Update `PROGRESS.md`.** Update the topic's status, language coverage,
   problem-solving evidence, interview-practice evidence, and links to the
   new artifacts and to the session summary written in step 4. Set the
   `next checkpoint` field to the value the session summary identified, so
   Phase 1 of the next session can pick it up directly.
6. **Refresh the progress view.** Regenerate
   [progress.html](progress.html) from `PROGRESS.md` so the visual view
   reflects the new state. `PROGRESS.md` is the source of truth;
   `progress.html` is a derived view and must never lead.

A session that does not reach step 6 is treated as incomplete. The next
session begins by finishing the close-out for the previous session before
starting Phase 1 against a fresh checkpoint.

## Worked example

A short illustration of one pass through the flow, using Week 1 of the
curriculum:

- **Phase 1.** `PROGRESS.md` records that Array concept and Python
  implementation are done, but the Java re-implementation is missing. The
  next checkpoint becomes "Array - Java re-implementation, with one
  trade-off note vs. the Python version."
- **Phase 2.** The session opens `docs/topics/array/README.md`, sees that
  the concept and Python sections already exist, and generates only a Java
  re-implementation note plus the trade-off paragraph. It does not pre-fill
  the C or TypeScript sections.
- **Phase 3.** The Java implementation file is saved under
  `implementations/java/array/`. The topic `README.md` is updated to link
  to it. A short session summary is written under `docs/sessions/`.
  `PROGRESS.md` flips Array's Java coverage to done, sets the next
  checkpoint to the first Linked List checkpoint defined by Week 1, and
  `progress.html` is regenerated.

The next session then starts at Phase 1 against the refreshed `PROGRESS.md`
and does not need to re-derive any of this state.

## Related documents

- [CURRICULUM.md](CURRICULUM.md) - study order, weekly path, language
  rotation, and the per-topic definition of done that Phase 1 uses.
- [TOPIC_FORMAT.md](TOPIC_FORMAT.md) - the shape that any newly generated or
  promoted topic material must follow.
- [PROGRESS.md](PROGRESS.md) - source of truth for progress; the input to
  Phase 1 and the output of Phase 3.
- [progress.html](progress.html) - derived progress view, refreshed in the
  last step of Phase 3.
