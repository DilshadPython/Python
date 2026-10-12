# 🧮 Mathematical & Financial Calculators (`calculate`) Pedagogical Module

Welcome to the **`calculate` Mathematical & Financial Calculators Module**. This module provides a complete 3-tier pedagogical architecture for mastering core geometry and hypotenuse math, credit card interest rate amortization schedules (`CreditCardRepaymentCalculator`), weight loss milestones (`WeightLossGoalTracker`), growth targets (`GoalGrowthTracker`), range-driven schedule iteration, $O(1)$ memory benchmarking, `dir(range)` runtime introspection, and historical version evolution notes from Python 2.7 to 3.13.

---

## 📂 Module Architecture

```
calculate/
├── 01_fundamentals/
│   ├── math_calculator_basics.py       # Pythagorean hypotenuse, difference of squares, 2D distance
│   └── test_fundamentals.py            # Unittest suite for fundamental mathematical formulas
├── 02_advanced_financial_and_goal_trackers/
│   ├── financial_and_goal_trackers.py  # CreditCardRepaymentCalculator, WeightLossGoalTracker, GoalGrowthTracker
│   └── test_advanced.py                # Unittest suite for credit repayment schedules, weight & growth targets
├── 03_range_evolution_and_performance/
│   ├── range_calculator_performance.py # Monthly schedule range iteration, O(1) memory benchmarking, dir(range)
│   └── test_range_evolution.py        # Unittest suite for schedule range generator & reflection
├── test_calculate_master.py            # Master unittest runner executing all 3 sub-tier test suites
└── README.md                           # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. Basic Mathematical Calculations (`01_fundamentals`)

Run basic Pythagorean hypotenuse and distance formula demonstrations:

```bash
python3 calculate/01_fundamentals/math_calculator_basics.py
```

### 2. Credit Card & Goal Calculators (`02_advanced_financial_and_goal_trackers`)

Execute credit card repayment schedule and target milestone trackers:

```bash
python3 calculate/02_advanced_financial_and_goal_trackers/financial_and_goal_trackers.py
```

### 3. Calculation Range Performance & Benchmarks (`03_range_evolution_and_performance`)

Simulate calculation schedule stepping sequences and memory benchmarks:

```bash
python3 calculate/03_range_evolution_and_performance/range_calculator_performance.py
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 calculate/test_calculate_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s calculate/01_fundamentals -p "test_*.py"
python3 -m unittest discover -s calculate/02_advanced_financial_and_goal_trackers -p "test_*.py"
python3 -m unittest discover -s calculate/03_range_evolution_and_performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01_fundamentals** | Pythagorean theorem $\sqrt{a^2+b^2}$, difference of squares $(a^2-b^2)$, 2D Euclidean distance | [`math_calculator_basics.py`](01_fundamentals/math_calculator_basics.py) | [`test_fundamentals.py`](01_fundamentals/test_fundamentals.py) |
| **02_advanced** | Object-oriented `CreditCardRepaymentCalculator`, `WeightLossGoalTracker`, `GoalGrowthTracker` | [`financial_and_goal_trackers.py`](02_advanced_financial_and_goal_trackers/financial_and_goal_trackers.py) | [`test_advanced.py`](02_advanced_financial_and_goal_trackers/test_advanced.py) |
| **03_range & evolution** | Schedule month range sequence `range(1, N+1)`, $O(1)$ memory footprint, `dir(range)` matrix, Py 2.7 to 3.13 history | [`range_calculator_performance.py`](03_range_evolution_and_performance/range_calculator_performance.py) | [`test_range_evolution.py`](03_range_evolution_and_performance/test_range_evolution.py) |
