"""Direct Evaluation of Literal Booleans (True / False).

Demonstrates direct boolean control flow with 'if True:' and 'if False:'.

Import Notes:
    - 'from typing import Union': Standard library typing import for annotations.
"""

from typing import Union


def evaluate_literal_condition(flag: bool) -> str:
    """Evaluate literal boolean conditions."""
    if flag:
        return "Condition evaluated to True: Executing 'if' block."
    else:
        return "Condition evaluated to False: Executing 'else' block."


def demo_if_what() -> None:
    """Demonstrate literal boolean evaluation."""
    print(evaluate_literal_condition(True))
    print(evaluate_literal_condition(False))


if __name__ == "__main__":
    demo_if_what()
