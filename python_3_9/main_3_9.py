"""
Python 3.9 Feature Demonstration
--------------------------------
Highlights:
1. Dictionary Union Operators `|` and `|=` (PEP 584)
2. Built-in Generic Types `list[T]`, `dict[K, V]` (PEP 585)
3. String `removeprefix()` and `removesuffix()` (PEP 616)
4. IANA Time Zone support (`zoneinfo` module) (PEP 615)
5. `math.lcm` (Least Common Multiple)
"""

from datetime import datetime
import math
from zoneinfo import ZoneInfo


# 1. Dict Union Operators `|` and `|=` (PEP 584)
def demo_dict_union() -> None:
    print("--- 1. Demo: Dict Union Operators (PEP 584) ---")
    default_config = {"host": "127.0.0.1", "port": 8000, "debug": True}
    user_config = {"port": 9000, "log_level": "INFO"}

    # Merge into a new dict using `|`
    final_config = default_config | user_config
    print(f"  Merged Dict (|):  {final_config}")

    # In-place update using `|=`
    settings = {"theme": "light"}
    settings |= {"theme": "dark", "notifications": True}
    print(f"  In-place Update (|=): {settings}")
    print()


# 2. Built-in Generics (PEP 585)
def process_scores(scores: dict[str, list[int]]) -> list[tuple[str, float]]:
    """Native collections list and dict used directly as generics without importing from typing!"""
    results: list[tuple[str, float]] = []
    for name, score_list in scores.items():
        avg = sum(score_list) / len(score_list) if score_list else 0.0
        results.append((name, round(avg, 2)))
    return results


def demo_builtin_generics() -> None:
    print("--- 2. Demo: Built-in Generics (PEP 585) ---")
    data: dict[str, list[int]] = {
        "Alice": [90, 95, 88],
        "Bob": [78, 85, 80]
    }
    processed = process_scores(data)
    print(f"  Processed Student Averages: {processed}")
    print()


# 3. String removeprefix() and removesuffix() (PEP 616)
def demo_string_strip() -> None:
    print("--- 3. Demo: removeprefix & removesuffix (PEP 616) ---")
    raw_url = "https://www.python.org/index.html"
    raw_file = "dataset_2026_final.csv"

    clean_url = raw_url.removeprefix("https://www.")
    clean_file = raw_file.removesuffix(".csv")

    print(f"  Original URL:  {raw_url}")
    print(f"  Stripped URL:  {clean_url}")
    print(f"  Original File: {raw_file}")
    print(f"  Stripped File: {clean_file}")
    print()


# 4. Standard IANA Timezone Support (`zoneinfo`) (PEP 615)
def demo_zoneinfo() -> None:
    print("--- 4. Demo: zoneinfo Module (PEP 615) ---")
    now_utc = datetime.now(ZoneInfo("UTC"))
    now_tokyo = now_utc.astimezone(ZoneInfo("Asia/Tokyo"))
    now_ny = now_utc.astimezone(ZoneInfo("America/New_York"))

    print(f"  UTC Time:      {now_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"  Tokyo Time:    {now_tokyo.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"  New York Time: {now_ny.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print()


# 5. Math LCM (Least Common Multiple)
def demo_math_lcm() -> None:
    print("--- 5. Demo: math.lcm ---")
    val = math.lcm(12, 18, 24)
    print(f"  LCM of (12, 18, 24): {val}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.9 FEATURE DEMO        ")
    print("========================================\n")
    demo_dict_union()
    demo_builtin_generics()
    demo_string_strip()
    demo_zoneinfo()
    demo_math_lcm()
