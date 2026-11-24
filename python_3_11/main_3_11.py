"""
Python 3.11 Feature Demonstration
---------------------------------
Highlights:
1. Exception Groups and `except*` (PEP 654)
2. Standard TOML Parsing with `tomllib` (PEP 680)
3. `typing.Self` for fluent builders (PEP 673)
4. `asyncio.TaskGroup` for structured concurrency
5. `enum.StrEnum` string enums
"""

import asyncio
from enum import StrEnum
import tomllib
from typing import Self


# 1. Self Type Annotation (PEP 673)
class QueryBuilder:
    def __init__(self) -> None:
        self._table: str = ""
        self._conditions: list[str] = []

    def from_table(self, table_name: str) -> Self:
        self._table = table_name
        return self

    def where(self, condition: str) -> Self:
        self._conditions.append(condition)
        return self

    def build(self) -> str:
        sql = f"SELECT * FROM {self._table}"
        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)
        return sql


def demo_self_type() -> None:
    print("--- 1. Demo: typing.Self (PEP 673) ---")
    query = (
        QueryBuilder()
        .from_table("users")
        .where("is_active = 1")
        .where("age >= 18")
        .build()
    )
    print(f"  Fluent Query Output: {query}")
    print()


# 2. TOML Parsing (`tomllib`) (PEP 680)
def demo_tomllib() -> None:
    print("--- 2. Demo: tomllib Module (PEP 680) ---")
    toml_data = """
    [tool.app]
    name = "PythonicApp"
    version = "3.11.0"
    features = ["fast_cpython", "tomllib", "task_group"]

    [tool.app.database]
    port = 5432
    enabled = true
    """

    config = tomllib.loads(toml_data)
    print(f"  Parsed TOML Config: {config}")
    print(f"  App Name: {config['tool']['app']['name']}")
    print(f"  Database Enabled? {config['tool']['app']['database']['enabled']}")
    print()


# 3. String Enum (`enum.StrEnum`)
class Environment(StrEnum):
    DEV = "development"
    STAGING = "staging"
    PROD = "production"


def demo_str_enum() -> None:
    print("--- 3. Demo: enum.StrEnum ---")
    env = Environment.PROD
    print(f"  Environment: {env}")
    print(f"  Is string instance? {isinstance(env, str)}")
    print(f"  Uppercase string check: {env.upper()}")
    print()


# 4. Async Task Group & Exception Handling (`asyncio.TaskGroup`)
async def async_task(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Task '{name}' completed in {delay}s"


async def demo_async_task_group() -> None:
    print("--- 4. Demo: asyncio.TaskGroup ---")
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(async_task("A", 0.05))
        t2 = tg.create_task(async_task("B", 0.02))

    print(f"  Result 1: {t1.result()}")
    print(f"  Result 2: {t2.result()}")
    print()


# 5. Exception Groups & except* (PEP 654)
def demo_exception_groups() -> None:
    print("--- 5. Demo: ExceptionGroup & except* (PEP 654) ---")
    eg = ExceptionGroup(
        "Multiple task failures",
        [ValueError("Invalid numeric value"), TypeError("Expected string, got int")]
    )

    try:
        raise eg
    except* ValueError as eg_val:
        print(f"  Caught value errors via except*: {eg_val.exceptions}")
    except* TypeError as eg_type:
        print(f"  Caught type errors via except*:  {eg_type.exceptions}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.11 FEATURE DEMO       ")
    print("========================================\n")
    demo_self_type()
    demo_tomllib()
    demo_str_enum()
    asyncio.run(demo_async_task_group())
    demo_exception_groups()
