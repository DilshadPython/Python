# =========================================================================
# PYTHON METHODS BASICS & ADVANCED OBJECT METHOD PATTERNS
# Sourced & Standardized from DilshadPython/Python/Methods
# =========================================================================
import inspect
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class BankAccount:
    """Demonstrates instance method state encapsulation and defensive checks."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        if not isinstance(account_holder, str):
            raise TypeError("account_holder must be a valid string")
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("initial_balance must be a numeric integer or float")
        if initial_balance < 0:
            raise ValueError("initial_balance cannot be negative")

        self.account_holder: str = account_holder
        self._balance: float = float(initial_balance)
        self.transaction_history: List[str] = [f"Account opened with ${self._balance:.2f}"]

    def deposit(self, amount: float) -> float:
        """Instance method: Modifies instance state by adding funds."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a numeric integer or float")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")

        self._balance += float(amount)
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Instance method: Modifies instance state by withdrawing funds."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a numeric integer or float")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: Balance is ${self._balance:.2f}")

        self._balance -= float(amount)
        self.transaction_history.append(f"Withdrew ${amount:.2f}")
        return self._balance

    def get_statement(self) -> Dict[str, Any]:
        """Instance method: Returns a structured summary of the account state."""
        return {
            "account_holder": self.account_holder,
            "current_balance": self._balance,
            "total_transactions": len(self.transaction_history),
            "recent_history": list(self.transaction_history),
        }


class UserProfile:
    """Demonstrates class methods (@classmethod) and static methods (@staticmethod)."""

    total_users_created: int = 0
    active_roles: List[str] = ["admin", "developer", "guest"]

    def __init__(self, username: str, role: str = "developer") -> None:
        if not isinstance(username, str):
            raise TypeError("username must be a valid string")
        if not isinstance(role, str):
            raise TypeError("role must be a valid string")

        self.username: str = username.strip()
        self.role: str = role.lower()
        UserProfile.total_users_created += 1

    @classmethod
    def from_csv_string(cls, csv_line: str) -> "UserProfile":
        """Class Method: Alternative constructor factory instantiating from CSV text."""
        if not isinstance(csv_line, str):
            raise TypeError("csv_line must be a string")

        parts = [p.strip() for p in csv_line.split(",")]
        if len(parts) < 1 or not parts[0]:
            raise ValueError("Invalid CSV format for user creation")

        username = parts[0]
        role = parts[1] if len(parts) > 1 else "developer"
        return cls(username=username, role=role)

    @classmethod
    def get_system_stats(cls) -> Dict[str, Any]:
        """Class Method: Accesses and reports class-level state."""
        return {
            "total_users": cls.total_users_created,
            "supported_roles": list(cls.active_roles),
            "class_name": cls.__name__,
        }

    @staticmethod
    def validate_username(username: str) -> bool:
        """Static Method: Utility function with no bound 'self' or 'cls' state."""
        if not isinstance(username, str):
            return False
        cleaned = username.strip()
        # Allow alphanumeric characters and underscores
        return len(cleaned) >= 3 and cleaned.replace("_", "").isalnum()


class StudentGrade:
    """Demonstrates property getter, setter, and deleter methods (@property)."""

    def __init__(self, student_name: str, score: float = 0.0) -> None:
        self.student_name: str = student_name
        self._score: float = 0.0
        self.score = score  # Triggers property setter validation

    @property
    def score(self) -> float:
        """Property Getter: Controlled access to private attribute."""
        return self._score

    @score.setter
    def score(self, value: float) -> None:
        """Property Setter: Validates data type and range bounds."""
        if not isinstance(value, (int, float)):
            raise TypeError("Score must be a numeric float or integer")
        if not (0.0 <= value <= 100.0):
            raise ValueError("Score must be between 0.0 and 100.0")
        self._score = float(value)

    @score.deleter
    def score(self) -> None:
        """Property Deleter: Safely resets or deletes attribute state."""
        self._score = 0.0

    @property
    def letter_grade(self) -> str:
        """Calculated Property: Read-only derived attribute."""
        if self._score >= 90.0:
            return "A"
        elif self._score >= 80.0:
            return "B"
        elif self._score >= 70.0:
            return "C"
        elif self._score >= 60.0:
            return "D"
        return "F"


class Vector2D:
    """Demonstrates special dunder methods for object modeling and operator overloading."""

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Vector coordinates x and y must be numeric")
        self.x: float = float(x)
        self.y: float = float(y)

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other: Any) -> "Vector2D":
        if not isinstance(other, Vector2D):
            raise TypeError("Can only add Vector2D to another Vector2D")
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector2D index out of range (0 or 1 valid)")

    def __call__(self, scalar: float = 1.0) -> float:
        """Makes instance callable like a function (returns magnitude multiplied by scalar)."""
        magnitude = (self.x ** 2 + self.y ** 2) ** 0.5
        return magnitude * scalar


class NonNegativeDescriptor:
    """Demonstrates CPython descriptor protocol (__get__, __set__, __delete__)."""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0.0)

    def __set__(self, instance: Any, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Attribute '{self.name}' must be numeric")
        if value < 0:
            raise ValueError(f"Attribute '{self.name}' cannot be negative")
        instance.__dict__[self.name] = float(value)


class ProductInventory:
    quantity = NonNegativeDescriptor("quantity")
    price = NonNegativeDescriptor("price")

    def __init__(self, product_name: str, quantity: float, price: float) -> None:
        self.product_name: str = product_name
        self.quantity = quantity
        self.price = price


def demonstrate_instance_methods(account_name: str, initial_balance: float) -> Dict[str, Any]:
    """Executes instance methods on BankAccount."""
    account = BankAccount(account_name, initial_balance)
    balance_after_deposit = account.deposit(150.0)
    balance_after_withdraw = account.withdraw(50.0)
    statement = account.get_statement()

    return {
        "account_holder": account_name,
        "balance_after_deposit": balance_after_deposit,
        "balance_after_withdraw": balance_after_withdraw,
        "statement": statement,
    }


def demonstrate_class_and_static_methods(csv_line: str) -> Dict[str, Any]:
    """Executes @classmethod and @staticmethod patterns on UserProfile."""
    user = UserProfile.from_csv_string(csv_line)
    is_valid_user = UserProfile.validate_username(user.username)
    system_stats = UserProfile.get_system_stats()

    return {
        "created_username": user.username,
        "created_role": user.role,
        "is_username_valid": is_valid_user,
        "system_stats": system_stats,
    }


def demonstrate_property_methods(student_name: str, initial_score: float) -> Dict[str, Any]:
    """Executes @property getter, setter, and deleter on StudentGrade."""
    student = StudentGrade(student_name, initial_score)
    initial_letter = student.letter_grade

    # Update score using setter
    student.score = 92.5
    updated_letter = student.letter_grade

    # Delete score (resets to 0.0)
    del student.score
    reset_score = student.score
    reset_letter = student.letter_grade

    return {
        "student_name": student_name,
        "initial_score": initial_score,
        "initial_letter": initial_letter,
        "updated_score": 92.5,
        "updated_letter": updated_letter,
        "reset_score": reset_score,
        "reset_letter": reset_letter,
    }


def demonstrate_special_dunder_methods(x: float, y: float) -> Dict[str, Any]:
    """Executes custom dunder methods on Vector2D."""
    v1 = Vector2D(x, y)
    v2 = Vector2D(3.0, 4.0)
    v3 = v1 + v2

    return {
        "v1_str": str(v1),
        "v1_repr": repr(v1),
        "v3_added_str": str(v3),
        "vectors_equal": v1 == Vector2D(x, y),
        "v1_len": len(v1),
        "v1_x_component": v1[0],
        "v1_y_component": v1[1],
        "v1_callable_scaled": v1(2.0),
    }


def demonstrate_descriptor_protocol(product_name: str, quantity: float, price: float) -> Dict[str, Any]:
    """Executes descriptor protocol validation on ProductInventory."""
    item = ProductInventory(product_name, quantity, price)
    initial_total = item.quantity * item.price

    item.quantity = 15.0
    updated_total = item.quantity * item.price

    return {
        "product_name": product_name,
        "initial_quantity": quantity,
        "initial_price": price,
        "initial_total": initial_total,
        "updated_quantity": 15.0,
        "updated_total": updated_total,
    }


def inspect_object_methods(target_object: Any) -> Dict[str, Any]:
    """Inspects object methods using built-in functions dir(), getattr(), and inspect module."""
    if target_object is None:
        raise TypeError("target_object cannot be None")

    all_attrs = dir(target_object)
    public_attrs = [attr for attr in all_attrs if not attr.startswith("_")]
    methods = [
        attr for attr in public_attrs if callable(getattr(target_object, attr, None))
    ]

    return {
        "object_type": type(target_object).__name__,
        "total_attributes": len(all_attrs),
        "public_methods_count": len(methods),
        "sample_methods": methods[:6],
        "is_bank_account": isinstance(target_object, BankAccount),
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
    }


if __name__ == "__main__":
    print("=== Python Methods & Object Architecture Demo ===")
    print("Instance Methods:", demonstrate_instance_methods("alex_dev", 100.0))
    print("Class & Static Methods:", demonstrate_class_and_static_methods("john_doe, admin"))
    print("Property Methods:", demonstrate_property_methods("Alex", 78.0))
    print("Dunder Methods:", demonstrate_special_dunder_methods(3.0, 4.0))
    print("Descriptor Protocol:", demonstrate_descriptor_protocol("Laptop", 5.0, 999.99))
    print("Method Inspection:", inspect_object_methods(BankAccount("test", 50.0)))
