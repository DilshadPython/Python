"""
cloud_app/tutorials/code_quality_basics.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive, PEP 8 compliant tutorial module demonstrating Python Code Quality,
SOLID Principles, Clean Code, Design Patterns, Error Handling, and Developer Tooling.

This module provides a 5-tier architecture:
1. PEP 8 & Clean Code Basics (Naming, Formatting, Small Functions, Documentation).
2. DRY & Separation of Concerns (Domain Logic, Data Access, Presentation Layers).
3. SOLID Design Principles (SRP, OCP, LSP, ISP, DIP).
4. Robust Error Handling, Type Hints & Unit Testing Patterns.
5. Production Tooling Configuration Blueprints (Ruff, Black, Pytest, Mypy, Pre-commit).
"""

import abc
import math
import re
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

# ── Custom Exception Hierarchy ────────────────────────────────────────────────


class CodeQualityError(Exception):
    """Base exception class for domain errors in the code quality module."""

    pass


class ValidationError(CodeQualityError):
    """Raised when input validation fails defensive constraints."""

    pass


class PaymentProcessingError(CodeQualityError):
    """Raised when a payment transaction fails execution."""

    pass


class ResourceNotFoundError(CodeQualityError):
    """Raised when requested entity is missing from data storage."""

    pass


# ── 1. PEP 8 & Clean Code Demonstrations ────────────────────────────────────────


def calculate_discounted_price(
    original_price: float,
    discount_rate: float,
    tax_rate: float = 0.05,
) -> float:
    """Calculate final price after applying discount and sales tax.

    Args:
        original_price: Base price of the product (must be >= 0).
        discount_rate: Fractional discount (0.0 to 1.0).
        tax_rate: Fractional sales tax rate (default 0.05 / 5%).

    Returns:
        Final calculated price rounded to 2 decimal places.

    Raises:
        ValidationError: If price or rates are out of valid bounds.
    """
    if original_price < 0:
        raise ValidationError("Original price cannot be negative.")
    if not (0.0 <= discount_rate <= 1.0):
        raise ValidationError("Discount rate must be between 0.0 and 1.0.")
    if not (0.0 <= tax_rate <= 1.0):
        raise ValidationError("Tax rate must be between 0.0 and 1.0.")

    discounted_amount = original_price * (1.0 - discount_rate)
    final_price = discounted_amount * (1.0 + tax_rate)
    return round(final_price, 2)


def is_valid_username(username: str) -> bool:
    """Check whether a username meets alphanumeric/underscore and length constraints.

    Single responsibility function: returns a simple boolean validation check.
    """
    if not username or not isinstance(username, str):
        return False
    clean_username = username.strip()
    return bool(re.match(r"^[a-zA-Z0-9_]{3,20}$", clean_username))


# ── 2. DRY & Separation of Concerns (SoC) ───────────────────────────────────


class User:
    """Domain Entity representing a user in the application."""

    def __init__(self, user_id: int, username: str, email: str) -> None:
        self.user_id: int = user_id
        self.username: str = username
        self.email: str = email

    def to_dict(self) -> Dict[str, Any]:
        """Convert domain entity to dictionary representation."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }


# Data Access Layer (Repository Abstraction)
class UserRepositoryProtocol(Protocol):
    """Dependency Inversion Protocol defining User Repository interface."""

    def get_by_id(self, user_id: int) -> Optional[User]: ...

    def save(self, user: User) -> None: ...


class InMemoryUserRepository:
    """In-memory concrete implementation of UserRepositoryProtocol."""

    def __init__(self) -> None:
        self._storage: Dict[int, User] = {}

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._storage.get(user_id)

    def save(self, user: User) -> None:
        self._storage[user.user_id] = user


# Business Service Layer (Single Responsibility)
class UserService:
    """High-level service orchestrating user business logic."""

    def __init__(self, repository: UserRepositoryProtocol) -> None:
        self._repository: UserRepositoryProtocol = repository

    def register_user(self, user_id: int, username: str, email: str) -> User:
        if not is_valid_username(username):
            raise ValidationError(f"Invalid username: '{username}'")
        if "@" not in email or "." not in email:
            raise ValidationError(f"Invalid email address: '{email}'")

        existing = self._repository.get_by_id(user_id)
        if existing:
            raise ValidationError(f"User ID {user_id} already registered.")

        user = User(user_id=user_id, username=username, email=email)
        self._repository.save(user)
        return user


# ── 3. SOLID Principles Implementation ───────────────────────────────────────


# S - Single Responsibility Principle (SRP)
class EmailValidator:
    """SRP: Sole responsibility is validating email syntax."""

    @staticmethod
    def validate(email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))


class PasswordHasher:
    """SRP: Sole responsibility is secure password hash verification."""

    @staticmethod
    def hash_password(plain_password: str) -> str:
        # Simulated hashing for demonstration
        return f"pbkdf2_sha256${len(plain_password)}${hash(plain_password)}"


# O - Open/Closed Principle (OCP) & L - Liskov Substitution (LSP)
class PaymentStrategy(abc.ABC):
    """Abstract Base Class defining flexible Payment Strategy interface."""

    @abc.abstractmethod
    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Process transaction amount and return status receipt."""
        pass


class CreditCardPayment(PaymentStrategy):
    """Credit Card payment processor strategy."""

    def __init__(self, card_number: str) -> None:
        self.card_number: str = card_number

    def process_payment(self, amount: float) -> Dict[str, Any]:
        if amount <= 0:
            raise ValidationError("Payment amount must be positive.")
        masked = (
            f"****-****-****-{self.card_number[-4:]}"
            if len(self.card_number) >= 4
            else "****"
        )
        return {
            "status": "SUCCESS",
            "method": "CreditCard",
            "amount": amount,
            "account": masked,
        }


class PayPalPayment(PaymentStrategy):
    """PayPal digital wallet payment strategy."""

    def __init__(self, paypal_email: str) -> None:
        self.paypal_email: str = paypal_email

    def process_payment(self, amount: float) -> Dict[str, Any]:
        if amount <= 0:
            raise ValidationError("Payment amount must be positive.")
        return {
            "status": "SUCCESS",
            "method": "PayPal",
            "amount": amount,
            "account": self.paypal_email,
        }


# I - Interface Segregation Principle (ISP)
class Workable(Protocol):
    def work(self) -> str: ...


class Feedable(Protocol):
    def eat(self) -> str: ...


class HumanWorker(Workable, Feedable):
    def work(self) -> str:
        return "Human coding backend algorithms."

    def eat(self) -> str:
        return "Human taking lunch break."


class RobotWorker(Workable):
    def work(self) -> str:
        return "Robot compiling binary instructions continuously."


# D - Dependency Inversion Principle (DIP)
class OrderProcessor:
    """High-level module depending strictly on PaymentStrategy abstraction."""

    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy: PaymentStrategy = payment_strategy

    def checkout(self, amount: float) -> Dict[str, Any]:
        return self.payment_strategy.process_payment(amount)


# ── 4. Developer Tools Blueprint Configurations ─────────────────────────────


def get_tooling_blueprints() -> Dict[str, Any]:
    """Return dictionary of industry-standard tool config blueprints."""
    return {
        "ruff": {
            "config_filename": "pyproject.toml or ruff.toml",
            "command": "ruff check . --fix",
            "snippet": '[tool.ruff]\nselect = ["E", "F", "B", "I", "N", "UP"]\nline-length = 88\ntarget-version = "py312"',
            "description": "Ultra-fast Python linter replacing flake8, isort, pyflakes, pydocstyle.",
        },
        "black": {
            "config_filename": "pyproject.toml",
            "command": "black . --check",
            "snippet": "[tool.black]\nline-length = 88\ntarget-version = ['py312']\ninclude = '\\.pyi?$' ",
            "description": "Uncompromising Python code formatter for uniform team code style.",
        },
        "pytest": {
            "config_filename": "pytest.ini",
            "command": "pytest --cov=cloud_app --cov-report=term-missing",
            "snippet": '[pytest]\ntestpaths = ["tests"]\npython_files = "test_*.py"\naddopts = "-vv --durations=5"',
            "description": "Industry-standard testing framework supporting fixtures & parametrization.",
        },
        "mypy": {
            "config_filename": "mypy.ini or pyproject.toml",
            "command": "mypy cloud_app --strict",
            "snippet": '[mypy]\npython_version = "3.12"\ndisallow_untyped_defs = true\nwarn_return_any = true\nstrict = true',
            "description": "Static type checker verifying PEP 484 type annotations.",
        },
        "pre_commit": {
            "config_filename": ".pre-commit-config.yaml",
            "command": "pre-commit run --all-files",
            "snippet": "repos:\n  - repo: https://github.com/astral-sh/ruff-pre-commit\n    rev: v0.3.0\n    hooks:\n      - id: ruff\n      - id: ruff-format",
            "description": "Multi-language Git hook framework running checks automatically before commit.",
        },
    }


# ── 5. Studio Sub-Pane Demonstrations ─────────────────────────────────────────


def demonstrate_pep8_and_clean_code() -> Dict[str, Any]:
    """Demonstrate clean pricing calculation and username validation."""
    price_1 = calculate_discounted_price(100.0, 0.20, tax_rate=0.08)
    price_2 = calculate_discounted_price(250.0, 0.10, tax_rate=0.05)

    u1_valid = is_valid_username("python_dev99")
    u2_valid = is_valid_username("a!")  # Invalid length & special char

    return {
        "price_100_20pct_off_8pct_tax": price_1,
        "price_250_10pct_off_5pct_tax": price_2,
        "username_python_dev99_valid": u1_valid,
        "username_a_bang_valid": u2_valid,
    }


def demonstrate_solid_principles() -> Dict[str, Any]:
    """Demonstrate OCP/DIP using Credit Card and PayPal payment strategies."""
    cc_strategy = CreditCardPayment("4111222233334444")
    paypal_strategy = PayPalPayment("developer@teachcloud.dev")

    processor_cc = OrderProcessor(cc_strategy)
    processor_paypal = OrderProcessor(paypal_strategy)

    res_cc = processor_cc.checkout(150.75)
    res_paypal = processor_paypal.checkout(89.99)

    robot = RobotWorker()
    human = HumanWorker()

    return {
        "credit_card_checkout": res_cc,
        "paypal_checkout": res_paypal,
        "robot_work": robot.work(),
        "human_work": human.work(),
        "human_eat": human.eat(),
    }


def demonstrate_dry_and_soc() -> Dict[str, Any]:
    """Demonstrate Layered Architecture (Repository -> Service -> Entity)."""
    repo = InMemoryUserRepository()
    service = UserService(repo)

    user1 = service.register_user(101, "ada_lovelace", "ada@university.edu")
    user2 = service.register_user(102, "guido_van", "guido@python.org")

    fetched = repo.get_by_id(101)

    return {
        "user1_dict": user1.to_dict(),
        "user2_dict": user2.to_dict(),
        "fetched_equal_user1": fetched is not None and fetched.email == user1.email,
        "total_users_saved": len(repo._storage),
    }


def demonstrate_error_handling_and_testing() -> Dict[str, Any]:
    """Demonstrate custom exception catching and defensive validation."""
    caught_validation_error = False
    error_message = ""

    try:
        calculate_discounted_price(-50.0, 0.10)
    except ValidationError as err:
        caught_validation_error = True
        error_message = str(err)

    return {
        "caught_validation_error": caught_validation_error,
        "error_message": error_message,
        "email_validation_valid": EmailValidator.validate("test@example.com"),
        "email_validation_invalid": EmailValidator.validate("invalid-email-format"),
    }


def demonstrate_refactoring_before_after() -> Dict[str, Any]:
    """Demonstrate code refactoring converting legacy unmaintainable code into clean code."""
    dirty_legacy_code = """
# ❌ Dirty Legacy Code (Poor naming, no type hints, duplicated logic, no error handling)
def p(d):
    t = 0
    for i in d:
        if i['type'] == 'book':
            t += i['price'] * 0.9  # hardcoded 10% discount
        elif i['type'] == 'tech':
            t += i['price'] * 0.8  # hardcoded 20% discount
    return t
"""

    clean_refactored_code = '''
# ✅ Clean Refactored Code (Meaningful names, type hints, SRP, DRY, documentation)
from typing import List, Dict

DISCOUNT_RATES: Dict[str, float] = {
    "book": 0.10,
    "tech": 0.20,
}

def calculate_item_price(price: float, item_type: str) -> float:
    """Calculate discounted item price based on item type catalog."""
    discount = DISCOUNT_RATES.get(item_type, 0.0)
    return price * (1.0 - discount)

def calculate_total_cart(cart_items: List[Dict[str, float]]) -> float:
    """Calculate total checkout price for list of cart items."""
    return sum(
        calculate_item_price(item["price"], item["type"])
        for item in cart_items
    )
'''

    # Execute refactored logic for verification
    sample_cart: List[Dict[str, Union[str, float]]] = [
        {"type": "book", "price": 20.0},
        {"type": "tech", "price": 100.0},
    ]
    refactored_total = sum(
        float(item["price"]) * (1.0 - (0.10 if item["type"] == "book" else 0.20))
        for item in sample_cart
    )

    return {
        "dirty_legacy_snippet": dirty_legacy_code.strip(),
        "clean_refactored_snippet": clean_refactored_code.strip(),
        "sample_cart_total": refactored_total,
    }


def demonstrate_tooling_configurations() -> Dict[str, Any]:
    """Return tools breakdown and config snippets."""
    return get_tooling_blueprints()


if __name__ == "__main__":
    print("=== Python Code Quality Tutorial Module ===")
    print("PEP 8 & Clean Code:", demonstrate_pep8_and_clean_code())
    print("SOLID Principles:", demonstrate_solid_principles())
    print("DRY & Separation of Concerns:", demonstrate_dry_and_soc())
    print("Error Handling & Validation:", demonstrate_error_handling_and_testing())
    print("Refactoring Before/After:", demonstrate_refactoring_before_after())
    print("Tooling Blueprints:", list(demonstrate_tooling_configurations().keys()))
