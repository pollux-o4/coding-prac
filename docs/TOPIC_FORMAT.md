# Topic Format

This is the stable entrypoint that defines the durable topic material format
for the one-month, AI-guided learning system. Every topic folder under
`docs/topics/<topic-slug>/` follows this format so that repeated sessions
sharpen the same artifact instead of producing parallel notes.

The format is intentionally small. It exists to keep topic material readable
at the curriculum's high pace, while making explicit which content is stable
enough to survive across sessions and which is still a draft.

## Durable topic document contract

Every topic has exactly one durable document at
`docs/topics/<topic-slug>/README.md`. That file is the minimum contract.

The contract requires, in order:

1. **Title and one-line scope.** The topic name and a single sentence
   describing what the document covers and, when relevant, what it does not
   (for example, "covers arrays as a contiguous-memory data structure; sorting
   algorithms over arrays live in their own topic").
2. **Curriculum anchor.** A short reference to where this topic sits in
   [CURRICULUM.md](CURRICULUM.md): the week and the priority tier (core data
   structure, extended data structure, algorithm, OS concept, or interview
   practice). This makes the document navigable from the curriculum without
   re-deriving the position each time.
3. **Required teaching structure** (see the next section). This is the body
   of the document and is non-negotiable.
4. **Language coverage table.** A small table listing Python (primary) plus
   Java, C, and TypeScript, with a status per language (`done`, `draft`, or
   `not started`) and a link to the implementation file under
   `implementations/<language>/<topic-slug>/` when it exists. The table is
   the topic's view of the per-topic definition of done from `CURRICULUM.md`.
5. **Linked artifacts.** Links to the runnable implementations and to any
   problem-set solutions under `solutions/<topic-slug>/` that belong to this
   topic. Code itself is not inlined into the topic document; the topic
   document points to it.
6. **Practice and interview notes section.** A single section that holds
   sharpened interview answers and recurring problem-solving insights for
   this topic. Splitting rules for this section are stated below.
7. **Last-promoted marker.** A short trailer recording when the document was
   last promoted in a close-out and which session summary under
   `docs/sessions/` produced that promotion. The marker exists so the next
   session can tell at a glance whether the document is freshly stable or
   stale.

A topic document missing any of these seven items is treated as a draft and
is not considered durable, even if its content is otherwise good.

## Required teaching structure

The body of the topic document follows a fixed five-part teaching structure.
The structure is preserved across every topic, regardless of whether the
topic is a data structure, an algorithm, an OS concept, or an interview
pattern, so that the learner sees the same shape on every review.

1. **Core claim or concept.** A single, plain-language statement of what the
   topic is and why it exists. For a data structure, this is the shape and
   the operation profile (for example, "an array is a contiguous block of
   memory indexed in O(1)"). For an algorithm, it is the invariant the
   algorithm maintains.
2. **Rationale.** Why the core claim holds and what it buys the learner.
   This section covers Big O for the common operations, the trade-offs
   against neighboring topics, and the situations in which the topic is the
   right choice. The rationale is allowed to evolve session over session;
   that is one of the main reasons promotion exists.
3. **Real example.** A realistic, non-toy use case that a working engineer
   would recognize - ideally one the learner has seen or is likely to see in
   interviews or in production-shaped problems. The example shows the topic
   in context, not in isolation.
4. **Easy example.** A deliberately small, minimal example that strips the
   topic down to its core mechanic. This example is what the learner
   re-reads on a fast pass and is what an interview answer can be anchored
   to under time pressure.
5. **Emphasized takeaways.** A short, explicitly marked list of the points
   the learner must retain after closing the document - the lines that
   should still be remembered a week later. Takeaways are written as
   imperative or declarative statements, not as open questions.

The five parts must appear in this order and must be individually labeled.
A topic document that merges them, drops one, or reorders them is not
considered to satisfy the format, because the value of the structure is in
its predictability across topics.

## Promotion rules for curated topic material

A topic document is built up by repeated promotions out of in-session
drafts, not by writing the whole document up front. Promotion is the act
that happens in the close-out path of [LEARNING_FLOW.md](LEARNING_FLOW.md),
specifically the "promote durable topic material" step.

Content is promoted into the durable topic document only when all of the
following hold:

- **Stability.** The content survived the learner's questions and
  challenges within the session without being rewritten more than once.
  Text that is still being argued with at the end of a session is left as
  draft for the next session.
- **Reusability.** The content will plausibly be useful to a future session
  on the same topic - on a review pass, when starting a re-implementation
  in another language, or when answering an interview question. One-off
  rephrasings of an idea that the learner already understands are not
  promoted.
- **Correction of a real misconception.** Content that corrected a wrong
  mental model held earlier in the session is preferred for promotion over
  content that merely restated something the learner already knew.
- **Fit with the required teaching structure.** Promoted content goes into
  one of the five labeled parts (core claim, rationale, real example, easy
  example, takeaways) or into a structural slot defined by the contract
  (language coverage, linked artifacts, practice and interview notes). It
  does not create new top-level sections.
- **Source identifiable.** The session summary in `docs/sessions/` for the
  session doing the promotion is updated to record what was promoted, so
  the topic document's last-promoted marker can point to a real entry.

Content that does not meet these criteria stays in the session draft and
either ages out or is reconsidered in a future session. Raw AI transcript
is never promoted; only learner-validated, structure-fitting material is.

Demotion is allowed and is the inverse rule: a future session that
discovers a promoted line is wrong, misleading, or no longer concise enough
removes or rewrites it during a close-out and notes the change in that
session's summary.

## Practice and interview notes: split rule

The practice and interview notes section starts as a single section inside
the topic document. It is split into its own file only when it has grown
enough that keeping it inline would dilute the teaching structure.

The split rule is intentionally conservative so the learner does not face
extra navigation early on:

1. **Default - inline.** While the section is small (roughly fewer than
   ten notes, or anything that still reads in a single quick scroll
   alongside the teaching structure), it stays inside
   `docs/topics/<topic-slug>/README.md`. The teaching structure remains the
   primary reading surface.
2. **Trigger to split.** Split only when at least one of the following is
   true:
   - The notes section has crossed roughly ten distinct entries (interview
     answers plus problem-solving insights combined) and has started
     visually competing with the teaching structure on a quick read.
   - The notes have begun to subdivide naturally into clusters - for
     example, "interview answers", "common pitfalls", and "problem-solving
     patterns" - that each have multiple entries.
   - A future session needs to link directly into the notes from another
     topic, and the inline section has no stable anchor that holds across
     promotions.
3. **How to split.** When the split is triggered, move the section into
   `docs/topics/<topic-slug>/PRACTICE.md`. Keep a short stub in the topic
   `README.md` that summarizes the high-value notes and links to
   `PRACTICE.md` for the full set. The teaching structure (core claim,
   rationale, real example, easy example, takeaways) stays in the
   `README.md` and is never moved out.
4. **No pre-emptive split.** A topic does not start with a `PRACTICE.md`.
   Creating one before the trigger fires is treated the same as
   pre-generating topic material in `LEARNING_FLOW.md`: it produces a
   reference manual the learner does not read.

The split rule applies only to the practice and interview notes section.
Implementation code and problem-set solutions live in their canonical
folders (`implementations/<language>/<topic-slug>/` and
`solutions/<topic-slug>/`) from day one and are not subject to this rule -
they are linked from the topic document rather than embedded in it.

## How this document is used

- [LEARNING_FLOW.md](LEARNING_FLOW.md) references this format in Phase 2
  (scaffold creation) and Phase 3 (promotion). A close-out that promotes
  material into a topic document must check it against the contract and
  the teaching structure described here.
- [CURRICULUM.md](CURRICULUM.md) references this format as the expected
  shape of each topic's notes. The per-topic definition of done in the
  curriculum is satisfied by, among other things, having a topic document
  that conforms to this format.
- This format is intentionally stable. Changes to the contract or the
  teaching structure are made deliberately and are reflected across all
  existing topic documents in a dedicated session, not silently during a
  normal topic close-out.
