# PostgreSQL Database Integration Master Guide

Welcome to the **PostgreSQL Integration Master Guide**, a production-grade educational reference detailing PostgreSQL administration, CPython database adapters (`psycopg2`), parameter query security (`%s`), context manager transactions, unit testing via `unittest.mock`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & PostgreSQL Architecture](#-overview--postgresql-architecture)
2. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
3. [PostgreSQL Installation & Administration Guide](#-postgresql-installation--administration-guide)
4. [Directory Structure & Module Overview](#-directory-structure--module-overview)
5. [Database Security & Parameterized Query Binding](#-database-security--parameterized-query-binding)
6. [How to Run the Code](#-how-to-run-the-code)
7. [Running Unit Tests](#-running-unit-tests)
8. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
9. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 🐘 Overview & PostgreSQL Architecture

PostgreSQL is an enterprise-grade Object-Relational Database Management System (ORDBMS). In CPython, database interaction follows **PEP 249 (Python Database API Specification v2.0)**.

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_postgres.py`](file:///home/monika/PycharmProjects/Devel/Python/postgresql/postgresql/beginner_postgres.py))
Focuses on basic database connections, cursor creation, simple `INSERT` / `SELECT` query execution, and explicit `connection.commit()`:
- **Connection**: `psycopg2.connect(user, password, host, port, database)`.
- **Query Execution**: `cursor.execute(sql, params)`.
- **Retrieval**: `cursor.fetchall()`.

```python
# Beginner Example: Step-by-step INSERT and SELECT
connection = psycopg2.connect(user="dilmac", database="university")
cursor = connection.cursor()

cursor.execute("INSERT INTO Students (Name) VALUES (%s)", ("Alice",))
connection.commit()

cursor.execute("SELECT * FROM Students;")
records = cursor.fetchall()
```

---

### 🚀 Intermediate Level ([`intermediate_postgres.py`](file:///home/monika/PycharmProjects/Devel/Python/postgresql/postgresql/intermediate_postgres.py))
Focuses on resource safety via context managers (`with connection:`), batch insertion using `executemany()`, and transactional error recovery with explicit `connection.rollback()`:
- **Batch Processing**: `cursor.executemany(sql, tuple_list)`.
- **Context Managers**: Automatic transaction management via `with connection:`.
- **Error Recovery**: Catching DB errors and invoking `connection.rollback()`.

```python
# Intermediate Example: Context managers and rollback
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.executemany("INSERT INTO mobile VALUES (%s, %s, %s)", batch_tuples)
except psycopg2.Error:
    connection.rollback()
```

---

### 🔥 Senior Level ([`senior_postgres.py`](file:///home/monika/PycharmProjects/Devel/Python/postgresql/postgresql/senior_postgres.py))
Focuses on enterprise architecture patterns including dataclass ORM object mapping, connection pooling, asynchronous coroutines (`asyncio`), and automated schema migration runners:
- **Dataclass ORM Mapping**: Strongly-typed `StudentModel` domain objects.
- **Asynchronous Queries**: `async` coroutine execution.
- **Database Migrations**: `SchemaMigrationRunner` executing DDL versioning scripts.

```python
# Senior Example: Dataclass ORM mapping and schema migrations
@dataclass
class StudentModel:
    id: Optional[int]
    name: str
    gender: str
    about: str

migrator = SchemaMigrationRunner(client)
migrator.apply_migrations()
```

---

## 📁 Directory Structure & Module Overview

```text
postgresql/
├── README.md                       # Master documentation and multi-tier guide
├── install_postgres.md             # Linux installation cheatsheet
├── test_postgresql.py              # Multi-tier unit test suite with unittest.mock
└── postgresql/
    ├── requirements.txt            # Dependency file (psycopg2-binary)
    ├── beginner_postgres.py        # Beginner tier (simple SELECT/INSERT)
    ├── intermediate_postgres.py    # Intermediate tier (executemany & rollback)
    ├── senior_postgres.py          # Senior tier (dataclass ORM & migrations)
    ├── postgres_client.py          # PostgreSQLClient adapter wrapper
    ├── create_db.py                # Database creation helper
    ├── create_table.py             # Table creation helper
    ├── insert_mobile_record.py     # Parameterized record insertion module
    └── connect_db.py               # Backward-compatible wrapper script
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_postgres.py` | 🌱 Beginner | Basic `connect()`, `execute()`, `fetchall()`, `commit()` |
| `intermediate_postgres.py` | 🚀 Intermediate | `executemany()`, `with connection:`, `rollback()` |
| `senior_postgres.py` | 🔥 Senior | `StudentModel` dataclass, `SchemaMigrationRunner`, `asyncio` |
| `postgres_client.py` | All Tiers | `PostgreSQLClient`, `execute_query()`, `fetch_all()` |
| `test_postgresql.py` | All Tiers | `unittest` suite covering all 3 developer tiers |

---

## 🛠️ PostgreSQL Installation & Administration Guide

### 1. Ubuntu / Debian / Linux Mint Installation
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib postgresql-client libpq-dev
sudo systemctl status postgresql
```

### 2. Service Management Commands
```bash
sudo systemctl start postgresql
sudo systemctl stop postgresql
sudo systemctl restart postgresql
```

### 3. Interactive `psql` Administration & User Configuration
```bash
sudo su - postgres
psql

-- In psql interactive shell:
ALTER USER postgres WITH PASSWORD 'secure_password';
CREATE ROLE dilmac WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'secret_pass';
ALTER USER dilmac WITH SUPERUSER;
CREATE DATABASE university;
\l
\du
\q
```

---

## 🔒 Database Security & Parameterized Query Binding

### 1. Protecting Against SQL Injection
Never concatenate raw user strings directly into SQL statements! Always use `%s` query parameter binding:

```python
# ❌ UNSAFE: Vulnerable to SQL Injection
user_input = "OnePlus'; DROP TABLE mobile; --"
cursor.execute(f"INSERT INTO mobile (MODEL) VALUES ('{user_input}')")

# ✅ SAFE: Parameterized Query Binding (%s)
user_input = "OnePlus 6"
cursor.execute("INSERT INTO mobile (MODEL, PRICE) VALUES (%s, %s)", (user_input, 950.00))
```

---

## 🚀 How to Run the Code

```bash
# Install dependencies
pip install -r postgresql/requirements.txt

# Run beginner tier examples
python3 postgresql/beginner_postgres.py

# Run intermediate tier examples
python3 postgresql/intermediate_postgres.py

# Run senior tier examples
python3 postgresql/senior_postgres.py
```

---

## 🧪 Running Unit Tests

Execute unit tests offline without requiring a running PostgreSQL server daemon:

```bash
# Run unittest suite directly
python3 -m unittest test_postgresql.py

# Run with pytest from repository root
pytest postgresql/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Database Adapter & Language Evolutions | Standard Library & Driver Improvements | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | PEP 249 DB-API 2.0 baseline | Byte strings vs Unicode in SQL query tuples | `str` bytes required explicit `.encode('utf-8')` before sending to PostgreSQL. |
| **Python 3.3** | `u'str'` unicode literal compatibility | Universal UTF-8 string encoding default | Native unicode text strings eliminated encoding mismatch errors in psycopg2. |
| **Python 3.4** | `enum.Enum`, `pathlib.Path` | Integrated `asyncio` for non-blocking I/O | Standard DB-API 2.0 synchronous connection pools. |
| **Python 3.5** | Type Hints (`typing`), `async`/`await` | `asyncpg` non-blocking PostgreSQL driver | Explicit type signatures for DB client methods (`Optional[Tuple]`). |
| **Python 3.6** | F-strings `f"{var}"`, `secrets` module | F-strings for dynamic DDL table identifiers | Safer dynamic SQL generation for table name definitions. |
| **Python 3.7** | `@dataclass`, `contextlib.asynccontextmanager` | `@dataclass` mapped database models | Clean object modeling replacing tuple unpacking from `fetchall()`. |
| **Python 3.8** | Walrus operator `:=`, Positional-only `/` | `TypedDict` database row representations | `while (row := cursor.fetchone()):` concise row fetching loops. |
| **Python 3.9** | Dict Union `|`, Built-in generics `list[tuple]` | Generic `list[tuple]` type hints for query results | Clean database record type annotations without `typing.List`. |
| **Python 3.10**| Pattern Matching `match/case` (PEP 634) | Structural pattern matching on DB query error codes | Exception routing for PostgreSQL error codes (`IntegrityError`, `UniqueViolation`). |
| **Python 3.11**| Exception Groups (`except*`), `psycopg3` | `psycopg` (v3) rewrite with native async support | 2x faster binary protocol execution and connection pooling. |
| **Python 3.12**| Syntactic `type` statements, `@override` | Custom database model type alias statements | `type RowRecord = tuple[int, str, float]`. |
| **Python 3.13**| Free-threaded GIL-free CPython | High-throughput concurrent DB client operations | Thread-safe connection pool execution without GIL lock contention. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Database pagination and batch processing loops frequently utilize `range()` sequence objects:

```python
# Batch inserting 1,000 database records in chunks of 100 using range()
batch_size = 100
total_records = 1000

for offset in range(0, total_records, batch_size):
    print(f"Executing SQL query: SELECT * FROM mobile LIMIT {batch_size} OFFSET {offset}")
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
r = range(0, 1000, 100)
print(r.start)  # Output: 0
print(r.stop)   # Output: 1000
print(r.step)   # Output: 100

print(r.index(300))  # Output: 3
print(r.count(500))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
