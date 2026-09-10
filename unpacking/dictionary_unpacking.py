"""
Keyword Mapping Dictionary Unpacking Module (`dictionary_unpacking.py`).

This module demonstrates unpacking dictionary key-value mappings into keyword function
parameters using the double asterisk (`**`) unpacking operator.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System execution utilities.
# - `from typing import Any, Dict`: PEP 484 type hint generics.
# - `from sequence_unpacking import calculate_volume_inches`: Volume calculation helper.
# =========================================================================
import sys
from typing import Any, Dict

try:
    from unpacking.sequence_unpacking import calculate_volume_inches
except ImportError:
    from sequence_unpacking import calculate_volume_inches


def unpack_dictionary_dimensions(dimensions_dict: Dict[str, float]) -> float:
    """Unpack a dictionary mapping into keyword parameters of calculate_volume_inches.

    Args:
        dimensions_dict (Dict[str, float]): Dictionary containing 'length', 'width', 'height'.

    Returns:
        float: Calculated volume in cubic inches.
    """
    # Double asterisk (**) unpacks dictionary keys into named keyword arguments
    return calculate_volume_inches(**dimensions_dict)


def merge_dictionaries(default_config: Dict[str, Any], user_config: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries using double asterisk (**) dictionary unpacking operator.

    Args:
        default_config (Dict[str, Any]): Base default options dictionary.
        user_config (Dict[str, Any]): Overriding user options dictionary.

    Returns:
        Dict[str, Any]: Merged configuration dictionary.
    """
    # Unpack both dictionaries into a new literal dictionary mapping
    return {**default_config, **user_config}


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for dictionary unpacking demonstration."""
    print("=== Keyword Dictionary Unpacking Demonstration ===")

    coins_dict: Dict[str, float] = {"length": 15.0, "width": 10.0, "height": 8.0}
    volume = unpack_dictionary_dimensions(coins_dict)

    print(f"Dimensions Dict: {coins_dict}")
    print(f"Calculated Volume (total(**coins_dict)): {volume} Cubic Inches")

    defaults = {"host": "localhost", "port": 5432, "debug": False}
    overrides = {"debug": True, "port": 5433}
    merged = merge_dictionaries(defaults, overrides)
    print(f"Merged Config ({'{**defaults, **overrides}'}): {merged}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
