"""
Python Easter Egg: `from __future__ import barry_as_FLUFL` (PEP 401)

PEP 401 ("BFLFL - BDFL Retirement") introduced the `barry_as_FLUFL` future import.
FLUFL stands for "Friendly Language Uncle For Life" (Barry Warsaw).

When activated:
- The standard inequality operator `!=` raises a SyntaxError.
- Re-enables the legacy Python 2 diamond inequality operator `<>`.

Example:
    >>> try:
    ...     exec("from __future__ import barry_as_FLUFL\\n1 != 2")
    ... except SyntaxError as exc:
    ...     print(exc)
    with Barry as BDFL, use '<>' instead of '!='
"""


def demonstrate_flufl_ne_error() -> str:
    """
    Executes code with `barry_as_FLUFL` enabled and attempts to use `!=`.

    Returns:
        str: Syntax error message enforcing `<>` over `!=`.
    """
    code = "from __future__ import barry_as_FLUFL\nresult = (1 != 2)"
    try:
        exec(code)
    except SyntaxError as err:
        return str(err)
    return "No error raised"


def demonstrate_flufl_diamond_op() -> bool:
    """
    Executes code with `barry_as_FLUFL` enabled and uses the `<>` operator.

    Returns:
        bool: Result of evaluating `1 <> 2` under FLUFL syntax rules.
    """
    code = "from __future__ import barry_as_FLUFL\nresult = (1 <> 2)"
    namespace: dict[str, object] = {}
    exec(code, namespace)
    return bool(namespace.get("result", False))


def main() -> None:
    """Executes the FLUFL Easter egg demonstration."""
    print("=" * 60)
    print("👑 Python Easter Egg: Barry as FLUFL (`from __future__ import barry_as_FLUFL`)")
    print("=" * 60)

    err_msg = demonstrate_flufl_ne_error()
    print(f"\n1. Result of using `!=` under FLUFL: SyntaxError('{err_msg}')")

    diamond_res = demonstrate_flufl_diamond_op()
    print(f"2. Result of evaluating `1 <> 2` under FLUFL: {diamond_res}")

    print("\nExplanation:")
    print("  PEP 401 declared Barry Warsaw as 'Friendly Language Uncle For Life'.")
    print("  This joke feature replaces `!=` with `<>` as a homage to early Python syntax.")


if __name__ == "__main__":
    main()
