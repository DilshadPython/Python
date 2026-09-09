"""
Python 3.5 Feature Demonstration
--------------------------------
Highlights:
1. `async` and `await` syntax (PEP 492)
2. Type annotations (`typing` module) (PEP 484)
3. Generalized unpacking (`*` and `**`) (PEP 448)
4. Matrix multiplication `@` operator (PEP 465)
5. Directory scanning with `os.scandir` (PEP 471)
"""

import asyncio
import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple


# 1. Native Coroutines with `async` / `await` (PEP 492)
async def fetch_data(source_id: int) -> Dict[str, str]:
    await asyncio.sleep(0.05)  # Non-blocking async sleep
    return {"id": str(source_id), "status": "active"}


async def run_async_demo() -> None:
    print("--- 1. Demo: Native async / await (PEP 492) ---")
    results = await asyncio.gather(fetch_data(101), fetch_data(102))
    for res in results:
        print(f"  Async Result: {res}")
    print()


# 2. Generalized Unpacking (PEP 448)
def demo_generalized_unpacking() -> None:
    print("--- 2. Demo: Generalized Unpacking (PEP 448) ---")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = [*list1, 99, *list2]
    print(f"  Merged List: {merged_list}")

    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged_dict = {**dict1, "override_b": 20, **dict2}
    print(f"  Merged Dict: {merged_dict}")
    print()


# 3. Matrix Multiplication `@` Operator (PEP 465)
class SimpleMatrix:
    def __init__(self, data: List[List[float]]):
        self.data = data

    def __matmul__(self, other: "SimpleMatrix") -> "SimpleMatrix":
        # Simplified 2x2 matrix dot product for demonstration
        a = self.data
        b = other.data
        result = [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
        return SimpleMatrix(result)

    def __repr__(self) -> str:
        return f"Matrix({self.data})"


def demo_matrix_operator() -> None:
    print("--- 3. Demo: Matrix Operator '@' (PEP 465) ---")
    m1 = SimpleMatrix([[1, 2], [3, 4]])
    m2 = SimpleMatrix([[5, 6], [7, 8]])
    product = m1 @ m2  # Triggers __matmul__
    print(f"  {m1} @ {m2} = {product}")
    print()


# 4. Fast Directory Scanning with `os.scandir` (PEP 471)
def demo_scandir() -> None:
    print("--- 4. Demo: os.scandir (PEP 471) ---")
    print("  Scanning current directory:")
    with os.scandir(".") as entries:
        for entry in entries:
            if entry.is_file():
                print(f"   [File] {entry.name:<20} Size: {entry.stat().st_size} bytes")
            elif entry.is_dir():
                print(f"   [Dir]  {entry.name}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.5 FEATURE DEMO        ")
    print("========================================\n")
    asyncio.run(run_async_demo())
    demo_generalized_unpacking()
    demo_matrix_operator()
    demo_scandir()
