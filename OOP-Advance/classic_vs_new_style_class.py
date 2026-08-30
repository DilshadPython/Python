"""Classic vs New-Style Classes Demonstration Module.

This module details the historical evolution of Python class object models:
1. Python 2 Classic Classes: Uninherited user classes (type `<type 'instance'>`).
2. Python 2/3 New-Style Classes: Inheriting explicitly from `object` (or implicit in Python 3).
3. Python 3 Unified Class Model: All classes implicitly inherit from `object` and share a unified type hierarchy.
"""


class ClassicStyle:
    """Class defined without explicit object inheritance (Classic style in Python 2, New style in Python 3)."""
    pass


class ExplicitNewStyle(object):
    """Class defined with explicit object inheritance (New style in Python 2 & Python 3)."""
    pass


if __name__ == "__main__":
    print("=== Classic vs New-Style Classes Demonstration ===")

    classic_inst = ClassicStyle()
    new_style_inst = ExplicitNewStyle()

    print("ClassicStyle instance type:", type(classic_inst))
    print("ExplicitNewStyle instance type:", type(new_style_inst))
    print("==========================================")

    print("ClassicStyle __class__:", classic_inst.__class__)
    print("ExplicitNewStyle __class__:", new_style_inst.__class__)

    print("\n--- Object Superclass Inheritance Verification ---")
    print("isinstance(classic_inst, object):", isinstance(classic_inst, object))
    print("isinstance(new_style_inst, object):", isinstance(new_style_inst, object))
