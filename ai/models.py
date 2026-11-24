"""Semantic Search demonstration using Sentence-Transformers and Cosine Similarity.

This module maps sentences and paragraphs into a dense vector space (384 dimensions)
using the `all-MiniLM-L6-v2` model for semantic similarity search.

Key Concepts:
- Dense Vector Embeddings: Captures semantic meaning beyond raw keyword matching.
- Cosine Similarity: Measures the angular distance between vectors.
- Resilient Design: Uses high-performance NumPy when installed, with standard library
  math fallback to guarantee zero crash on clean environments.
- Non-blocking Authentication: Optional Hugging Face authentication via environment variables.
"""

import math
import os
from typing import Any, List, Optional, Sequence, Tuple, Union

# Attempt to load NumPy; if shadowed by a local directory or absent, fall back gracefully
try:
    import numpy as np  # type: ignore
    if not hasattr(np, "ndarray"):
        np = None
except (ImportError, AttributeError):
    np = None

Vector = Union[List[float], Any]


def authenticate_huggingface(token: Optional[str] = None) -> bool:
    """Safely authenticate with Hugging Face Hub if a token is available.

    Note: Public open-weights models such as 'all-MiniLM-L6-v2' do NOT require
    authentication. This helper is optional for private models or rate-limit boosts.

    Args:
        token (str, optional): Hugging Face access token. Defaults to $HF_TOKEN.

    Returns:
        bool: True if authenticated, False if running anonymously.
    """
    hf_token = token or os.getenv("HF_TOKEN")
    if hf_token:
        try:
            from huggingface_hub import login  # type: ignore
            login(token=hf_token)
            print("[INFO] Successfully authenticated with Hugging Face Hub.")
            return True
        except Exception as exc:
            print(f"[WARN] Hugging Face login failed ({exc}). Continuing anonymously.")
            return False
    # No token provided; proceed anonymously for public models
    return False


def calculate_cosine_similarity(query_vector: Vector, document_vectors: Sequence[Vector]) -> List[float]:
    """Calculate cosine similarity scores between a query vector and document vectors.

    Formula:
        cosine_similarity(u, v) = (u . v) / (||u|| * ||v||)

    Args:
        query_vector: 1D vector (List[float] or np.ndarray).
        document_vectors: Collection of 1D vectors (List of vectors or 2D np.ndarray).

    Returns:
        List[float]: Similarity score for each document, bounded between -1.0 and 1.0.
    """
    scores: List[float] = []

    # Fast path if real NumPy is available
    if np is not None and isinstance(query_vector, np.ndarray) and isinstance(document_vectors, np.ndarray):
        q_norm = float(np.linalg.norm(query_vector))
        d_norms = np.linalg.norm(document_vectors, axis=1)
        if q_norm == 0.0 or np.any(d_norms == 0.0):
            q_norm = max(q_norm, 1e-12)
            d_norms = np.where(d_norms == 0.0, 1e-12, d_norms)
        dot_products = np.dot(document_vectors, query_vector)
        return [float(score) for score in (dot_products / (d_norms * q_norm))]

    # Standard library fallback (zero dependencies, identical math precision)
    norm_q = math.sqrt(sum(float(x) ** 2 for x in query_vector))
    for doc in document_vectors:
        dot = sum(float(a) * float(b) for a, b in zip(query_vector, doc))
        norm_d = math.sqrt(sum(float(y) ** 2 for y in doc))
        if norm_q == 0.0 or norm_d == 0.0:
            scores.append(0.0)
        else:
            scores.append(float(dot / (norm_q * norm_d)))

    return scores


class SemanticSearchEngine:
    """Semantic search engine powered by SentenceTransformer embeddings."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", corpus: Optional[Sequence[str]] = None) -> None:
        """Initialize search engine with a transformer model and corpus.

        Args:
            model_name (str): Sentence transformer model identifier.
            corpus (Sequence[str], optional): Initial list of documents.
        """
        self.model_name = model_name
        self._model = None  # Lazy-loaded on first encode
        self.corpus: List[str] = list(corpus) if corpus else []
        self.corpus_vectors: Optional[Any] = None

    @property
    def model(self):
        """Lazy loader for SentenceTransformer to allow fast, clean module imports."""
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer  # type: ignore
                self._model = SentenceTransformer(self.model_name)
            except ImportError as err:
                raise ImportError(
                    "The 'sentence-transformers' package is required to encode embeddings.\n"
                    "Install it via: uv sync  (or pip install sentence-transformers)"
                ) from err
        return self._model

    def index_documents(self, documents: Sequence[str]) -> Any:
        """Encode and store document embeddings for future queries.

        Args:
            documents (Sequence[str]): List of sentences or paragraphs to index.

        Returns:
            Any: Matrix or list of document embeddings.
        """
        self.corpus = list(documents)
        self.corpus_vectors = self.model.encode(self.corpus, normalize_embeddings=True)
        return self.corpus_vectors

    def search(self, query: str, top_k: int = 1) -> List[Tuple[float, str]]:
        """Search the indexed corpus for documents most semantically similar to query.

        Args:
            query (str): Search query sentence.
            top_k (int): Number of top matches to return.

        Returns:
            List[Tuple[float, str]]: List of (similarity_score, document_text) tuples.
        """
        if self.corpus_vectors is None or len(self.corpus) == 0:
            raise ValueError("Corpus is empty. Call index_documents() before search().")

        query_vector = self.model.encode(query, normalize_embeddings=True)
        scores = calculate_cosine_similarity(query_vector, self.corpus_vectors)

        # Pair scores with document text and sort descending
        indexed_scores = sorted(enumerate(scores), key=lambda item: item[1], reverse=True)
        top_matches = indexed_scores[:top_k]

        return [(score, self.corpus[idx]) for idx, score in top_matches]


# Default corpus used in tutorial
DEFAULT_PLACES = [
    "Beautiful mountains in Kurdistan",
    "Historic citadel in Erbil",
    "Waterfalls in Duhok",
    "Kurdish traditional music"
]


def search(query: str, places: Optional[Sequence[str]] = None) -> Tuple[float, str]:
    """Legacy backward-compatible functional API for semantic search.

    Args:
        query (str): The search phrase.
        places (Sequence[str], optional): Optional custom list of places.

    Returns:
        Tuple[float, str]: The highest (similarity_score, matching_place_text).
    """
    corpus = places if places is not None else DEFAULT_PLACES
    engine = SemanticSearchEngine(corpus=corpus)
    engine.index_documents(corpus)
    matches = engine.search(query, top_k=1)
    return matches[0]


if __name__ == "__main__":
    authenticate_huggingface()

    print("--- Semantic Search Demonstration ---")
    query_text = "nice nature place"
    print(f"Query: '{query_text}'")

    try:
        score, best_match = search(query_text)
        print(f"Best Match:   '{best_match}'")
        print(f"Score:        {score:.4f}")
    except ImportError as exc:
        print(f"[NOTE] {exc}")
