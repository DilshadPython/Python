"""
03-Advanced-Operators-and-Range/dunder_operator_overloading_and_bitwise_flags.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Custom Operator Overloading & Bitwise Flags Examples:
1. Custom Bitmask Permission Flags (__or__, __and__, __invert__)
2. Custom Polynomial / Number Wrapper with (__add__, __sub__, __eq__)
"""
from typing import Any


class PermissionFlags:
    """
    Demonstrates bitwise operator overloading (__or__, __and__, __invert__, __contains__)
    to implement Unix-style file permission flags (READ=4, WRITE=2, EXECUTE=1).
    """
    READ = 1 << 2   # 4 (0b100)
    WRITE = 1 << 1  # 2 (0b010)
    EXEC = 1 << 0   # 1 (0b001)

    def __init__(self, mask: int = 0) -> None:
        self.mask: int = mask

    def __or__(self, other: Any) -> "PermissionFlags":
        """Combine permissions using Bitwise OR (|)"""
        if isinstance(other, PermissionFlags):
            return PermissionFlags(self.mask | other.mask)
        elif isinstance(other, int):
            return PermissionFlags(self.mask | other)
        return NotImplemented

    def __and__(self, other: Any) -> "PermissionFlags":
        """Intersect permissions using Bitwise AND (&)"""
        if isinstance(other, PermissionFlags):
            return PermissionFlags(self.mask & other.mask)
        elif isinstance(other, int):
            return PermissionFlags(self.mask & other)
        return NotImplemented

    def __contains__(self, flag: int) -> bool:
        """Check if specific permission flag is set using 'in' operator"""
        return (self.mask & flag) == flag

    def __eq__(self, other: Any) -> bool:
        """Evaluate permission mask equality (==)"""
        if isinstance(other, PermissionFlags):
            return self.mask == other.mask
        return False
