"""
Intermediate Level JSON Customization Module (`intermediate_json.py`).

This module provides functional JSON serialization patterns designed for intermediate developers
(custom `json.JSONEncoder` subclassing for non-standard types like Dataclasses and `datetime`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from dataclasses import dataclass, asdict`: Python 3.7+ dataclasses.
# - `from datetime import datetime`: Date and time objects.
# - `import json`: Core JSON encoding and decoding module.
# - `import sys`: System execution utilities.
# - `from typing import Any, Dict`: PEP 484 type hint generics.
# =========================================================================
from dataclasses import asdict, dataclass
from datetime import datetime
import json
import sys
from typing import Any, Dict


@dataclass
class ProjectMetadata:
    """Dataclass holding project metadata information."""

    title: str
    started_year: int
    author: str
    created_at: datetime
    skills: list[str]


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSONEncoder subclass handling `datetime` and `@dataclass` instances."""

    def default(self, obj: Any) -> Any:
        """Override default encoder method to handle non-serializable objects.

        Args:
            obj (Any): Target object to encode.

        Returns:
            Any: JSON-compatible primitive object.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        return super().default(obj)


def serialize_custom_metadata(metadata: ProjectMetadata) -> str:
    """Serialize a dataclass instance containing datetime objects using `CustomJSONEncoder`.

    Args:
        metadata (ProjectMetadata): Input dataclass instance.

    Returns:
        str: Encoded JSON string with sorted keys and indent formatting.
    """
    return json.dumps(
        metadata,
        cls=CustomJSONEncoder,
        indent=4,
        sort_keys=True,
    )


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate JSON demonstration."""
    print("=== Intermediate Level JSON Customization ===")

    project = ProjectMetadata(
        title="Python and JSON",
        started_year=2018,
        author="Dilshad Abdulla",
        created_at=datetime.now(),
        skills=["Python", "Django", "Bootstrap", "JSON", "Flask"],
    )

    encoded_json = serialize_custom_metadata(project)
    print(f"Custom Encoded Dataclass JSON:\n{encoded_json}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
