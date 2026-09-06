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

#### Step 4 (Optional): Install MySQL Server on Windows
- Download the official MySQL Installer from [MySQL Community Downloads](https://dev.mysql.com/downloads/installer/).
- Run the installer and select **Developer Default**.
- Remember your `root` password for configuration in `mysql_db.py`.

---

### 🍎 2. macOS Installation Guide

#### Step 1: Open Terminal
Press `Cmd + Space`, type `Terminal`, and press `Enter`.

#### Step 2: Ensure Python 3 is Installed
```bash
python3 --version
```
*(If Python is not installed, install it using Homebrew: `brew install python3`)*

#### Step 3: Create and Activate a Virtual Environment
```bash
# Navigate to your project folder
cd /path/to/your/project/database

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 5 (Optional): Install MySQL Server on macOS
```bash
# Install MySQL using Homebrew
brew install mysql

# Start MySQL Service
brew services start mysql
```

---

### 🐧 3. Linux Installation Guide (Ubuntu / Debian / Fedora / Arch)

#### Step 1: Open Terminal (`Ctrl + Alt + T`)

#### Step 2: Install Python 3, venv, and pip
- **Ubuntu / Debian**:
  ```bash
  sudo apt update
  sudo apt install -y python3 python3-pip python3-venv
  ```
- **Fedora / RHEL**:
  ```bash
  sudo dnf install -y python3 python3-pip
  ```
- **Arch Linux**:
  ```bash
  sudo pacman -S python python-pip
  ```

#### Step 3: Create and Activate a Virtual Environment
```bash
cd /path/to/your/project/database
python3 -m venv venv
source venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 5 (Optional): Install MySQL / MariaDB Server on Linux
- **Ubuntu / Debian**:
  ```bash
  sudo apt install -y mysql-server
  sudo systemctl start mysql
  ```

---

## 📦 Requirements File (`requirements.txt`)

```text
# Official MySQL driver
mysql-connector-python>=8.0.0

# Pure Python MySQL driver alternative
pymysql>=1.0.0
```

---

## 📁 Directory Architecture

```text
database/
├── README.md                  # Complete documentation and beginner guide
├── requirements.txt           # External python package dependencies
├── mysql_db.py                # Object-oriented MySQL database manager
└── sqlite3/
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

## 🏁 Quick Start: Beginner Code Tutorial

If you are starting for the first time, run the interactive beginner starter script:

```bash
python3 sqlite3/beginner_starter.py
```

### Beginner Code Walkthrough ([sqlite3/beginner_starter.py](file:///home/monika/PycharmProjects/Devel/Python/database/sqlite3/beginner_starter.py))

```python
import sqlite3

# 1. Connect to Database (Creates file if missing)
with sqlite3.connect("starter_demo.db") as connection:
    cursor = connection.cursor()

    # 2. Create Table (Schema definition with data types)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER DEFAULT 0
        )
    """)

    # 3. Create / Insert Records
    cursor.execute(
        "INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)",
        ("Wireless Mouse", 25.50, 100)
    )
    connection.commit()  # Save changes to disk

    # 4. Read Records
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 5. Update Records
    cursor.execute("UPDATE Products SET price = ? WHERE name = ?", (19.99, "Wireless Mouse"))
    connection.commit()

    # 6. Delete Records
    cursor.execute("DELETE FROM Products WHERE name = ?", ("Wireless Mouse",))
    connection.commit()
```

---

## 🛠️ Detailed Method & File Reference

### 1. `mysql_db.py` - MySQL Database Manager

#### Class: `MySQLDatabaseManager`

##### Attributes
- `config` (`Dict[str, Any]`): Connection parameters dictionary (host, user, password, database, port).
- `connection` (`Optional[Any]`): Active MySQL connection object instance.

##### Methods
1. `__init__(self, config: Dict[str, Any]) -> None`: Initializes manager with configuration parameters.
2. `connect(self) -> bool`: Establishes connection to MySQL server.
3. `disconnect(self) -> None`: Safely closes the active connection.
4. `create_table(self, query: str) -> None`: Executes DDL statement to create a table.
5. `execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]`: Executes `SELECT` queries and returns results.
6. `execute_update(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> int`: Executes `INSERT`/`UPDATE`/`DELETE` DML statements and commits changes.

##### Usage Example:
```python
from mysql_db import MySQLDatabaseManager

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "test_db",
    "port": 3306
}

db = MySQLDatabaseManager(db_config)
if db.connect():
    db.create_table("CREATE TABLE IF NOT EXISTS Users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
    db.execute_update("INSERT INTO Users (name) VALUES (%s)", ("Alice",))
    print(db.execute_query("SELECT * FROM Users"))
    db.disconnect()
```

---

### 2. SQLite Modules Summary

| Module | Description | Function / Entry Point |
| :--- | :--- | :--- |
| **`sqlite3/beginner_starter.py`** | Comprehensive beginner guide covering all CRUD steps. | `run_beginner_tutorial()` |
| **`sqlite3/connect_db.py`** | Basic database connection and cursor closing demo. | `connect_database()` |
| **`sqlite3/create_table.py`** | Demonstrates `CREATE TABLE IF NOT EXISTS`. | `create_car_table()` |
| **`sqlite3/insert_static_data.py`** | Demonstrates batch inserting static tuples into SQLite. | `setup_database()` |
| **`sqlite3/insert_dynamic_data.py`** | Demonstrates dynamic parameterized user input insertion. | `dynamic_insert_data()` |
| **`sqlite3/read_all_data.py`** | Reads all rows from database (`SELECT *`). | `read_all_records()` |
| **`sqlite3/read_filtered_data.py`** | Reads rows matching condition (`WHERE Name = ?`). | `read_filtered_records()` |
| **`sqlite3/read_by_user_input.py`** | Search database by brand input parameter. | `read_by_user_input()` |
| **`sqlite3/read_by_multiple_inputs.py`** | Search using multiple compound parameters (`Name` and `Version`). | `read_by_multiple_inputs()` |
| **`sqlite3/read_with_limit.py`** | Paginated query results using `LIMIT N`. | `read_with_limit()` |
| **`sqlite3/update_data.py`** | Modifies existing rows using `UPDATE`. | `update_records()` |
| **`sqlite3/delete_data.py`** | Demonstrates `DELETE` within active transaction. | `delete_records()` |
| **`sqlite3/delete_data_with_commit.py`** | Demonstrates `DELETE` with explicit transaction `commit()`. | `delete_records_with_commit()` |
| **`sqlite3/email_counter_crud.py`** | Parses mail logs and aggregates counts per sender email address. | `process_email_log()` |

---

## 💡 Best Practices Checklist

1. **Use Parameterized Queries**: Always use `?` (SQLite) or `%s` (MySQL) to pass variables safely and prevent SQL injection.
2. **Always Use Context Managers**: Use `with sqlite3.connect(...) as connection:` to handle connection cleanup automatically.
3. **Commit Transactions**: DML commands (`INSERT`, `UPDATE`, `DELETE`) require `connection.commit()` to persist changes to disk.
