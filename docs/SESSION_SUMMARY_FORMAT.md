# Session Summary Format

This is the stable entrypoint that defines the durable session summary
format for the one-month, AI-guided learning system. Every learning session
ends by writing a session summary that conforms to this format, so the next
session can recover what happened without replaying any raw chat transcript.

The format is intentionally small. It exists so that a session's outcome -
what was learned, what got stuck, what changed on disk, what comes next -
becomes a durable artifact at close-out, while the live chat transcript
remains a throwaway working surface.

## What a session summary is for

A session summary is the close-out artifact of a single learning session.
It is read by:

- The **next session** opening against [PROGRESS.md](PROGRESS.md), to
  recover the previous session's context (one summary per session, the most
  recent one is pointed to from the topic's "Latest session" field).
- The **topic document** under `docs/topics/<topic-slug>/README.md`, whose
  last-promoted marker (see [TOPIC_FORMAT.md](TOPIC_FORMAT.md)) points back
  to the session summary that produced the latest promotion.
- A **future review pass** on the same topic, to see what blockers or
  confusions surfaced and whether they have since been resolved.

A session summary is not a meeting note, not a tutorial, and not a copy of
the AI dialogue. It captures the session's outcome compactly enough that
the next session can act on it in seconds.

## Storage location and naming

Every session summary lives as a single Markdown file under
`docs/sessions/`. There is exactly one summary file per session.

The naming convention is:

```
docs/sessions/<YYYY-MM-DD>-<topic-slug>-<short-slug>.md
```

- `<YYYY-MM-DD>` is the session's local date, so a directory listing reads
  in chronological order.
- `<topic-slug>` matches the topic folder under `docs/topics/`, so a future
  session can find every summary that touched a given topic by prefix.
- `<short-slug>` is a 2-4 word kebab-case marker of what the session did
  (for example, `array-python-impl`, `linked-list-concept`,
  `bigo-followups`). It exists so two sessions on the same date and topic
  can be told apart without opening either file.

Sessions that span more than one topic still produce exactly one summary;
the file uses the primary topic in the filename and the secondary topic is
recorded inside the "learned scope" section. Sessions are not retroactively
renamed or moved; once a summary is written, its path is stable.

## Required fields

Every session summary has exactly the following five fields, in this order
and individually labeled. A summary missing any field is treated as
incomplete; the close-out path is not finished until all five are present.

### 1. Learned scope

A short, plain-language record of what the session actually covered. This
field answers "what did this session work on, and against which
checkpoint".

Concretely, it states:

- The checkpoint that was being worked, as selected in Phase 1 of
  [LEARNING_FLOW.md](LEARNING_FLOW.md) (topic, target artifact, acceptance
  criterion).
- What of that checkpoint was actually completed in the session, in one to
  three sentences.
- Any secondary topic the session touched, if the work crossed a topic
  boundary.

This field is written even when the session did not finish its checkpoint -
in that case it records the partial progress and the "next step" field
records what remains.

### 2. Blockers or confusion

A short, honest record of what got stuck, what was misunderstood, and what
the learner is still uncertain about. This field is the one that most
distinguishes a session summary from a triumphant changelog.

It captures:

- Wrong mental models the session had to correct (briefly, so the next
  session can recognize the same trap).
- Questions that were raised but not resolved, and the reason they were
  deferred.
- Tooling or environment friction that slowed the session down enough to
  matter to a future session.

"None this session" is an acceptable value; leaving the field out is not.

### 3. Changed artifacts

A list of the durable artifacts the session created or modified, by path.
This field is what makes the summary actionable without re-running any
commands or scanning the working tree.

Each entry is one line of the form:

```
<path> - <create | update | promote> - <short reason>
```

The artifacts that belong in this list are the ones the close-out path in
[LEARNING_FLOW.md](LEARNING_FLOW.md) produces or touches:

- Topic material under `docs/topics/<topic-slug>/` (especially promotions
  into `README.md`).
- Implementation code under `implementations/<language>/<topic-slug>/`.
- Problem-set solutions under `solutions/<topic-slug>/`.
- The session summary file itself does not list itself.
- [PROGRESS.md](PROGRESS.md) is always changed by a close-out; it is listed
  for completeness but does not need a per-field breakdown - the
  per-topic-field changes belong in PROGRESS.md itself, not duplicated here.

If a file was created and immediately abandoned (for example, a scratch
draft that never got promoted), it is not listed. Only durable changes
appear.

### 4. Next step

The single next checkpoint identified by the session, written so that
Phase 1 of the next session can honor it directly. This is the same value
that the close-out path writes into the "Next checkpoint" field of the
relevant topic row in [PROGRESS.md](PROGRESS.md); the two must agree.

The next step records:

- The topic the next checkpoint belongs to.
- The specific artifact the next session is expected to produce (for
  example, "Java re-implementation of `array` with one trade-off note vs.
  the Python version", not "more arrays").
- The acceptance criterion that will mark that checkpoint as done.

If a session ends without a clear next step (for example, the curriculum
just crossed a week boundary and the next topic has not been opened yet),
the next step field still names a concrete first move - typically "open the
first topic of Week N from [CURRICULUM.md](CURRICULUM.md) and scaffold its
folder". An empty next step is not allowed.

### 5. Evidence links

A short list of links that back up the session summary's claims. Evidence
is what lets a future session trust the summary without re-running the
session.

Typical entries:

- The topic `README.md` whose promotion this session caused.
- The implementation file(s) added or updated.
- The problem-set solution file(s) added.
- A specific commit hash or pull request, when the session's changes were
  pushed.
- An external reference (book chapter, paper section, course lesson) that
  the learner consulted, when the session relied on it.

Evidence links are bare links or short Markdown links; they are not
annotated explanations. The annotation lives in the surrounding field that
referenced the link.

## Integration with the progress contract

The session summary integrates with [PROGRESS.md](PROGRESS.md) by being
**linked from** the per-topic "Latest session" field, never copied into it.

The integration rules are:

- The "Latest session" field in `PROGRESS.md` holds a link to exactly one
  session summary file under `docs/sessions/`, plus its date. Older
  summaries for the same topic stay in the folder but are not pointed at
  from `PROGRESS.md`.
- `PROGRESS.md` does not embed any field of the session summary inline. In
  particular, the long-form text of "learned scope", "blockers or
  confusion", and the evidence-link list never appears in `PROGRESS.md`.
  Those belong in the summary file.
- The session summary's "next step" field and `PROGRESS.md`'s "Next
  checkpoint" field for the same topic carry the same checkpoint. They are
  written together in the same close-out step (Phase 3, step 5 of
  [LEARNING_FLOW.md](LEARNING_FLOW.md)) and must not be allowed to drift.
- Topic `README.md` files reference session summaries through their
  last-promoted marker, as defined in [TOPIC_FORMAT.md](TOPIC_FORMAT.md).
  That reference is the second supported link into `docs/sessions/`; the
  first is the `PROGRESS.md` "Latest session" field.

This boundary preserves the progress contract's second part: `PROGRESS.md`
stays compact and does not carry long logs. The session summary is the
durable place where the long-ish narrative of a session lives.

## Raw AI transcripts are not durable artifacts

The raw transcript of the AI tutor session - the back-and-forth chat
between the learner and the AI - is not a durable learning artifact and is
not stored under `docs/sessions/`, `docs/topics/`, or anywhere else in the
repository.

The reasons are intentional, not incidental:

- **Volume.** A single session's transcript easily exceeds the entire
  durable artifact set for the topic it covered. Keeping transcripts would
  swamp the durable surface, exactly the failure mode the progress
  contract is set up to prevent.
- **Signal-to-noise.** Most lines in a transcript are scaffolding, false
  starts, rephrasings, and corrections the learner has already absorbed.
  The session summary is the deliberate distillation of the signal.
- **Promotion direction.** [TOPIC_FORMAT.md](TOPIC_FORMAT.md) already
  states that raw AI transcript is never promoted into a topic document.
  This format extends that rule outward: the transcript does not live as
  its own first-class artifact either.

If a specific exchange from a session needs to survive (a sharpened
interview answer, a corrected misconception, a worked example), the
mechanism is promotion into a topic `README.md` or capture as a labeled
field inside the session summary - not preserving the transcript verbatim.

A session that ends without producing a session summary conforming to this
format is treated the same as a session that did not happen: the next
session cannot recover its state, and the close-out path of
[LEARNING_FLOW.md](LEARNING_FLOW.md) is not considered finished.

## Related documents

- [LEARNING_FLOW.md](LEARNING_FLOW.md) - the close-out path that writes the
  session summary (Phase 3, step 4) and reads it on the next session.
- [PROGRESS.md](PROGRESS.md) - the source of truth that links to the latest
  session summary per topic and carries the matching "Next checkpoint"
  field.
- [TOPIC_FORMAT.md](TOPIC_FORMAT.md) - the topic document format whose
  last-promoted marker points back at the session summary that produced the
  promotion.
- [CURRICULUM.md](CURRICULUM.md) - the study order and per-topic definition
  of done that the session summary's "next step" field is written against.
