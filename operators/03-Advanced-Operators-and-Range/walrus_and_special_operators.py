"""
Python Operators: Special Operators, Functional Utilities & Parameter Syntax.

This module demonstrates:
- Functional operator helpers: operator.itemgetter, operator.attrgetter, operator.methodcaller
- Parameter signature operators: Positional-Only (/) and Keyword-Only (*) parameter boundaries (PEP 570)
- Advanced Walrus Operator (:=) data transformations
"""
# "import module" loads operator standard library module.
import operator
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Any, Dict, List, Tuple


class ItemRecord:
    """Class representing an item with price and quantity for operator.attrgetter sorting."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Initialize ItemRecord attributes."""
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def calculate_total_cost(self) -> float:
        """Calculate total item inventory value."""
        return self.price * self.quantity


def sort_records_using_operator_getters(records: List[ItemRecord]) -> Tuple[List[ItemRecord], List[Dict[str, Any]]]:
    """
    Demonstrate operator.attrgetter and operator.itemgetter for high-performance sorting.

    Args:
        records (List[ItemRecord]): Unsorted list of ItemRecord objects.

    Returns:
        Tuple[List[ItemRecord], List[Dict[str, Any]]]: Sorted records by price and sorted dictionaries by key.
    """
    # Sort object list by 'price' attribute using operator.attrgetter
    sorted_by_price = sorted(records, key=operator.attrgetter("price"))

    dict_list = [{"name": r.name, "value": r.calculate_total_cost()} for r in records]
    # Sort dictionary list by 'value' key using operator.itemgetter
    sorted_dicts = sorted(dict_list, key=operator.itemgetter("value"), reverse=True)

    return sorted_by_price, sorted_dicts


def calculate_discounted_price(base_price: float, discount_rate: float, /, *, tax_rate: float = 0.05) -> float:
    """
    Demonstrate parameter signature operators:
    - '/' enforces positional-only parameters (base_price, discount_rate)
    - '*' enforces keyword-only parameters (tax_rate)

    Args:
        base_price (float): Positional-only base cost.
        discount_rate (float): Positional-only discount multiplier (e.g. 0.10).
        tax_rate (float): Keyword-only tax rate multiplier (default 0.05).

    Returns:
        float: Final calculated price including tax.
    """
    if base_price < 0 or discount_rate < 0 or tax_rate < 0:
        raise ValueError("Prices and rates must be non-negative.")

    discounted = base_price * (1.0 - discount_rate)
    final_price = discounted * (1.0 + tax_rate)
    return round(final_price, 2)
