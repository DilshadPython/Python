"""Multiple Inheritance and Method Resolution Order (MRO) Module.

This module demonstrates multiple inheritance in Python and details how the C3 Linearization
algorithm determines the Method Resolution Order (MRO) for method resolution.
"""

from typing import List, Tuple, Type


class BaseA:
    """Base class A."""

    def execute_action(self) -> str:
        """Execute action in BaseA."""
        return "Executed in BaseA"


class SubB(BaseA):
    """Subclass B inheriting from BaseA."""

    pass


class BaseC:
    """Independent Base class C."""

    def execute_action(self) -> str:
        """Execute action in BaseC."""
        return "Executed in BaseC"


class DiamondC(BaseA):
    """Subclass C inheriting from BaseA (Diamond Pattern)."""

    def execute_action(self) -> str:
        """Execute action in DiamondC overriding BaseA."""
        return "Executed in DiamondC"


class DerivedD1(SubB, BaseC):
    """Class D1 inheriting from SubB (which inherits BaseA) and independent BaseC."""

    pass


class DerivedD2(SubB, DiamondC):
    """Class D2 inheriting from SubB and DiamondC (both inheriting from BaseA - Diamond inheritance)."""

    pass


def get_mro_class_names(cls: Type[object]) -> List[str]:
    """Return list of class names in Method Resolution Order.

    Args:
        cls: Class to inspect.

    Returns:
        List of class names.
    """
    return [c.__name__ for c in cls.__mro__]


if __name__ == "__main__":
    print("=== Multiple Inheritance & MRO Demonstration ===")

    # 1. Non-diamond multiple inheritance
    d1 = DerivedD1()
    print("DerivedD1 Action Result:", d1.execute_action())
    print("DerivedD1 MRO:", get_mro_class_names(DerivedD1))

    # 2. Diamond multiple inheritance
    d2 = DerivedD2()
    print("\nDerivedD2 Action Result:", d2.execute_action())
    print("DerivedD2 MRO:", get_mro_class_names(DerivedD2))
