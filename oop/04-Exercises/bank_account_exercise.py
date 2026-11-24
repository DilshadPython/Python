"""
Object-Oriented Programming Exercises: Bank Account & Savings Account Hierarchy.

This module provides practical practice problems combining fundamentals (inheritance, encapsulation)
and advanced concepts (properties, defensive validation).
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Optional


class BankAccount:
    """Base class representing a standard bank account."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        """Initialize bank account with holder name and balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder: str = account_holder
        self._balance: float = float(initial_balance)

    @property
    def balance(self) -> float:
        """Getter property exposing current account balance."""
        return self._balance

    def deposit(self, amount: float) -> float:
        """Deposit funds into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw funds from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance


class SavingsAccount(BankAccount):
    """Savings account extending BankAccount with interest rate calculations."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.03) -> None:
        """Initialize savings account with interest rate."""
        super().__init__(account_holder, initial_balance)
        self.interest_rate: float = interest_rate

    def apply_interest(self) -> float:
        """Calculate and deposit interest based on interest rate."""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return self._balance
