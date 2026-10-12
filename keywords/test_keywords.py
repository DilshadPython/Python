"""
Unit Test Suite for `keywords` Modules across Developer Tiers (Beginner, Intermediate, Senior).

This test suite verifies:
1. Hard and soft keyword inspection utilities (`python_keywords.py`).
2. Beginner level keyword functions (`beginner_keywords.py`).
3. Intermediate level keyword functions (`intermediate_keywords.py`).
4. Senior level keyword functions (`senior_keywords.py`).
"""

import asyncio
from pathlib import Path
import tempfile
import unittest

# Support both package and local directory import paths
try:
    from keywords.python_keywords import (
        get_all_python_keywords,
        get_soft_keywords,
        is_reserved_keyword,
        is_soft_keyword,
        get_keyword_summary,
    )
    from keywords.beginner_keywords import (
        demonstrate_control_flow,
        demonstrate_loops,
        demonstrate_boolean_logic,
        demonstrate_error_handling,
    )
    from keywords.intermediate_keywords import (
        demonstrate_generators,
        demonstrate_scope_keywords,
        demonstrate_lambdas_and_assertions,
        demonstrate_context_manager_and_finally,
    )
    from keywords.senior_keywords import (
        demonstrate_async_concurrency,
        demonstrate_pattern_matching,
        extract_keywords_from_ast,
        demonstrate_type_statement_analysis,
    )
except ImportError:
    from python_keywords import (
        get_all_python_keywords,
        get_soft_keywords,
        is_reserved_keyword,
        is_soft_keyword,
        get_keyword_summary,
    )
    from beginner_keywords import (
        demonstrate_control_flow,
        demonstrate_loops,
        demonstrate_boolean_logic,
        demonstrate_error_handling,
    )
    from intermediate_keywords import (
        demonstrate_generators,
        demonstrate_scope_keywords,
        demonstrate_lambdas_and_assertions,
        demonstrate_context_manager_and_finally,
    )
    from senior_keywords import (
        demonstrate_async_concurrency,
        demonstrate_pattern_matching,
        extract_keywords_from_ast,
        demonstrate_type_statement_analysis,
    )


class TestPythonKeywordsCore(unittest.TestCase):
    """Test suite for core keyword lookup functions."""

    def test_get_all_python_keywords(self) -> None:
        """Verify hard reserved keywords list."""
        keywords = get_all_python_keywords()
        self.assertIsInstance(keywords, list)
        self.assertGreater(len(keywords), 30)
        self.assertIn("def", keywords)
        self.assertIn("async", keywords)

    def test_is_reserved_keyword(self) -> None:
        """Verify keyword validator helper."""
        self.assertTrue(is_reserved_keyword("def"))
        self.assertFalse(is_reserved_keyword("my_var"))

    def test_get_keyword_summary(self) -> None:
        """Verify keyword summary dictionary structure."""
        summary = get_keyword_summary()
        self.assertIn("hard_keyword_count", summary)
        self.assertGreater(summary["hard_keyword_count"], 30)


class TestBeginnerKeywords(unittest.TestCase):
    """Test suite for beginner level keyword functions."""

    def test_demonstrate_control_flow(self) -> None:
        """Verify if/elif/else grade evaluation."""
        self.assertIn("Grade A", demonstrate_control_flow(95))
        self.assertIn("Grade B", demonstrate_control_flow(80))
        self.assertIn("Grade F", demonstrate_control_flow(40))

    def test_demonstrate_loops(self) -> None:
        """Verify for/while loop sequence generation."""
        squares = demonstrate_loops(4)
        self.assertEqual(squares, [0, 1, 4, 9])

    def test_demonstrate_boolean_logic(self) -> None:
        """Verify and/or/not/is boolean logic."""
        res = demonstrate_boolean_logic(True, False)
        self.assertFalse(res["can_login"])
        self.assertTrue(res["needs_attention"])

    def test_demonstrate_error_handling(self) -> None:
        """Verify try/except conversion handling."""
        self.assertEqual(demonstrate_error_handling("12.5"), 12.5)
        self.assertTrue(str(demonstrate_error_handling("abc")).startswith("Error:"))


class TestIntermediateKeywords(unittest.TestCase):
    """Test suite for intermediate level keyword functions."""

    def test_demonstrate_generators(self) -> None:
        """Verify yield and yield from generator output."""
        evens = list(demonstrate_generators(6))
        self.assertEqual(evens, [0, 2, 4])

    def test_demonstrate_scope_keywords(self) -> None:
        """Verify nonlocal and global scope modification."""
        res = demonstrate_scope_keywords()
        self.assertEqual(res["outer_count"], 20)
        self.assertGreaterEqual(res["global_counter"], 10)

    def test_demonstrate_lambdas_and_assertions(self) -> None:
        """Verify lambda, assert, and loop control keywords."""
        processed = demonstrate_lambdas_and_assertions([1, 2, 0, 3, -4, 999, 5])
        self.assertEqual(processed, [1, 4, 9])

    def test_demonstrate_context_manager(self) -> None:
        """Verify with/as context manager and finally cleanup."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "test_file.txt"
            content = "Intermediate Context Manager Test"
            read_content = demonstrate_context_manager_and_finally(temp_file, content)

            self.assertEqual(read_content, content)
            self.assertFalse(temp_file.exists())


class TestSeniorKeywords(unittest.TestCase):
    """Test suite for senior level keyword functions."""

    def test_demonstrate_async_concurrency(self) -> None:
        """Verify async/await concurrent task execution."""
        results = asyncio.run(demonstrate_async_concurrency([1, 2]))
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["resource_id"], 1)

    def test_demonstrate_pattern_matching(self) -> None:
        """Verify match/case structural pattern matching."""
        self.assertIn("Launching", demonstrate_pattern_matching("start service_a"))
        self.assertIn("Terminating", demonstrate_pattern_matching("stop service_b"))
        self.assertIn("Unrecognized", demonstrate_pattern_matching("invalid"))

    def test_extract_keywords_from_ast(self) -> None:
        """Verify CPython AST keyword node extraction."""
        code = "if True: pass\nfor i in range(1): yield i"
        nodes = extract_keywords_from_ast(code)
        self.assertIn("If", nodes)
        self.assertIn("For", nodes)

    def test_demonstrate_type_statement_analysis(self) -> None:
        """Verify soft keyword and identifier analysis."""
        analysis = demonstrate_type_statement_analysis("match")
        self.assertEqual(analysis["identifier"], "match")
        self.assertTrue(analysis["valid_variable_name"])


if __name__ == "__main__":
    unittest.main()
