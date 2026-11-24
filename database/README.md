# Python Database Operations & Management Module

Welcome to the **Python Database Module**. This directory provides a structured, educational, and production-ready collection of Python scripts demonstrating relational database interactions using both SQLite (Python standard library) and MySQL (external server connection driver).

---

## 🚀 Beginner's Guide: Core Database Concepts & Definitions

If you are new to databases, this section will help you understand all fundamental concepts before writing code.

### 📚 Core Terminology Definitions

| Term | Definition | Analogous Concept |
| :--- | :--- | :--- |
| **Database (DB)** | An organized collection of structured data stored electronically on a computer system. | A digital filing cabinet or workbook. |
| **Relational Database (RDBMS)** | A database that organizes data into tables linked by predefined relationships. | Excel workbook with multiple interlinked sheets. |
| **Table** | A collection of related data entries organized in vertical columns and horizontal rows. | A single spreadsheet tab/sheet. |
| **Column / Field** | A vertical data attribute representing a specific type of information (e.g., `name`, `age`). | A single spreadsheet column header. |
| **Row / Record** | A single horizontal data entry containing values for all attributes of an item. | A single spreadsheet row filled with data. |
| **Primary Key (PK)** | A unique identifier for every record in a table (e.g., `id=101`). No two rows can share the same PK. | A Social Security Number or Student ID. |
| **Foreign Key (FK)** | A column in one table that references the Primary Key of another table to create a link between them. | A reference code pointing to another sheet. |
| **SQL** | **Structured Query Language** - The universal language used to communicate with relational databases. | The command language for database requests. |
| **CRUD** | Acronym for the 4 basic database operations: **C**reate, **R**ead, **U**pdate, and **D**elete. | Add, View, Edit, Remove operations. |

---

### 🔤 Database Data Types (Definitions & Examples)

Databases enforce data types on each column to ensure data consistency and integrity.

| Data Type | SQL Keyword | Description | Python Equivalent | Example Values |
| :--- | :--- | :--- | :--- | :--- |
| **Integer** | `INTEGER` / `INT` | Whole numbers (positive, negative, or zero). | `int` | `1`, `42`, `-10`, `2026` |
| **Floating Point** | `REAL` / `FLOAT` / `DOUBLE` | Decimal numbers with fractional parts. | `float` | `19.99`, `3.14159`, `-0.05` |
| **Text / String** | `TEXT` / `VARCHAR(N)` | Text characters or strings. `VARCHAR(N)` limits string length to `N`. | `str` | `"Alice"`, `"Toyota Camry"`, `"email@example.com"` |
| **Binary Data** | `BLOB` | Binary Large Object. Used for raw bytes like images or encrypted data. | `bytes` | `b'\x89PNG...'` |
| **Null Value** | `NULL` | Represents missing, empty, or unknown values. | `None` | `None` |

---

## 💻 OS-Specific Installation Guide

Python includes the `sqlite3` module by default. For external MySQL database management, follow the setup steps for your operating system below.

### 🪟 1. Windows Installation Guide

#### Step 1: Open Command Prompt or PowerShell
Press `Win + R`, type `cmd` or `powershell`, and press `Enter`.

#### Step 2: Create and Activate a Virtual Environment
```cmd
:: Navigate to your project folder
cd C:\path\to\your\project\database

:: Create virtual environment named 'venv'
python -m venv venv

:: Activate virtual environment
venv\Scripts\activate
```

#### Step 3: Install Required Dependencies
```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🍎 2. macOS Installation Guide

#### Step 1: Open Terminal (`Cmd + Space` -> `Terminal`)

#### Step 2: Create and Activate Virtual Environment
```bash
cd /path/to/your/project/database
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🐧 3. Linux Installation Guide (Ubuntu / Debian / Fedora / Arch)

#### Step 1: Open Terminal (`Ctrl + Alt + T`)

#### Step 2: Create and Activate Virtual Environment
```bash
cd /path/to/your/project/database
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧪 Automated Testing & Security Verification

To guarantee code security, data integrity, and prevent regression bugs or SQL Injection vulnerabilities, an automated unit test suite is included in the `tests/` directory.

### 🛡️ What is Tested for Security & Stability?

1. **SQL Injection Defense**: Tests tautology attacks (`' OR '1'='1`), piggybacked `DROP TABLE` attempts, and `UNION` query injection payloads against all search functions to ensure parameters are properly bound.
2. **SQLite Operations Test**: Tests connection management, table creation, batch static insertion, dynamic user input handling, filtering, limit pagination, updates, and deletions in isolated temporary database instances (`tempfile`).
3. **MySQL Manager Test**: Tests configuration validation, connection failure handling, fallback states, and mock query executions.

### 🏃 How to Run the Test Suite

Run the full test suite using Python's built-in `unittest` runner:

```bash
python3 -m unittest discover -v -s tests
```

Or using `pytest`:

```bash
pytest -v tests/
```

---

## 📁 Directory Architecture

```text
database/
├── README.md                  # Complete documentation, setup, and testing guide
├── requirements.txt           # External package dependencies (MySQL drivers, pytest)
├── mysql_db.py                # Object-oriented MySQL database manager
├── tests/
│   ├── __init__.py            # Test package marker
│   ├── test_sqlite_modules.py # SQLite CRUD operations test suite
│   ├── test_mysql_manager.py  # MySQLDatabaseManager test suite
│   └── test_security_sql_injection.py # Security & SQL Injection test suite
└── sqlite_db/
    ├── __init__.py            # Package marker
    ├── beginner_starter.py    # Step-by-step beginner tutorial script
    ├── connect_db.py          # Connection and cursor initialization demo
    ├── create_table.py         # Table schema creation DDL demo
    ├── insert_static_data.py  # Static dataset batch insertion demo
    ├── insert_dynamic_data.py # Dynamic user input record insertion demo
    ├── read_all_data.py       # Full table query (SELECT *) demo
    ├── read_filtered_data.py  # Conditional row query (WHERE) demo
    ├── read_by_user_input.py  # Dynamic single-parameter search demo
    ├── read_by_multiple_inputs.py # Compound multi-parameter search demo
    ├── read_with_limit.py     # Pagination query (LIMIT) demo
    ├── update_data.py         # Record update (UPDATE) demo
    ├── delete_data.py         # Row deletion (DELETE) demo
    ├── delete_data_with_commit.py # Persistent deletion with explicit commit demo
    └── email_counter_crud.py  # Log aggregation CRUD counter demo
```

---

## 💡 Best Practices Checklist

1. **Use Parameterized Queries**: Always use `?` (SQLite) or `%s` (MySQL) to pass variables safely and prevent SQL injection.
2. **Always Use Context Managers**: Use `with sqlite3.connect(...) as connection:` to handle connection cleanup automatically.
3. **Commit Transactions**: DML commands (`INSERT`, `UPDATE`, `DELETE`) require `connection.commit()` to persist changes to disk.
4. **Run Unit Tests**: Execute `python3 -m unittest discover -v -s tests` before committing code changes.
