# 🤖 Artificial Intelligence & Neural Networks (`ai_python`) Pedagogical Module

Welcome to the **`ai_python` Artificial Intelligence & Deep Learning Module**. This module provides a complete 3-tier pedagogical architecture for mastering neural network data preprocessing (MNIST digit vector flattening & pixel normalization), object-oriented model building (`DenseLayer`, `SequentialModel`), mathematical activation functions (`ReLU`, `Softmax`), range-driven training epoch iteration, $O(1)$ memory benchmarking, `dir(range)` runtime introspection, and historical version evolution notes from Python 2.7 to 3.13.

---

## 📂 Module Architecture

```
ai_python/
├── 01_fundamentals/
│   ├── mnist_classifier_basics.py       # Pixel normalization [0..255] -> [0..1], 2D grid flattening, metrics
│   └── test_fundamentals.py            # Unittest suite for normalization, flattening, and metrics
├── 02_advanced_model_architecture/
│   ├── advanced_neural_network.py      # DenseLayer, SequentialModel, ReLU, Softmax, forward propagation
│   └── test_advanced.py                # Unittest suite for neural layers, Softmax probability sum, predictions
├── 03_range_evolution_and_performance/
│   ├── range_epoch_performance.py      # Epoch/batch range iteration, O(1) memory benchmarking, dir(range) matrix
│   └── test_range_evolution.py        # Unittest suite for epoch range generator & reflection
├── test_ai_python_master.py             # Master unittest runner executing all 3 sub-tier test suites
└── README.md                            # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. MNIST Preprocessing Basics (`01_fundamentals`)

Run basic synthetic image preprocessing and metric calculation demo:

```bash
python3 ai_python/01_fundamentals/mnist_classifier_basics.py
```

### 2. Advanced Neural Network Model (`02_advanced_model_architecture`)

Execute multi-layer forward propagation pass (`784 -> 128 -> 10` nodes):

```bash
python3 ai_python/02_advanced_model_architecture/advanced_neural_network.py
```

### 3. Range Epoch Performance & Benchmarks (`03_range_evolution_and_performance`)

Simulate range epoch iteration loops and memory benchmarks:

```bash
python3 ai_python/03_range_evolution_and_performance/range_epoch_performance.py
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 ai_python/test_ai_python_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s ai_python/01_fundamentals -p "test_*.py"
python3 -m unittest discover -s ai_python/02_advanced_model_architecture -p "test_*.py"
python3 -m unittest discover -s ai_python/03_range_evolution_and_performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01_fundamentals** | Matrix flattening ($28\times 28 \rightarrow 784$), pixel normalization, synthetic dataset generation, accuracy scoring | [`mnist_classifier_basics.py`](01_fundamentals/mnist_classifier_basics.py) | [`test_fundamentals.py`](01_fundamentals/test_fundamentals.py) |
| **02_advanced** | Object-oriented `DenseLayer`, `SequentialModel`, `ReLU` math, `Softmax` probability distribution | [`advanced_neural_network.py`](02_advanced_model_architecture/advanced_neural_network.py) | [`test_advanced.py`](02_advanced_model_architecture/test_advanced.py) |
| **03_range & evolution** | Epoch training loop `range(1, epochs+1)`, mini-batch offsets, $O(1)$ memory footprint, `dir(range)` matrix | [`range_epoch_performance.py`](03_range_evolution_and_performance/range_epoch_performance.py) | [`test_range_evolution.py`](03_range_evolution_and_performance/test_range_evolution.py) |
