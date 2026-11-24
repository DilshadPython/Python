"""
Module Import vs Direct Script Execution Analysis Module.

This module demonstrates:
- How importing a module dynamically changes its internal __name__ attribute.
- Executing functions imported from external files safely.
- Comparing direct invocation (__name__ == '__main__') with imported execution.
"""

# Import pathlib and sys to configure folder import paths
from pathlib import Path
import sys

# Ensure 01-Fundamentals can be imported
sys.path.insert(0, str(Path(__file__).parent.parent / "01-Fundamentals"))

# Import functions from fundamentals module
from name_attribute_basics import format_greeting, get_execution_context


def analyze_imported_module() -> dict[str, str]:
    """Analyze execution context when functions are imported into another module.

    Returns:
        dict[str, str]: Context information showing current module vs imported module behavior.
    """
    imported_context = get_execution_context()
    return {
        "current_file_module": __name__,
        "imported_func_module": imported_context["module_name"],
        "greeting_result": format_greeting("Studio Learner"),
    }


if __name__ == "__main__":
    result = analyze_imported_module()
    print("--- Import vs Execution Analysis ---")
    print(f"Current File __name__:     {result['current_file_module']}")
    print(f"Imported Function __name__:{result['imported_func_module']}")
    print(f"Greeting Result:          {result['greeting_result']}")
