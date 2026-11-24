# AI Semantic Search & Environment Guide

Welcome to the **AI & Semantic Search Tutorial Module**. This guide explains semantic vector search using Sentence Transformers, cosine similarity math, and provides a comprehensive guide on the **best modern ways to create and manage Python virtual environments (`venv`)**.

---

## 1. What is Semantic Search?

Traditional search looks for exact keyword matches (e.g. searching for *"nature"* will miss sentences containing *"mountains"* or *"waterfalls"* unless explicitly written).

**Semantic search** converts text into dense numerical vectors (**embeddings**) that capture the contextual meaning of words:
1. Sentences are mapped to a high-dimensional vector space (384 dimensions for `all-MiniLM-L6-v2`).
2. Sentences with similar meanings are placed close together in this vector space.
3. The search calculates **Cosine Similarity** between the query vector and document vectors to find the closest conceptual match.

$$\text{Cosine Similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$

---

## 2. Virtual Environment Guide: Which is the Best Way?

> **Question**: *Which is the best way to add a virtual environment: `python -m venv venv` or another way?*

### Summary Recommendation
* **The Modern Industry Best Practice (Recommended)**: **`uv` (`uv venv`)**
* **The Universal Built-In Standard**: **`python -m venv .venv`**

---

### Comparison: Virtual Environment Tools

| Feature | `uv venv` *(Recommended)* | `python -m venv` *(Built-in)* | `poetry` |
| :--- | :--- | :--- | :--- |
| **Creation Speed** | **Instant (~10ms)** | 1 – 3 seconds | Moderate |
| **Package Installation** | **10x – 100x faster** (Rust-based) | Slow (standard pip) | Slow |
| **External Dependency** | Requires `uv` (`pip install uv` or standalone binary) | **None** (Built into Python stdlib) | Requires `poetry` |
| **Lockfile Support** | Native `uv.lock` | None (manual `requirements.txt`) | Native `poetry.lock` |
| **No-Activation Execution**| Supported via `uv run` | Requires manual activation or explicit path | Supported via `poetry run` |
| **Cross-Platform** | Linux, macOS, Windows | Linux, macOS, Windows | Linux, macOS, Windows |

---

### Method A: The Modern Best Practice — `uv` (Fastest & Most Reliable)

Since your repository already includes `uv.lock` and `pyproject.toml`, **`uv` is the ideal choice**.

#### 1. Create the virtual environment:
```bash
# Inside the /ai folder (or project root):
uv venv
```
*(Creates `.venv/` in milliseconds).*

#### 2. Install / sync dependencies directly from the lockfile:
```bash
uv sync
```

#### 3. Run scripts without needing to manually activate:
```bash
uv run python models.py
```
*(Or activate manually if you prefer):*
```bash
source .venv/bin/activate
python models.py
```

---

### Method B: The Built-in Standard — `python -m venv` (Zero Installs)

If you are working on a machine where third-party CLIs like `uv` cannot be installed, use Python's built-in `venv` module.

> **Naming Tip**: Name your virtual environment folder **`.venv`** (with a leading dot) or **`venv`**. Naming it `.venv` keeps it hidden from directory listings and automatically matches standard `.gitignore` rules.

#### 1. Create the virtual environment:
```bash
python3 -m venv .venv
```

#### 2. Activate the virtual environment:
* **Linux / macOS**:
  ```bash
  source .venv/bin/activate
  ```
* **Windows (Command Prompt)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

#### 3. Upgrade pip and install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
# OR if using pyproject.toml:
pip install -e .
```

#### 4. Deactivate when finished:
```bash
deactivate
```

---

## 3. Module Overview

| File | Description | Core Concept |
| :--- | :--- | :--- |
| `models.py` | Semantic search engine & `SentenceTransformer` | Embeddings, cosine similarity, vector search |
| `test_models.py` | Automated unit test suite (`unittest`) | Mathematical verification of cosine metrics & mock search |
| `pyproject.toml`| Project metadata & dependency declarations | Modern PEP 621 Python packaging |
| `uv.lock` | Pinned exact dependency graph | Deterministic, reproducible builds |

---

## 4. Running the Semantic Search Example

From the `ai/` folder:

```bash
python3 models.py
```

Example output:
```text
--- Semantic Search Demonstration ---
Query: 'nice nature place'
Best Match:   'Waterfalls in Duhok'
Score:        0.6721
```

---

## 5. Running the Unit Tests

Execute the test suite from the repository root:

```bash
python3 -m unittest ai/test_models.py
```
Expected output:
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```
