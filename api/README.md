# 🌐 REST API Request & Client Integration (`api`) Pedagogical Module

Welcome to the **`api` REST API Integration Module**. This module provides a clean 3-tier pedagogical architecture for mastering HTTP REST API interaction, JSON data extraction, object-oriented API client design, range-driven pagination, $O(1)$ memory benchmarking, `dir(range)` runtime introspection, and historical version evolution notes from Python 2.7 to 3.13.

---

## 📂 Module Architecture

```
api/
├── 01_fundamentals/
│   ├── basic_api_requests.py        # HTTP GET requests via urllib, status code checking, JSON formatting
│   └── test_fundamentals.py         # Unittest suite mocking urllib HTTP requests
├── 02_advanced_rest_and_endpoints/
│   ├── advanced_api_client.py       # Object-oriented PokeApiClient class, endpoint routing, custom exceptions
│   └── test_advanced.py             # Unittest suite mocking multi-endpoint requests & error handling
├── 03_range_evolution_and_performance/
│   ├── range_api_pagination.py      # Range sequence pagination, O(1) memory benchmarking, dir(range) matrix
│   └── test_range_evolution.py      # Unittest suite for range offset generator & reflection
├── test_api_master.py              # Master unittest runner executing all 3 sub-tier test suites
└── README.md                        # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. Basic REST API Requests (`01_fundamentals`)

Execute basic iTunes API search:

```bash
python3 api/01_fundamentals/basic_api_requests.py
```

### 2. Advanced REST Client (`02_advanced_rest_and_endpoints`)

Execute object-oriented PokéAPI client:

```bash
python3 api/02_advanced_rest_and_endpoints/advanced_api_client.py
```

### 3. Range Pagination & Evolution (`03_range_evolution_and_performance`)

Simulate range offset API pagination and memory benchmarks:

```bash
python3 api/03_range_evolution_and_performance/range_api_pagination.py
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 api/test_api_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s api/01_fundamentals -p "test_*.py"
python3 -m unittest discover -s api/02_advanced_rest_and_endpoints -p "test_*.py"
python3 -m unittest discover -s api/03_range_evolution_and_performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01_fundamentals** | HTTP GET, `urllib.request`, JSON decoding, query parameter encoding, error handling | [`basic_api_requests.py`](01_fundamentals/basic_api_requests.py) | [`test_fundamentals.py`](01_fundamentals/test_fundamentals.py) |
| **02_advanced_rest_and_endpoints** | OOP client (`PokeApiClient`), multi-endpoint routing (`/pokemon`, `/ability`), `PokeApiError` | [`advanced_api_client.py`](02_advanced_rest_and_endpoints/advanced_api_client.py) | [`test_advanced.py`](02_advanced_rest_and_endpoints/test_advanced.py) |
| **03_range_evolution_and_performance** | Range offset pagination, $O(1)$ memory footprint, `dir(range)` matrix, Py 2.7 to 3.13 history | [`range_api_pagination.py`](03_range_evolution_and_performance/range_api_pagination.py) | [`test_range_evolution.py`](03_range_evolution_and_performance/test_range_evolution.py) |
