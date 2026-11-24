"""
Runtime Introspection and Reflection Matrix Module for Module Attributes.

This module demonstrates:
- Reflection via dir() on current module execution scope.
- Inspecting built-in module attributes: __name__, __file__, __doc__, __package__, __spec__.
- Demonstrating dir(range) attributes (.start, .stop, .step, .count(), .index()).
"""

# Import sys for interpreter details
import sys


def introspect_module_attributes() -> dict[str, object]:
    """Inspect public and dunder attributes of current module scope.

    Returns:
        dict[str, object]: Dictionary containing module introspection details.
    """
    public_and_special_attrs = dir(sys.modules[__name__])

    return {
        "attribute_count": len(public_and_special_attrs),
        "module_name": __name__,
        "has_file_attr": hasattr(sys.modules[__name__], "__file__"),
        "has_doc_attr": hasattr(sys.modules[__name__], "__doc__"),
        "sample_attributes": public_and_special_attrs[:10],
    }


def introspect_range_attributes() -> dict[str, object]:
    """Inspect and demonstrate dir(range) public attributes and methods.

    Returns:
        dict[str, object]: Range reflection metadata.
    """
    r = range(10, 100, 5)
    public_attrs = [a for a in dir(r) if not a.startswith("__")]

    return {
        "public_attribute_list": public_attrs,
        "start": r.start,
        "stop": r.stop,
        "step": r.step,
        "count_of_25": r.count(25),
        "index_of_30": r.index(30),
    }


if __name__ == "__main__":
    mod_info = introspect_module_attributes()
    print("--- Module Introspection dir() ---")
    print(f"Module Name: {mod_info['module_name']}")
    print(f"Attribute Count: {mod_info['attribute_count']}")

    rng_info = introspect_range_attributes()
    print("\n--- Range Introspection dir(range) ---")
    print(f"Public Attributes: {rng_info['public_attribute_list']}")
    print(f"Start: {rng_info['start']}, Stop: {rng_info['stop']}, Step: {rng_info['step']}")
    print(f"r.count(25): {rng_info['count_of_25']}, r.index(30): {rng_info['index_of_30']}")
