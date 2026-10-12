"""
JSON Schema Parsing Demonstration (`example.py`).

This module demonstrates parsing JSON schema strings (`json.loads`) and iterating top-level keys.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from json_processor import JSONProcessor`: Modular JSON engine.
# =========================================================================
try:
    from json_tutorial.json_processor import JSONProcessor
except ImportError:
    from json_processor import JSONProcessor


RAW_DETAILS_JSON = """
{
    "properties": {
        "firstName": {
            "type": "string",
            "fname": "Dilshad"
        },
        "lastName": {
            "type": "string",
            "lname": "Abdulla"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}
"""


def main() -> None:
    """Run JSON schema dictionary inspection."""
    data = JSONProcessor.parse_string(RAW_DETAILS_JSON)
    print("Parsed JSON Schema Object:")
    print(data)

    print("\nProperties Keys:")
    for prop in data.get("properties", {}):
        print(f"  - {prop}")

    print("\nTop-Level Key Value Pairs:")
    for key, value in data.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
