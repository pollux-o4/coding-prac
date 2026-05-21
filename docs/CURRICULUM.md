# Curriculum

This is the stable study path for the one-month CS interview-prep learning
system. Future sessions follow the order, priorities, and weekly plan defined
here.

## Operating model at a glance

| Item | Value |
|------|-------|
| Goal | Build interview-ready CS fundamentals, weighted toward roles that focus on knowledge over live coding tests. |
| Duration | One month of focused study (about 5 days per week, 3-4 hours per day, totaling 60-80 hours). |
| Pace | Concept-first, fast reading with AI assistance; depth comes from implementation and problem solving. |
| Primary language | **Python** for learning, exploration, and first-pass implementations. |
| Secondary implementation languages | **Java**, **C**, and **TypeScript** for re-implementing studied topics to internalize trade-offs across paradigms. |
| Time allocation | Data structures + algorithms (~70%), operating systems (~15%), interview practice and review (~15%). |
| Theory vs. practice split | Roughly 50% concept study, 50% problem solving and mock interviews. |

## Study order and priorities

The curriculum follows a single ranked priority list. Every week stays inside
this ordering, even when individual topics shift.

1. **Data structures + algorithms (~70%)**
   - Core data structures (must-learn): Array, Linked List, Stack, Queue,
     Binary Tree.
   - Extended data structures (as time allows): Graph, Hash Table, Heap, Trie.
   - Algorithms are studied alongside the data structure that motivates them,
     not as a separate track.
2. **Operating systems (~15%)**
   - Pulled in opportunistically when a data structure or algorithm makes an
     OS concept concrete (e.g., stack overflow with recursion, cache locality
     with arrays).
   - Core surface area: processes, memory, threads, caching.
3. **Interview practice and review (~15%)**
   - Problem solving on LeetCode-style sets tied to the week's topic.
   - Mock interviews, with frequency increasing toward week 4.

## Language rotation per topic

Each topic is studied in the same fixed order so that the learner builds the
same mental model across paradigms:

1. **Concept** - read and explain the data structure or algorithm in plain
   language, with Big O and trade-offs.
2. **Python** (primary) - implement first in Python to get a working version
   quickly and to anchor the mental model.
3. **Java** - re-implement to practice static typing, classes, and the JVM
   memory model framing.
4. **C** - re-implement to confront manual memory management and pointer
   semantics.
5. **TypeScript** - re-implement to practice structural typing and to cover
   the language used for web-facing interview questions.

Python is always the primary practice language. Java, C, and TypeScript are
implementation languages applied to topics already studied in Python. A topic
is not considered "done" until at least the Python implementation and one
secondary-language re-implementation exist.

## One-month path

The four weeks are sequenced so that each week's data structures feed the
next week's algorithms. Hours are guidance, not a contract.

### Week 1 - Foundations and linear structures

- Day 1-2: Big O notation and the memory model (about 6 hours of prep work
  before any structure-specific study).
- Day 3-5: Array and core array problems (about 12 hours).
- Day 6-7: Linked List and related problems (about 12 hours).
- Day 8-10: Stack and Queue (about 12 hours).
- Algorithms in parallel: linear search, binary search.
- Checkpoint: Array, Linked List, and Stack implemented in Python plus at
  least one of Java / C / TypeScript.

### Week 2 - Trees and traversal

- Day 1-5: Binary Tree and recursion (about 15 hours).
- Day 6-7: DFS and BFS foundations and implementation (about 12 hours).
- Algorithms in parallel: DFS, BFS.
- Linked OS concepts: stack overflow, the recursion call stack.
- Checkpoint: at least five tree traversal problems solved; at least one
  mock interview.

### Week 3 - Graphs, advanced search, hashing

- Day 1-4: Graph theory and implementation (about 12 hours).
- Day 5-7: DFS and BFS on graphs and related problems (about 12 hours).
- Day 8-10: Hash Table (about 12 hours).
- Algorithms in parallel: topological sort, introductory shortest path
  (Dijkstra).
- Checkpoint: at least five graph problems solved; Sliding Window and Two
  Pointers patterns understood.

### Week 4 - Sorting, DP / Greedy, and consolidation

- Day 1-3: Sorting algorithms - Bubble, Selection, Insertion, Merge, Quick
  (about 9 hours).
- Day 4-5: Dynamic Programming and Greedy fundamentals (about 9 hours).
- Day 6-7: Heap and Trie as optional depth topics (about 6 hours).
- Day 8-10: Mock interviews and full-curriculum review (about 12 hours).
- Algorithms in parallel: Sliding Window, Two Pointers.
- Checkpoint: five sorting algorithms implemented with time-complexity
  comparison; at least three mock interviews completed.

## Definition of done per topic

A topic is durably learned when all of the following hold:

- Concept can be explained from memory, including Big O for the common
  operations and at least one real-world use case.
- A working Python implementation exists.
- At least one re-implementation exists in Java, C, or TypeScript (with a
  goal of covering all three across the month).
- At least three interview-style questions have been answered for the topic.
- At least two related problems have been solved end-to-end.

## How this document is used

- Future sessions treat this document as the source of truth for what to
  study next. When the current week or topic is unclear, the session
  consults this curriculum first.
- Progress against the weekly checkpoints is tracked in
  [PROGRESS.md](PROGRESS.md).
- The per-topic learning workflow (concept -> Python -> secondary language
  -> questions -> problems) is described in more detail in
  [LEARNING_FLOW.md](LEARNING_FLOW.md), and the expected shape of each
  topic's notes lives in [TOPIC_FORMAT.md](TOPIC_FORMAT.md).
