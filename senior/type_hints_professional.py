"""
Track 05: Type Hints Like a Professional

Description: Master Senior Python Track 05: Professional Type Systems. Structural subtyping with typing.Protocol, TypeVar, Self, @overload, TypedDict, Literal, and static exhaustiveness checking with assert_never.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/type_hints_professional
"""

# --- Code Snippet 1 ---
from typing import Protocol, runtime_checkable

@runtime_checkable
class PaymentGateway(Protocol):
    def charge(self, amount: int) -> bool: ...

class StripeGateway:
    """Satisfies PaymentGateway contract implicitly."""
    def charge(self, amount: int) -> bool:
        print(f"Stripe charged ${amount}")
        return True

def process_payment(gateway: PaymentGateway, amount: int) -> bool:
    return gateway.charge(amount)

# --- Code Snippet 2 ---
from typing import Self, overload, TypedDict, Literal

class UserPayload(TypedDict):
    user_id: str
    role: Literal["admin", "developer", "guest"]

class QueryBuilder:
    def filter_by(self, field: str, value: str) -> Self:
        """Returns instance type for fluent method chaining."""
        return self

@overload
def parse_id(val: int) -> int: ...
@overload
def parse_id(val: str) -> str: ...

def parse_id(val: int | str) -> int | str:
    return val

# --- Code Snippet 3 ---
from typing import assert_never, Literal
from dataclasses import dataclass

@dataclass
class Card:
    method: Literal["card"]
    pan: str

@dataclass
class Crypto:
    method: Literal["crypto"]
    wallet: str

Payment = Card | Crypto

def route_payment(p: Payment) -> str:
    match p:
        case Card(pan=pan):
            return f"Processing Card: {pan}"
        case Crypto(wallet=w):
            return f"Processing Crypto Wallet: {w}"
        case _ as unreachable:
            assert_never(unreachable)

