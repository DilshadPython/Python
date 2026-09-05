"""
Python Exception Handling: `try-except-else-finally` Control Flow

This module demonstrates the complete 4-part exception clause architecture in Python:
- `try`: Code block monitored for exceptions.
- `except`: Code block executed if a matching exception occurs.
- `else`: Code block executed ONLY if NO exception was raised in the `try` block.
- `finally`: Code block ALWAYS executed regardless of whether exceptions occurred or were caught.
"""
from typing import List, Tuple


def execute_transaction(amount: float, balance: float) -> Tuple[bool, float, List[str]]:
    """
    Executes a financial transaction illustrating the try-except-else-finally workflow.

    Args:
        amount (float): Transaction amount.
        balance (float): Account balance.

    Returns:
        Tuple[bool, float, List[str]]: (Success flag, updated balance, execution log lines).
    """
    logs: List[str] = []
    success = False

    logs.append("Step 1: Entering `try` block.")
    try:
        if amount <= 0:
            raise ValueError("Transaction amount must be strictly positive.")
        if amount > balance:
            raise ValueError("Insufficient funds for transaction.")
        balance -= amount
        success = True
    except ValueError as err:
        logs.append(f"Step 2: Trapped `ValueError` in `except` block: {err}")
    else:
        logs.append(f"Step 2: Executing `else` block (No exceptions). Remaining Balance: ${balance:.2f}")
    finally:
        logs.append("Step 3: Executing `finally` block (Cleanup & Audit logging finalized).")

    return success, balance, logs


def main() -> None:
    """Demonstrates complete try-except-else-finally workflow."""
    print("=" * 60)
    print("3. `try-except-else-finally` Control Flow Demonstration")
    print("=" * 60)

    # 1. Successful Transaction (Triggers try -> else -> finally)
    print("\n--- Scenario A: Successful Transaction ---")
    ok, bal, log_list = execute_transaction(50.0, 200.0)
    print(f"Outcome: Success={ok}, Balance=${bal}")
    for entry in log_list:
        print(f"  {entry}")

    # 2. Failed Transaction (Triggers try -> except -> finally)
    print("\n--- Scenario B: Insufficient Funds Transaction ---")
    ok_b, bal_b, log_list_b = execute_transaction(300.0, 200.0)
    print(f"Outcome: Success={ok_b}, Balance=${bal_b}")
    for entry in log_list_b:
        print(f"  {entry}")


if __name__ == "__main__":
    main()
