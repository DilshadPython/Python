"""
Python 3.8 Feature Demonstration
--------------------------------
Highlights:
1. Assignment Expressions / Walrus Operator `:=` (PEP 572)
2. Positional-only parameters `/` (PEP 570)
3. Self-documenting f-strings `f"{expr=}"`
4. `TypedDict` and `Protocol` typing additions (PEP 589 / PEP 544)
5. `math.prod` for iterable product calculations
"""

import math
from typing import TypedDict, Literal, Protocol, List


# 1. Walrus Operator `:=` (PEP 572)
def demo_walrus_operator() -> None:
    print("--- 1. Demo: Walrus Operator := (PEP 572) ---")
    data_sample = ["  python ", "", "  3.8  ", "  rocks ", "  "]

    # Assign and test in list comprehension
    cleaned_items = [clean for item in data_sample if (clean := item.strip())]
    print(f"  Raw data:     {data_sample}")
    print(f"  Cleaned data: {cleaned_items}")

    # Assign and evaluate length condition
    if (n := len(cleaned_items)) > 3:
        print(f"  Count condition met: Found {n} items!")
    print()


# 2. Positional-Only Parameters `/` (PEP 570)
def compute_area(width: float, height: float, /, unit: str = "sq_m") -> str:
    """width and height MUST be passed positionally. unit can be positional or keyword."""
    area = width * height
    return f"{area:.2f} {unit}"


def demo_positional_only() -> None:
    print("--- 2. Demo: Positional-Only Parameters / (PEP 570) ---")
    # Positional call works
    res1 = compute_area(10.5, 4.0, unit="sq_ft")
    print(f"  Area result: {res1}")

    try:
        # Passing width as keyword argument triggers TypeError
        compute_area(width=10.5, height=4.0)  # type: ignore
    except TypeError as err:
        print(f"  Caught expected error passing positional-only parameter as keyword: {err}")
    print()


# 3. F-String Debugging Specifier `f"{expr=}"`
def demo_fstring_debug() -> None:
    print("--- 3. Demo: F-String f'{expr=}' ---")
    x = 42
    y = 100
    user_name = "Monika"
    
    print(f"  {x=}")
    print(f"  {y=}")
    print(f"  {user_name.upper()=}")
    print(f"  {x + y * 2=}")
    print()


# 4. TypedDict & Structural Typing (PEP 589 & PEP 544)
class ServerConfig(TypedDict):
    host: str
    port: int
    environment: Literal["development", "staging", "production"]


class Renderable(Protocol):
    def render(self) -> str:
        ...


class HTMLCard:
    def render(self) -> str:
        return "<div>Card Component</div>"


def render_component(item: Renderable) -> None:
    print(f"  Duck Typing / Protocol Render: {item.render()}")


def demo_typing_additions() -> None:
    print("--- 4. Demo: TypedDict & Protocol (PEP 589 & PEP 544) ---")
    config: ServerConfig = {
        "host": "localhost",
        "port": 8080,
        "environment": "production"
    }
    print(f"  TypedDict Server Config: {config}")

    card = HTMLCard()
    render_component(card)
    print()


# 5. Math Utilities (`math.prod`)
def demo_math_prod() -> None:
    print("--- 5. Demo: math.prod ---")
    numbers = [2, 3, 4, 5]
    product = math.prod(numbers)
    print(f"  Numbers: {numbers} -> Product: {product}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.8 FEATURE DEMO        ")
    print("========================================\n")
    demo_walrus_operator()
    demo_positional_only()
    demo_fstring_debug()
    demo_typing_additions()
    demo_math_prod()
