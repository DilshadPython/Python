"""
Python Exception Handling: Stack Propagation & Unwinding

This module demonstrates call stack unwinding and exception propagation across
multi-tier application architectures (`main` -> `service` -> `repository` -> `low_level_op`).

Key Concepts:
- Uncaught exceptions bubble up function frames until a matching `except` block is found.
- If no frame catches the exception, Python terminates execution and outputs the stack trace.
"""
from typing import List


class CalculationService:
    """Simulates a multi-tier service layer triggering low-level arithmetic errors."""

    @staticmethod
    def divide_numbers(a: float, b: float) -> float:
        """Low-level arithmetic function raising ZeroDivisionError if b == 0."""
        print("    [Level 3: Low-level divide_numbers()] Executing division.")
        return a / b

    def process_data(self, numbers: List[float]) -> float:
        """Mid-tier process function calling divide_numbers."""
        print("  [Level 2: Mid-tier process_data()] Calling divide_numbers().")
        # Attempts to divide the first number by the second
        return self.divide_numbers(numbers[0], numbers[1])


def execute_pipeline(data: List[float]) -> None:
    """Top-level pipeline coordinator invoking CalculationService."""
    print("[Level 1: Top-level execute_pipeline()] Initializing service.")
    service = CalculationService()
    result = service.process_data(data)
    print(f"[Level 1: Top-level execute_pipeline()] Calculation successful: {result}")


def main() -> None:
    """Demonstrates exception propagation across nested call frames."""
    print("=" * 60)
    print("6. Call Stack Exception Propagation & Unwinding")
    print("=" * 60)

    # 1. Normal execution flow
    print("\n--- Flow A: Valid Inputs ---")
    try:
        execute_pipeline([100.0, 5.0])
    except ZeroDivisionError:
        print("Trapped ZeroDivisionError in main().")

    # 2. Propagation flow: Error originates at Level 3, bubbles through Level 2 and Level 1, caught in main()
    print("\n--- Flow B: Zero Division Triggering Stack Unwinding ---")
    try:
        execute_pipeline([100.0, 0.0])
    except ZeroDivisionError as err:
        print(f"\nSuccessfully caught propagated ZeroDivisionError in main(): {err}")
        print("Notice how intermediate function calls (Level 3, Level 2, Level 1) were unwound.")


if __name__ == "__main__":
    main()
