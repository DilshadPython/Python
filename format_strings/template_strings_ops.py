"""string.Template Safe String Formatting Module.

Provides functions demonstrating `string.Template` for secure, user-facing template string
substitution (`substitute` and `safe_substitute`) preventing code execution vulnerabilities.
"""

from string import Template
from typing import Any, Dict


def substitute_template(template_pattern: str, mapping: Dict[str, Any]) -> str:
    """Substitute placeholders using `string.Template.substitute`.

    Args:
        template_pattern: String template containing `$var` or `${var}` placeholders.
        mapping: Dictionary containing replacement key-value pairs.

    Returns:
        Substituted string result.

    Raises:
        KeyError: If a placeholder variable is missing in mapping.
    """
    tmpl = Template(template_pattern)
    return tmpl.substitute(mapping)


def safe_substitute_template(template_pattern: str, mapping: Dict[str, Any]) -> str:
    """Substitute placeholders using `string.Template.safe_substitute` without raising errors.

    Args:
        template_pattern: Template pattern string.
        mapping: Partial key-value pair mapping dictionary.

    Returns:
        Substituted string where missing placeholders remain intact.
    """
    tmpl = Template(template_pattern)
    return tmpl.safe_substitute(mapping)


class CustomTemplate(Template):
    """Custom template class using `%` as delimiter instead of `$`."""

    delimiter = "%"


def custom_delimiter_template(template_pattern: str, mapping: Dict[str, Any]) -> str:
    """Substitute placeholders using a custom delimiter template.

    Args:
        template_pattern: Pattern string using `%var` syntax.
        mapping: Key-value mapping.

    Returns:
        Substituted string result.
    """
    tmpl = CustomTemplate(template_pattern)
    return tmpl.substitute(mapping)


def main() -> None:
    """Demonstrate string.Template operations."""
    print("--- Template String Operations ---")

    template_str = "Hello $name! Your account balance is $balance USD."
    user_data = {"name": "Dilshad", "balance": 1500.50}

    # 1. Standard substitution
    result = substitute_template(template_str, user_data)
    print(f"[substitute] {result}")

    # 2. Safe substitution with missing key
    partial_data = {"name": "Dilshad"}
    safe_result = safe_substitute_template(template_str, partial_data)
    print(f"\n[safe_substitute] {safe_result}")

    # 3. Custom delimiter (%)
    custom_str = "Welcome %user to %app!"
    custom_result = custom_delimiter_template(
        custom_str, {"user": "Monika", "app": "Python DevSuite"}
    )
    print(f"\n[custom_delimiter] {custom_result}")


if __name__ == "__main__":
    main()
