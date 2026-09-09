"""
Universally Unique Identifier (UUID) Generator & Utilities.

This module demonstrates UUID generation across standard variants:
- UUID v1: Host MAC address and timestamp-based identifier.
- UUID v3: MD5 hash namespace-based identifier.
- UUID v4: Randomly generated identifier.
- UUID v5: SHA-1 hash namespace-based identifier.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI entry point handling.
# - `import uuid`: Standard library implementation of RFC 4122 UUID objects.
# - `from typing import Dict, List`: PEP 484 type annotations for generic structures.
# =========================================================================
import sys
import uuid
from typing import Dict, List


def generate_uuid_v1(count: int = 1) -> List[uuid.UUID]:
    """Generate a list of host MAC and timestamp-based UUID v1 identifiers.

    Args:
        count (int): Number of UUID v1 instances to generate. Defaults to 1.

    Returns:
        List[uuid.UUID]: List of generated UUID v1 objects.

    Raises:
        TypeError: If count is not an integer.
        ValueError: If count is not positive.
    """
    if not isinstance(count, int):
        raise TypeError(f"Count must be an integer, got {type(count).__name__}")
    if count <= 0:
        raise ValueError(f"Count must be a positive integer, got {count}")

    return [uuid.uuid1() for _ in range(count)]


def generate_uuid_v3(name: str, namespace: uuid.UUID = uuid.NAMESPACE_DNS) -> uuid.UUID:
    """Generate an MD5 hash namespace-based UUID v3 identifier.

    Args:
        name (str): Identifier seed string.
        namespace (uuid.UUID): UUID namespace context. Defaults to NAMESPACE_DNS.

    Returns:
        uuid.UUID: Generated UUID v3 object.

    Raises:
        TypeError: If name is not a string or namespace is invalid.
    """
    if not isinstance(name, str):
        raise TypeError(f"Name must be a string, got {type(name).__name__}")
    if not isinstance(namespace, uuid.UUID):
        raise TypeError(f"Namespace must be a UUID instance, got {type(namespace).__name__}")

    return uuid.uuid3(namespace, name)


def generate_uuid_v4(count: int = 1) -> List[uuid.UUID]:
    """Generate a list of cryptographically random UUID v4 identifiers.

    Args:
        count (int): Number of UUID v4 instances to generate. Defaults to 1.

    Returns:
        List[uuid.UUID]: List of generated UUID v4 objects.

    Raises:
        TypeError: If count is not an integer.
        ValueError: If count is not positive.
    """
    if not isinstance(count, int):
        raise TypeError(f"Count must be an integer, got {type(count).__name__}")
    if count <= 0:
        raise ValueError(f"Count must be a positive integer, got {count}")

    return [uuid.uuid4() for _ in range(count)]


def generate_uuid_v5(name: str, namespace: uuid.UUID = uuid.NAMESPACE_DNS) -> uuid.UUID:
    """Generate a SHA-1 hash namespace-based UUID v5 identifier.

    Args:
        name (str): Identifier seed string.
        namespace (uuid.UUID): UUID namespace context. Defaults to NAMESPACE_DNS.

    Returns:
        uuid.UUID: Generated UUID v5 object.

    Raises:
        TypeError: If name is not a string or namespace is invalid.
    """
    if not isinstance(name, str):
        raise TypeError(f"Name must be a string, got {type(name).__name__}")
    if not isinstance(namespace, uuid.UUID):
        raise TypeError(f"Namespace must be a UUID instance, got {type(namespace).__name__}")

    return uuid.uuid5(namespace, name)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point displaying UUID v1, v3, v4, and v5 demonstrations."""
    print("=== UUID Generation Suite (RFC 4122) ===")

    print("\n1. UUID v1 (Host MAC & Timestamp):")
    for u1 in generate_uuid_v1(3):
        print(f"   UUID v1: {u1} [Version: {u1.version}]")

    print("\n2. UUID v3 (MD5 Namespace):")
    u3 = generate_uuid_v3("python.org")
    print(f"   UUID v3 ('python.org'): {u3} [Version: {u3.version}]")

    print("\n3. UUID v4 (Cryptographically Random):")
    for u4 in generate_uuid_v4(3):
        print(f"   UUID v4: {u4} [Version: {u4.version}]")

    print("\n4. UUID v5 (SHA-1 Namespace):")
    u5 = generate_uuid_v5("python.org")
    print(f"   UUID v5 ('python.org'): {u5} [Version: {u5.version}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
