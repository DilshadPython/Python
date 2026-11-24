"""
Python 3.4 Feature Demonstration
--------------------------------
Highlights:
1. `pathlib` for object-oriented path manipulation (PEP 428)
2. `enum` standard library module (PEP 435)
3. `functools.singledispatch` generic functions (PEP 443)
4. `statistics` mathematical functions (PEP 450)
"""

from enum import Enum, auto
from functools import singledispatch
from pathlib import Path
import statistics


# 1. Object-Oriented Paths (`pathlib`) (PEP 428)
def demo_pathlib() -> None:
    print("--- 1. Demo: pathlib Module (PEP 428) ---")
    current_dir = Path(".")
    abs_path = current_dir.resolve()
    
    print(f"  Current Directory: {abs_path}")
    print(f"  Parent Directory:  {abs_path.parent}")
    
    # Path join operator `/`
    sample_file = current_dir / "README.md"
    print(f"  Sample File Exists? {sample_file.exists()}")
    print(f"  File Name: {sample_file.name}, Extension: {sample_file.suffix}")
    print()


# 2. Enumerations (`enum`) (PEP 435)
class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()


def demo_enum() -> None:
    print("--- 2. Demo: enum Module (PEP 435) ---")
    current_status = Status.RUNNING
    print(f"  Current Status: {current_status}")
    print(f"  Status Name:    {current_status.name}")
    print(f"  Status Value:   {current_status.value}")
    print(f"  Is Completed?   {current_status is Status.COMPLETED}")
    print()


# 3. Single-Dispatch Generic Functions (`functools.singledispatch`) (PEP 443)
@singledispatch
def format_data(arg: object) -> str:
    return f"[Generic Output]: {arg}"


@format_data.register(int)
def _(arg: int) -> str:
    return f"[Integer Format]: {arg:,d}"


@format_data.register(list)
def _(arg: list) -> str:
    return f"[List Format ({len(arg)} items)]: " + ", ".join(str(x) for x in arg)


def demo_singledispatch() -> None:
    print("--- 3. Demo: functools.singledispatch (PEP 443) ---")
    print(f"  String argument: {format_data('Hello Python 3.4')}")
    print(f"  Integer argument: {format_data(1000000)}")
    print(f"  List argument:    {format_data([10, 20, 30])}")
    print()


# 4. Built-in Statistics (`statistics`) (PEP 450)
def demo_statistics() -> None:
    print("--- 4. Demo: statistics Module (PEP 450) ---")
    dataset = [2.5, 3.2, 4.8, 1.9, 5.5, 4.8]
    print(f"  Data: {dataset}")
    print(f"  Mean:               {statistics.mean(dataset):.2f}")
    print(f"  Median:             {statistics.median(dataset):.2f}")
    print(f"  Mode:               {statistics.mode(dataset)}")
    print(f"  Standard Deviation: {statistics.stdev(dataset):.2f}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.5 / 3.4 FEATURE DEMO   ")
    print("========================================\n")
    demo_pathlib()
    demo_enum()
    demo_singledispatch()
    demo_statistics()
