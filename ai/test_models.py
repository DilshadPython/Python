"""Unit tests for the AI semantic search module.

Tests cosine similarity math, vector ranking, search engine mechanics, and edge cases.
"""

import unittest
from unittest.mock import MagicMock

from ai.models import (
    calculate_cosine_similarity,
    SemanticSearchEngine,
    authenticate_huggingface,
    DEFAULT_PLACES
)


class TestSemanticSearch(unittest.TestCase):
    """Test suite for semantic search mathematics and search engine."""

    def test_cosine_similarity_identical_vectors(self):
        """Identical vectors should yield a cosine similarity of 1.0."""
        v1 = [1.0, 2.0, 3.0]
        doc_matrix = [[1.0, 2.0, 3.0]]
        scores = calculate_cosine_similarity(v1, doc_matrix)
        self.assertAlmostEqual(scores[0], 1.0, places=5)

    def test_cosine_similarity_orthogonal_vectors(self):
        """Orthogonal (perpendicular) vectors should yield a cosine similarity of 0.0."""
        v1 = [1.0, 0.0, 0.0]
        doc_matrix = [[0.0, 1.0, 0.0]]
        scores = calculate_cosine_similarity(v1, doc_matrix)
        self.assertAlmostEqual(scores[0], 0.0, places=5)

    def test_cosine_similarity_opposite_vectors(self):
        """Opposite vectors should yield a cosine similarity of -1.0."""
        v1 = [1.0, 0.0]
        doc_matrix = [[-1.0, 0.0]]
        scores = calculate_cosine_similarity(v1, doc_matrix)
        self.assertAlmostEqual(scores[0], -1.0, places=5)

    def test_cosine_similarity_ranking_order(self):
        """Verify that ranking correctly sorts highest similarity first."""
        query = [1.0, 1.0, 0.0]
        docs = [
            [1.0, 1.0, 0.0],  # Exactly identical -> 1.0
            [1.0, 0.0, 0.0],  # Partial match -> ~0.707
            [0.0, 0.0, 1.0],  # Completely orthogonal -> 0.0
        ]
        scores = calculate_cosine_similarity(query, docs)
        self.assertGreater(scores[0], scores[1])
        self.assertGreater(scores[1], scores[2])

    def test_search_engine_with_mocked_model(self):
        """Verify SemanticSearchEngine logic with mock embeddings (no network needed)."""
        engine = SemanticSearchEngine(corpus=["Apple", "Banana", "Vehicle"])

        # Mock sentence transformer model output
        mock_model = MagicMock()
        mock_model.encode.side_effect = lambda texts, normalize_embeddings=True: (
            [[0.9, 0.1], [0.8, 0.2], [0.0, 1.0]] if isinstance(texts, list)
            else [0.95, 0.05]
        )
        engine._model = mock_model

        engine.index_documents(engine.corpus)
        results = engine.search("Fruit", top_k=2)

        self.assertEqual(len(results), 2)
        # First match should be 'Apple' due to highest mock vector alignment
        self.assertEqual(results[0][1], "Apple")
        self.assertGreater(results[0][0], results[1][0])

    def test_search_engine_empty_corpus_raises_error(self):
        """Attempting to search an empty corpus should raise a ValueError."""
        engine = SemanticSearchEngine()
        with self.assertRaises(ValueError):
            engine.search("test query")

    def test_authenticate_huggingface_without_token(self):
        """authenticate_huggingface should return False gracefully when no token is present."""
        self.assertFalse(authenticate_huggingface(token=None))


if __name__ == "__main__":
    unittest.main()
