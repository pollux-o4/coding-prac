#!/usr/bin/env python3
"""Tests for `scripts/scaffold_topic.py`.

These tests use only the standard library (`unittest`, `tempfile`, `pathlib`)
so they can be run directly with:

    python scripts/test_scaffold_topic.py

The tests run inside a temporary working tree, so they never touch the real
repository. They cover the two verification properties demanded by issue #10
acceptance criterion 3:

1. **Placeholder generation only.** Running the scaffold creates the expected
   files at the canonical artifact locations, every file contains explicit
   TODO placeholder markers, and no file contains finished teaching content.
2. **Rerun safety.** Running the scaffold a second time with previously
   filled content in place leaves that filled content byte-for-byte
   unchanged.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Ensure the script under test is importable regardless of how the test
# runner is invoked.
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import scaffold_topic  # noqa: E402  (import after sys.path manipulation)


class ScaffoldTopicTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    # ---- AC 1 / AC 2: placeholder slots exist at canonical locations ------

    def test_creates_topic_implementation_and_solution_slots(self) -> None:
        slug = "linked-list"
        languages = ("python", "java", "c", "typescript")

        created, skipped = scaffold_topic.scaffold(slug, languages, self.root)

        topic_doc = self.root / "docs" / "topics" / slug / "README.md"
        solution_doc = self.root / "solutions" / slug / "README.md"

        self.assertTrue(topic_doc.exists(), "topic document placeholder missing")
        self.assertTrue(solution_doc.exists(), "solution slot README missing")
        for lang in languages:
            impl_doc = self.root / "implementations" / lang / slug / "README.md"
            self.assertTrue(
                impl_doc.exists(),
                f"implementation slot README for {lang} missing",
            )

        expected_count = 1 + len(languages) + 1  # topic + per-lang impl + solution
        self.assertEqual(len(created), expected_count)
        self.assertEqual(skipped, [])

    # ---- AC 1: topic document carries the seven TOPIC_FORMAT slots --------

    def test_topic_document_contains_all_seven_format_slots(self) -> None:
        slug = "array"
        scaffold_topic.scaffold(slug, scaffold_topic.DEFAULT_LANGUAGES, self.root)

        body = (self.root / "docs" / "topics" / slug / "README.md").read_text(
            encoding="utf-8"
        )

        # Item 1: title + one-line scope placeholder.
        self.assertIn("one-line scope", body)
        # Item 2: curriculum anchor.
        self.assertIn("Curriculum anchor", body)
        # Item 3: five-part teaching structure, each part labeled.
        for part in (
            "Core claim or concept",
            "Rationale",
            "Real example",
            "Easy example",
            "Emphasized takeaways",
        ):
            self.assertIn(part, body, f"teaching structure section missing: {part}")
        # Item 4: language coverage table header.
        self.assertIn("Language coverage", body)
        self.assertIn("| Language | Status | Implementation |", body)
        # Item 5: linked artifacts.
        self.assertIn("Linked artifacts", body)
        # Item 6: practice and interview notes.
        self.assertIn("Practice and interview notes", body)
        # Item 7: last-promoted marker.
        self.assertIn("Last promoted", body)

    # ---- AC 3: placeholders only, no finished teaching content -----------

    def test_topic_document_is_placeholder_only(self) -> None:
        slug = "stack"
        scaffold_topic.scaffold(slug, ("python",), self.root)
        body = (self.root / "docs" / "topics" / slug / "README.md").read_text(
            encoding="utf-8"
        )

        # Every required slot is explicitly marked TODO.
        self.assertGreaterEqual(
            body.count("<!-- TODO:"),
            9,
            "expected at least nine TODO placeholders in topic document",
        )
        # The language coverage table has no filled status rows.
        self.assertNotIn("| done |", body)
        self.assertNotIn("| draft |", body)
        # The linked-artifacts list is empty (only the TODO marker, no
        # markdown list rows).
        artifacts_block = body.split("## Linked artifacts", 1)[1].split("##", 1)[0]
        self.assertIn("TODO", artifacts_block)
        list_rows = [
            line
            for line in artifacts_block.splitlines()
            if line.lstrip().startswith(("- ", "* ", "1."))
        ]
        self.assertEqual(list_rows, [], "linked-artifacts list must start empty")

    def test_implementation_and_solution_slots_state_contract(self) -> None:
        slug = "queue"
        scaffold_topic.scaffold(slug, ("python",), self.root)

        impl = (
            self.root / "implementations" / "python" / slug / "README.md"
        ).read_text(encoding="utf-8")
        solution = (self.root / "solutions" / slug / "README.md").read_text(
            encoding="utf-8"
        )

        # Both slot READMEs cite the artifact policy so a future session does
        # not treat the folder as a dumping ground.
        self.assertIn("ARTIFACT_POLICY.md", impl)
        self.assertIn("ARTIFACT_POLICY.md", solution)
        # The implementation slot mentions the learner-authored contract.
        self.assertIn("learner-authored", impl)
        # Neither slot ships runnable code (no fenced code blocks).
        self.assertNotIn("```", impl)
        self.assertNotIn("```", solution)

    # ---- AC 3: rerun safety ----------------------------------------------

    def test_rerun_does_not_overwrite_filled_content(self) -> None:
        slug = "binary-tree"
        scaffold_topic.scaffold(slug, ("python",), self.root)

        topic_doc = self.root / "docs" / "topics" / slug / "README.md"
        impl_doc = self.root / "implementations" / "python" / slug / "README.md"
        solution_doc = self.root / "solutions" / slug / "README.md"

        # Simulate a study session filling these placeholders with real
        # content.
        filled_topic = "# Binary Tree\n\nA tree with at most two children per node.\n"
        filled_impl = "# python implementation\n\nclass Node: pass\n"
        filled_solution = "# solutions\n\n## Problem 1: invert tree\nSolved.\n"
        topic_doc.write_text(filled_topic, encoding="utf-8")
        impl_doc.write_text(filled_impl, encoding="utf-8")
        solution_doc.write_text(filled_solution, encoding="utf-8")

        created, skipped = scaffold_topic.scaffold(slug, ("python",), self.root)

        self.assertEqual(
            created,
            [],
            "rerun must not create any file when slots already exist",
        )
        self.assertEqual(len(skipped), 3, "rerun must skip every existing slot")
        # Filled content is preserved byte-for-byte.
        self.assertEqual(topic_doc.read_text(encoding="utf-8"), filled_topic)
        self.assertEqual(impl_doc.read_text(encoding="utf-8"), filled_impl)
        self.assertEqual(solution_doc.read_text(encoding="utf-8"), filled_solution)

    def test_rerun_fills_only_missing_slots(self) -> None:
        slug = "graph"
        scaffold_topic.scaffold(slug, ("python", "java"), self.root)

        # Remove one slot to simulate it never having been scaffolded.
        java_slot = self.root / "implementations" / "java" / slug / "README.md"
        java_slot.unlink()

        created, skipped = scaffold_topic.scaffold(
            slug, ("python", "java"), self.root
        )

        self.assertEqual(
            [p.name for p in created],
            ["README.md"],
            "rerun should recreate exactly the missing slot",
        )
        self.assertEqual(created[0], java_slot)
        # Every other slot is reported as skipped.
        self.assertEqual(len(skipped), 3)


if __name__ == "__main__":
    unittest.main()
