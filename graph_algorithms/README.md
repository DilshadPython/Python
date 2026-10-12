# Graph Algorithms & Data Visualization Master Guide (`matplotlib`)

Welcome to the **Graph Algorithms & Data Visualization Master Guide**, a production-grade educational reference detailing bar chart visualizations (`matplotlib.pyplot`), graph theory data structures (Adjacency List, Breadth-First Search BFS, Depth-First Search DFS), unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Architectural Architecture](#-overview--architectural-architecture)
2. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
3. [Directory Structure & Module Overview](#-directory-structure--module-overview)
4. [Installation & Requirements](#-installation--requirements)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 🎁 Overview & Architectural Architecture

Data visualization and graph theory represent two core pillars of Python software engineering:
- **Matplotlib Visualizations**: Transforming numerical and categorical datasets into vertical (`bar`) and horizontal (`barh`) charts.
- **Graph Algorithms**: Representing relationships between nodes using Adjacency Lists and traversing graph trees using BFS and DFS queue algorithms.

```text
[ Graph Data Structure ] ---> [ BFS / DFS Traversal ] ---> [ Matplotlib Subplot Render ]
```

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_graph.py`](file:///home/monika/PycharmProjects/Devel/Python/graph_algorithms/beginner_graph.py))
Focuses on basic vertical bar chart generation using `matplotlib.pyplot`:
- **Bar Plot Creation**: `plt.bar(categories, values, color='green')`.
- **Chart Titles & Labels**: `plt.title()`, `plt.xlabel()`, `plt.ylabel()`.
- **Figure Export**: `plt.savefig("chart.png")`.

```python
# Beginner Example: Simple bar chart plot
plt.bar(books, read_counts, color="green")
plt.title("Book Library")
plt.xlabel("Books")
plt.ylabel("Status")
plt.savefig("beginner_chart.png")
```

---

### 🚀 Intermediate Level ([`intermediate_graph.py`](file:///home/monika/PycharmProjects/Devel/Python/graph_algorithms/intermediate_graph.py))
Focuses on horizontal bar charts (`barh`), data value annotations (`bar_label`), and custom grid styling:
- **Horizontal Bar Charts**: `ax.barh(categories, values)`.
- **Data Value Annotations**: `ax.bar_label(bars, fmt='%d')`.
- **Grid Customization**: `ax.grid(axis='x', linestyle='--')`.

```python
# Intermediate Example: Styled horizontal bar chart with data labels
bars = ax.barh(technologies, readership, color="#2b5c8f")
ax.bar_label(bars, fmt="%d", padding=5)
ax.grid(axis="x", linestyle="--", alpha=0.6)
```

---

### 🔥 Senior Level ([`senior_graph.py`](file:///home/monika/PycharmProjects/Devel/Python/graph_algorithms/senior_graph.py))
Focuses on Adjacency List graph representations, BFS/DFS traversal implementations, and multi-panel Matplotlib subplots:
- **Graph Class**: `class Graph:` with `adj_list: Dict[str, List[str]]`.
- **Breadth-First Search**: Queue-based BFS (`collections.deque`).
- **Depth-First Search**: Recursive stack DFS.
- **Multi-Panel Subplots**: `fig, (ax1, ax2) = plt.subplots(1, 2)`.

```python
# Senior Example: Graph BFS traversal
def breadth_first_search(self, start_node: str) -> List[str]:
    visited = {start_node}
    queue = deque([start_node])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

---

## 📁 Directory Structure & Module Overview

```text
graph_algorithms/
├── README.md                     # Master documentation and multi-tier guide
├── requirements.txt              # Dependency specification file
├── test_graph_algorithms.py      # Multi-tier unit test suite
├── bar_chart_generator.py        # Modular bar chart generator with headless fallback
├── beginner_graph.py             # Beginner tier (plt.bar, title, labels, savefig)
├── intermediate_graph.py         # Intermediate tier (barh, bar_label, gridlines)
├── senior_graph.py               # Senior tier (Graph class, BFS, DFS, subplots)
├── bar_graph.py                  # Legacy wrapper script
└── bar_graph_update.py           # Legacy wrapper script
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_graph.py` | 🌱 Beginner | `plt.bar()`, `plt.title()`, `plt.xlabel()`, `plt.savefig()` |
| `intermediate_graph.py` | 🚀 Intermediate | `ax.barh()`, `ax.bar_label()`, custom gridlines |
| `senior_graph.py` | 🔥 Senior | `Graph` class, BFS, DFS, `plt.subplots(1, 2)` |
| `bar_chart_generator.py` | All Tiers | `render_bar_chart()`, headless `matplotlib.use('Agg')` |
| `test_graph_algorithms.py` | All Tiers | `unittest` suite verifying plotting and graph algorithms |

---

## 📦 Installation & Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r graph_algorithms/requirements.txt
```

---

## 🚀 How to Run the Code

```bash
# Run modular bar chart generator
python3 graph_algorithms/bar_chart_generator.py

# Run beginner tier examples
python3 graph_algorithms/beginner_graph.py

# Run intermediate tier examples
python3 graph_algorithms/intermediate_graph.py

# Run senior tier examples
python3 graph_algorithms/senior_graph.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest` (runs headless without opening popups):

```bash
# Run unittest suite directly
python3 -m unittest test_graph_algorithms.py

# Run with pytest from repository root
pytest graph_algorithms/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Visualization & Graph Evolution | Syntax & System Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Matplotlib 1.x series | Required explicit `plt.show()` event loops; eager `range()` list allocation. | Required `xrange()` for large graph node iterations. |
| **Python 3.4** | `pathlib.Path` integration | Save paths accept `Path` instances natively in Matplotlib 2.x+. | String path conversions required in Python 2.7. |
| **Python 3.8** | Matplotlib 3.4 `bar_label` API | Added `ax.bar_label()` direct bar annotation support. | Manual text calculation loop `ax.text(x, y, str)` in 2.7-3.7. |
| **Python 3.10**| Pattern matching in graph nodes | `match node:` structural inspection of graph edge types. | If-elif-else type checks in Python 2.7. |
| **Python 3.12**| Optimized deque & collection types | C-accelerated `collections.deque` for high-speed BFS traversals. | Higher overhead in legacy Python 2.7 deque objects. |
| **Python 3.13**| Free-threaded GIL-free rendering | Parallel non-blocking plot rendering across multiple CPU cores. | Thread locks prevented parallel Matplotlib backend calls. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Iterating graph nodes or plotting categorical axes frequently uses `range()` sequence objects:

```python
# Iterating plot bar positions using range()
categories = ["A", "B", "C", "D"]
for i in range(len(categories)):
    print(f"Bar Index {i}: Category={categories[i]}")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating sequence containment `500 in range(0, 1000, 5)` computes in constant-time arithmetic evaluation without allocating memory arrays.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

```python
r = range(0, 10, 2)
print(r.start)  # Output: 0
print(r.stop)   # Output: 10
print(r.step)   # Output: 2

print(r.index(6))  # Output: 3
print(r.count(4))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.