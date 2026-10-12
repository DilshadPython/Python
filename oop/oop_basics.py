# =========================================================================
# PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) BASICS & ARCHITECTURE
# Sourced & Standardized from DilshadPython/Python/object_oriented
# =========================================================================
import abc
import json
import sys
from typing import Any, Dict, List, Optional, Tuple, Type, Union


# -------------------------------------------------------------------------
# 0. CLASS DEFINITION BASICS & PROCEDURAL COMPARISON
# -------------------------------------------------------------------------
class User:
    """Represents a user entity encapsulating profile state and instance methods."""

    def __init__(self, first_name: str, last_name: str, payment: float) -> None:
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("first_name and last_name must be strings")
        if not first_name.strip() or not last_name.strip():
            raise ValueError("First and last names cannot be empty")
        if not isinstance(payment, (int, float)) or payment < 0:
            raise ValueError("Payment balance cannot be negative")

        self.first_name: str = first_name.strip()
        self.last_name: str = last_name.strip()
        self.payment: float = float(payment)

    @property
    def email(self) -> str:
        """Dynamically generate email address based on first and last name."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

    def full_name(self) -> str:
        """Return the formatted full name of the user."""
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self, rate: float) -> float:
        """Apply a discount rate multiplier to the user's payment balance."""
        if not isinstance(rate, (int, float)) or rate <= 0 or rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.payment = round(self.payment * rate, 2)
        return self.payment


def procedural_user_representation(first_name: str, last_name: str, payment: float) -> Dict[str, Any]:
    """Legacy procedural dictionary representation of user data."""
    return {
        "first_name": first_name,
        "last_name": last_name,
        "payment": payment,
        "email": f"{first_name.lower()}.{last_name.lower()}@company.com",
    }


def demonstrate_class_definition_basics() -> Dict[str, Any]:
    """Executes User class instantiation and procedural comparison."""
    user = User("Alice", "Smith", 250.00)
    procedural = procedural_user_representation("Alice", "Smith", 250.00)
    discounted_payment = user.apply_discount(0.90)

    return {
        "user_full_name": user.full_name(),
        "user_email": user.email,
        "discounted_payment": discounted_payment,
        "procedural_email": procedural["email"],
        "is_user_instance": isinstance(user, User),
    }


# -------------------------------------------------------------------------
# 1. CLASS AND INSTANCE ATTRIBUTES
# -------------------------------------------------------------------------
class CompanyEmployee:
    """Demonstrates Class vs Instance attributes, __dict__ namespaces, and dynamic deletion."""

    company_name: str = "TechCorp Solutions"
    total_employees: int = 0

    def __init__(self, emp_id: str, name: str, salary: float) -> None:
        if not isinstance(emp_id, str) or not isinstance(name, str):
            raise TypeError("emp_id and name must be strings")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("salary must be a non-negative number")

        self.emp_id: str = emp_id
        self.name: str = name
        self.salary: float = float(salary)
        CompanyEmployee.total_employees += 1

    def get_details(self) -> Dict[str, Any]:
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "salary": self.salary,
            "company": self.company_name,
        }


def demonstrate_class_and_instance_attributes() -> Dict[str, Any]:
    """Executes class vs instance attribute scope and namespace inspection."""
    emp1 = CompanyEmployee("E-101", "Alex Dev", 85000.0)
    emp2 = CompanyEmployee("E-102", "Sarah Smith", 92000.0)

    initial_company = emp1.company_name
    emp2.company_name = "TechCorp Labs"

    emp1.temporary_tag = "Contractor"
    has_tag_before = hasattr(emp1, "temporary_tag")
    delattr(emp1, "temporary_tag")
    has_tag_after = hasattr(emp1, "temporary_tag")

    return {
        "total_employees": CompanyEmployee.total_employees,
        "emp1_company": initial_company,
        "emp2_company_shadow": emp2.company_name,
        "has_tag_before": has_tag_before,
        "has_tag_after": has_tag_after,
        "emp1_namespace_keys": list(emp1.__dict__.keys()),
    }


# -------------------------------------------------------------------------
# 1B. CLASS AND INSTANCE DATA REFLECTION
# -------------------------------------------------------------------------
class DataReflectionModel:
    """Demonstrates Class and Instance Data reflection, dir(), getattr(), and dynamic deletion."""

    data_version: str = "v2.4"
    instance_count: int = 0

    def __init__(self, record_id: str, payload: Dict[str, Any]) -> None:
        if not isinstance(record_id, str):
            raise TypeError("record_id must be a string")
        if not isinstance(payload, dict):
            raise TypeError("payload must be a dictionary")

        self.record_id: str = record_id
        self.payload: Dict[str, Any] = payload
        DataReflectionModel.instance_count += 1

    def inspect_public_attributes(self) -> List[str]:
        """Returns list of public attribute and method names via dir()."""
        return [attr for attr in dir(self) if not attr.startswith("__")]


def demonstrate_class_and_instance_data() -> Dict[str, Any]:
    """Executes Class and Instance Data reflection, instance counting, and dir() inspection."""
    m1 = DataReflectionModel("REC-001", {"status": "ACTIVE", "score": 98.5})
    m2 = DataReflectionModel("REC-002", {"status": "PENDING", "score": 76.0})

    m1.dynamic_note = "Priority Processing"
    note_before = getattr(m1, "dynamic_note")
    delattr(m1, "dynamic_note")
    has_note_after = hasattr(m1, "dynamic_note")

    return {
        "total_instances_created": DataReflectionModel.instance_count,
        "data_version": DataReflectionModel.data_version,
        "public_attrs": m1.inspect_public_attributes(),
        "note_before": note_before,
        "has_note_after": has_note_after,
        "m1_record_id": m1.record_id,
    }


# -------------------------------------------------------------------------
# 2. CONSTRUCTORS AND INITIALIZATION
# -------------------------------------------------------------------------
class Vehicle:
    """Demonstrates constructor (__init__) initialization logic and default values."""

    def __init__(
        self, make: str, model: str, year: int, odometer: float = 0.0
    ) -> None:
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("make and model must be strings")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("year must be a valid integer year (>= 1886)")
        if not isinstance(odometer, (int, float)) or odometer < 0:
            raise ValueError("odometer reading cannot be negative")

        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.odometer: float = float(odometer)

    def drive(self, distance: float) -> float:
        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("distance must be non-negative")
        self.odometer += float(distance)
        return self.odometer


def demonstrate_constructors_and_initialization() -> Dict[str, Any]:
    """Executes vehicle constructor initialization and distance tracking."""
    car = Vehicle("Toyota", "Corolla", 2022, 15000.0)
    initial_reading = car.odometer
    updated_reading = car.drive(250.5)

    return {
        "vehicle_str": f"{car.year} {car.make} {car.model}",
        "initial_odometer": initial_reading,
        "updated_odometer": updated_reading,
    }


# -------------------------------------------------------------------------
# 3. ENCAPSULATION AND MANAGED PROPERTIES
# -------------------------------------------------------------------------
class BankAccountSecure:
    """Demonstrates public, protected (_), and private (__) attributes with name mangling."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner: str = owner
        self._account_type: str = "Savings"
        self.__balance: float = 0.0
        self.balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a numeric float or int")
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = float(amount)

    @balance.deleter
    def balance(self) -> None:
        self.__balance = 0.0

    def get_mangled_attribute_name(self) -> str:
        """Returns the CPython internal mangled name for private attribute."""
        return f"_{self.__class__.__name__}__balance"


def demonstrate_encapsulation_and_properties() -> Dict[str, Any]:
    """Executes property getters/setters and inspects private name mangling."""
    account = BankAccountSecure("John Doe", 500.0)
    initial_balance = account.balance

    account.balance = 1200.50
    updated_balance = account.balance

    mangled_key = account.get_mangled_attribute_name()
    mangled_value = getattr(account, mangled_key)

    del account.balance
    reset_balance = account.balance

    return {
        "owner": account.owner,
        "initial_balance": initial_balance,
        "updated_balance": updated_balance,
        "mangled_key": mangled_key,
        "mangled_value": mangled_value,
        "reset_balance": reset_balance,
    }


# -------------------------------------------------------------------------
# 4. INHERITANCE AND SUPER()
# -------------------------------------------------------------------------
class Animal:
    def __init__(self, species: str, sound: str) -> None:
        self.species: str = species
        self.sound: str = sound

    def make_sound(self) -> str:
        return f"The {self.species} goes '{self.sound}'"


class Mammal(Animal):
    def __init__(self, species: str, sound: str, fur_color: str) -> None:
        super().__init__(species, sound)
        self.fur_color: str = fur_color

    def describe(self) -> str:
        return f"{self.make_sound()} and has {self.fur_color} fur."


class Dog(Mammal):
    def __init__(self, name: str, breed: str, fur_color: str) -> None:
        super().__init__("Canine", "Woof", fur_color)
        self.name: str = name
        self.breed: str = breed

    def make_sound(self) -> str:
        base_sound = super().make_sound()
        return f"{self.name} ({self.breed}) says: {base_sound}"


def demonstrate_inheritance_and_super() -> Dict[str, Any]:
    """Executes single and multi-level inheritance with method overriding."""
    dog = Dog("Buddy", "Golden Retriever", "Golden")
    return {
        "dog_name": dog.name,
        "breed": dog.breed,
        "fur_color": dog.fur_color,
        "sound_output": dog.make_sound(),
        "is_animal_instance": isinstance(dog, Animal),
        "is_mammal_instance": isinstance(dog, Mammal),
    }


# -------------------------------------------------------------------------
# 5. MULTIPLE INHERITANCE AND METHOD RESOLUTION ORDER (MRO)
# -------------------------------------------------------------------------
class Device:
    def turn_on(self) -> str:
        return "Device powering on"


class Camera(Device):
    def turn_on(self) -> str:
        return f"Camera lens opening -> {super().turn_on()}"


class Phone(Device):
    def turn_on(self) -> str:
        return f"Phone screen lighting -> {super().turn_on()}"


class SmartPhone(Camera, Phone):
    """Diamond inheritance resolving order via C3 Linearization MRO."""

    def turn_on(self) -> str:
        return f"SmartPhone Booting: [{super().turn_on()}]"


def demonstrate_multiple_inheritance_and_mro() -> Dict[str, Any]:
    """Executes multiple diamond inheritance and inspects MRO chain."""
    phone = SmartPhone()
    boot_sequence = phone.turn_on()
    mro_class_names = [cls.__name__ for cls in SmartPhone.mro()]

    return {
        "boot_sequence": boot_sequence,
        "mro_chain": mro_class_names,
    }


# -------------------------------------------------------------------------
# 6. POLYMORPHISM AND DUCK TYPING
# -------------------------------------------------------------------------
class PDFReport:
    def render(self) -> str:
        return "Rendering PDF Document Layout"


class HTMLReport:
    def render(self) -> str:
        return "<div>Rendering HTML Document View</div>"


class JSONReport:
    def render(self) -> str:
        return '{"type": "JSONReport", "status": "rendered"}'


def render_any_report(report_object: Any) -> str:
    """Polymorphic dispatcher using Duck Typing ('if it has render(), invoke it')."""
    if not hasattr(report_object, "render") or not callable(getattr(report_object, "render")):
        raise TypeError("Object does not implement callable render() method")
    return report_object.render()


def demonstrate_polymorphism_and_duck_typing() -> Dict[str, Any]:
    """Executes polymorphic dispatch across unrelated duck-typed objects."""
    reports = [PDFReport(), HTMLReport(), JSONReport()]
    rendered_outputs = [render_any_report(r) for r in reports]

    return {
        "total_rendered": len(rendered_outputs),
        "pdf_output": rendered_outputs[0],
        "html_output": rendered_outputs[1],
        "json_output": rendered_outputs[2],
    }


# -------------------------------------------------------------------------
# 7. COMPOSITION VS INHERITANCE
# -------------------------------------------------------------------------
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower: int = horsepower

    def start(self) -> str:
        return f"Engine ({self.horsepower} HP) vrooming"


class CarComposition:
    """Demonstrates 'Has-A' Composition relationship instead of 'Is-A' Inheritance."""

    def __init__(self, model: str, horsepower: int) -> None:
        self.model: str = model
        self.engine: Engine = Engine(horsepower)

    def start_car(self) -> str:
        return f"Car {self.model}: {self.engine.start()}"


def demonstrate_composition_vs_inheritance() -> Dict[str, Any]:
    """Executes object composition pattern."""
    car = CarComposition("Mustang", 450)
    return {
        "car_model": car.model,
        "engine_hp": car.engine.horsepower,
        "start_status": car.start_car(),
    }


# -------------------------------------------------------------------------
# 8. MAGIC DUNDER METHODS
# -------------------------------------------------------------------------
class CustomContainer:
    """Demonstrates magic dunder methods for container behavior and operator overloading."""

    def __init__(self, name: str, items: Optional[List[Any]] = None) -> None:
        self.name: str = name
        self.items: List[Any] = list(items) if items is not None else []

    def __str__(self) -> str:
        return f"Container '{self.name}' with {len(self.items)} items"

    def __repr__(self) -> str:
        return f"CustomContainer(name={self.name!r}, items={self.items!r})"

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> Any:
        return self.items[index]

    def __add__(self, other: Any) -> "CustomContainer":
        if not isinstance(other, CustomContainer):
            raise TypeError("Can only add CustomContainer to another CustomContainer")
        combined_items = self.items + other.items
        return CustomContainer(f"{self.name}+{other.name}", combined_items)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CustomContainer):
            return False
        return self.items == other.items

    def __call__(self, multiplier: int = 1) -> List[Any]:
        return self.items * multiplier


def demonstrate_magic_dunder_methods() -> Dict[str, Any]:
    """Executes custom dunder method overloading."""
    c1 = CustomContainer("Alpha", [10, 20])
    c2 = CustomContainer("Beta", [30, 40])
    c3 = c1 + c2

    return {
        "c1_str": str(c1),
        "c1_repr": repr(c1),
        "c3_len": len(c3),
        "c3_first_item": c3[0],
        "c3_callable": c1(2),
        "containers_equal": c1 == CustomContainer("Copy", [10, 20]),
    }


# -------------------------------------------------------------------------
# 9. STATIC AND CLASS METHODS & FACTORY CONSTRUCTORS
# -------------------------------------------------------------------------
class TemperatureConverter:
    """Demonstrates @classmethod factory constructors and @staticmethod utility helpers."""

    unit_system: str = "Metric / Imperial"

    @classmethod
    def from_celsius_list(cls, celsius_values: List[float]) -> List[float]:
        """Class method processing values with class context."""
        return [cls.celsius_to_fahrenheit(c) for c in celsius_values]

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Static method pure utility converter."""
        if not isinstance(celsius, (int, float)):
            raise TypeError("Celsius value must be numeric")
        return (float(celsius) * 9 / 5) + 32.0


class UserFactory(User):
    """Subclass of User demonstrating multiple @classmethod factory constructors."""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserFactory":
        """Factory constructor instantiating from a dictionary payload."""
        return cls(data["first_name"], data["last_name"], data["payment"])

    @classmethod
    def from_formatted_string(cls, string_data: str) -> "UserFactory":
        """Factory constructor instantiating from hyphenated string (e.g. 'Jane-Doe-300')."""
        parts = string_data.split("-")
        if len(parts) != 3:
            raise ValueError("String payload must be formatted as 'FirstName-LastName-Payment'")
        return cls(parts[0], parts[1], float(parts[2]))


def demonstrate_static_and_class_methods() -> Dict[str, Any]:
    """Executes static and class method converters."""
    single_f = TemperatureConverter.celsius_to_fahrenheit(100.0)
    list_f = TemperatureConverter.from_celsius_list([0.0, 25.0, 100.0])

    # Class method factory instantiation
    user1 = UserFactory.from_dict({"first_name": "Bob", "last_name": "Miller", "payment": 150.0})
    user2 = UserFactory.from_formatted_string("Jane-Doe-300.0")

    return {
        "boiling_point_f": single_f,
        "converted_list_f": list_f,
        "unit_system": TemperatureConverter.unit_system,
        "user1_email": user1.email,
        "user2_full_name": user2.full_name(),
        "user2_payment": user2.payment,
    }


# -------------------------------------------------------------------------
# 10. ABSTRACT BASE CLASSES (ABC)
# -------------------------------------------------------------------------
class BaseDatabaseConnector(abc.ABC):
    """Abstract Base Class establishing contract for database connectors."""

    def __init__(self, connection_str: str) -> None:
        self.connection_str: str = connection_str

    @abc.abstractmethod
    def connect(self) -> str:
        """Abstract method requiring subclass implementation."""
        pass

    @abc.abstractmethod
    def query(self, sql: str) -> Dict[str, Any]:
        """Abstract method requiring subclass implementation."""
        pass


class PostgresConnector(BaseDatabaseConnector):
    def connect(self) -> str:
        return f"Connected to PostgreSQL database at {self.connection_str}"

    def query(self, sql: str) -> Dict[str, Any]:
        return {"db": "PostgreSQL", "query": sql, "status": "SUCCESS", "rows": 5}


def demonstrate_abstract_base_classes() -> Dict[str, Any]:
    """Executes Abstract Base Class instantiation validation and subclass implementation."""
    cannot_instantiate_abstract = False
    try:
        BaseDatabaseConnector("test_db")  # type: ignore
    except TypeError:
        cannot_instantiate_abstract = True

    pg_db = PostgresConnector("postgresql://localhost:5432/production_db")
    conn_status = pg_db.connect()
    query_result = pg_db.query("SELECT * FROM users;")

    return {
        "cannot_instantiate_abstract": cannot_instantiate_abstract,
        "conn_status": conn_status,
        "query_result": query_result,
        "is_connector_subclass": issubclass(PostgresConnector, BaseDatabaseConnector),
    }


# -------------------------------------------------------------------------
# 11. BUILT-IN SUBCLASSING & CONTAINER OPERATOR OVERLOADING
# -------------------------------------------------------------------------
class LoggingDict(dict):
    """Dictionary subclass logging key assignment operations."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.log_history: List[str] = []

    def __setitem__(self, key: Any, value: Any) -> None:
        entry = f"Assigning key '{key}' -> value '{value}'"
        self.log_history.append(entry)
        super().__setitem__(key, value)


class OneBasedList(list):
    """List subclass supporting 1-based indexing for container sequences."""

    def __getitem__(self, index: Any) -> Any:
        if isinstance(index, int):
            if index > 0:
                return super().__getitem__(index - 1)
            elif index < 0:
                return super().__getitem__(index)
            raise IndexError("1-based index cannot be zero.")
        return super().__getitem__(index)

    def __setitem__(self, index: Any, value: Any) -> None:
        if isinstance(index, int) and index > 0:
            super().__setitem__(index - 1, value)
        else:
            super().__setitem__(index, value)


def demonstrate_builtin_subclassing() -> Dict[str, Any]:
    """Executes native dict and list subclass container behaviors."""
    log_dict = LoggingDict()
    log_dict["user_id"] = "USR-998"
    log_dict["status"] = "ACTIVE"

    one_list = OneBasedList(["Python", "OOP", "Architecture", "Design Patterns"])
    first_item = one_list[1]  # 1-based index returns "Python"
    second_item = one_list[2]

    one_list[1] = "Modern Python"
    updated_first = one_list[1]

    return {
        "log_dict_keys": list(log_dict.keys()),
        "log_history_count": len(log_dict.log_history),
        "log_history_entry": log_dict.log_history[0],
        "one_list_first_item": first_item,
        "one_list_second_item": second_item,
        "updated_first_item": updated_first,
    }


# -------------------------------------------------------------------------
# 12. DESCRIPTORS, MIXINS & SUBCLASS REGISTRATION HOOKS
# -------------------------------------------------------------------------
class BoundedIntegerDescriptor:
    """Descriptor enforcing integer type and boundary constraints on class attributes."""

    def __init__(self, min_value: int = 0, max_value: int = 100) -> None:
        self.min_value: int = min_value
        self.max_value: int = max_value
        self.private_name: str = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self.private_name = f"_{name}"

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.min_value)

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Attribute '{self.private_name[1:]}' must be an integer.")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"Attribute '{self.private_name[1:]}' value {value} must be between "
                f"{self.min_value} and {self.max_value}."
            )
        setattr(instance, self.private_name, value)


class JSONSerializerMixin:
    """Mixin class providing reusable JSON serialization capability."""

    def to_json(self) -> str:
        clean_dict = {
            k.lstrip("_"): v
            for k, v in self.__dict__.items()
            if not callable(v) and not k.startswith("__")
        }
        return json.dumps(clean_dict, sort_keys=True)


class PluginBase:
    """Base class utilizing __init_subclass__ (PEP 487) for automatic subclass registration."""

    registered_plugins: Dict[str, Type["PluginBase"]] = {}

    def __init_subclass__(cls, plugin_name: str = "", **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        name = plugin_name or cls.__name__
        cls.registered_plugins[name] = cls


class AnalyticsPlugin(PluginBase, JSONSerializerMixin):
    """Concrete plugin derived from PluginBase and JSONSerializerMixin using descriptor validation."""

    score = BoundedIntegerDescriptor(min_value=0, max_value=100)

    def __init__(self, plugin_id: str, score: int) -> None:
        self.plugin_id: str = plugin_id
        self.score = score


def demonstrate_mixins_and_descriptors() -> Dict[str, Any]:
    """Executes descriptor validation, mixin JSON serialization, and __init_subclass__ registration."""
    plugin = AnalyticsPlugin("PLG-101", 95)
    json_output = plugin.to_json()

    # Descriptor validation check
    invalid_bound = False
    try:
        plugin.score = 150  # Exceeds max_value 100
    except ValueError:
        invalid_bound = True

    return {
        "plugin_id": plugin.plugin_id,
        "score": plugin.score,
        "json_output": json_output,
        "invalid_bound_raised": invalid_bound,
        "registered_plugin_names": list(PluginBase.registered_plugins.keys()),
    }


# -------------------------------------------------------------------------
# 13. EXERCISE 1: BANK ACCOUNT & SAVINGS ACCOUNT HIERARCHY
# -------------------------------------------------------------------------
class BankAccount:
    """Base class representing a standard bank account with balance guards."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        if not isinstance(account_holder, str) or not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder: str = account_holder.strip()
        self._balance: float = float(initial_balance)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= float(amount)
        return self._balance


class SavingsAccount(BankAccount):
    """Savings account extending BankAccount with interest rate calculations."""

    def __init__(
        self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.03
    ) -> None:
        super().__init__(account_holder, initial_balance)
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate: float = float(interest_rate)

    def apply_interest(self) -> float:
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return self._balance


def demonstrate_bank_account_exercise() -> Dict[str, Any]:
    """Executes bank account deposit, withdrawal, and savings interest calculations."""
    acc = SavingsAccount("Robert Johnson", 1000.0, interest_rate=0.05)
    acc.deposit(500.0)
    balance_after_deposit = acc.balance

    acc.withdraw(200.0)
    balance_after_withdrawal = acc.balance

    balance_after_interest = acc.apply_interest()

    return {
        "account_holder": acc.account_holder,
        "balance_after_deposit": balance_after_deposit,
        "balance_after_withdrawal": balance_after_withdrawal,
        "balance_after_interest": balance_after_interest,
    }


# -------------------------------------------------------------------------
# 14. EXERCISE 2: VEHICLE FLEET MANAGEMENT & ELECTRIC CARS
# -------------------------------------------------------------------------
class FleetVehicle:
    """Base class for transport fleet vehicles tracking mileage."""

    def __init__(self, make: str, model: str, year: int) -> None:
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("make and model must be strings")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("year must be a valid integer year (>= 1886)")

        self.make: str = make
        self.model: str = model
        self.year: int = year
        self._mileage: float = 0.0

    @property
    def mileage(self) -> float:
        return self._mileage

    def drive(self, distance: float) -> float:
        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Distance cannot be negative.")
        self._mileage += float(distance)
        return self._mileage

    def vehicle_info(self) -> str:
        return f"{self.year} {self.make} {self.model} (Mileage: {self._mileage} km)"


class ElectricCarFleet(FleetVehicle):
    """Subclass representing an electric car with battery capacity management."""

    def __init__(
        self, make: str, model: str, year: int, battery_capacity_kwh: float
    ) -> None:
        super().__init__(make, model, year)
        if not isinstance(battery_capacity_kwh, (int, float)) or battery_capacity_kwh <= 0:
            raise ValueError("battery_capacity_kwh must be positive")
        self.battery_capacity_kwh: float = float(battery_capacity_kwh)
        self.battery_level_percent: float = 100.0

    def drive_electric(self, distance: float, kwh_per_km: float = 0.2) -> float:
        """Drive electric vehicle consuming battery level percentage."""
        self.drive(distance)
        consumed_kwh = distance * kwh_per_km
        consumed_percent = (consumed_kwh / self.battery_capacity_kwh) * 100.0
        self.battery_level_percent = max(0.0, self.battery_level_percent - consumed_percent)
        return self.battery_level_percent

    def charge(self) -> float:
        self.battery_level_percent = 100.0
        return self.battery_level_percent


def demonstrate_vehicle_fleet_exercise() -> Dict[str, Any]:
    """Executes vehicle fleet management and electric car battery charging."""
    ev = ElectricCarFleet("Tesla", "Model Y", 2024, 75.0)
    initial_info = ev.vehicle_info()

    battery_after_trip = ev.drive_electric(150.0)
    mileage_after_trip = ev.mileage

    recharged_level = ev.charge()

    return {
        "initial_info": initial_info,
        "mileage_after_trip": mileage_after_trip,
        "battery_after_trip": round(battery_after_trip, 1),
        "recharged_level": recharged_level,
        "battery_capacity": ev.battery_capacity_kwh,
    }


if __name__ == "__main__":
    print("=== Python Object-Oriented Programming (OOP) Master Suite ===")
    print("0. Class Definition Basics:", demonstrate_class_definition_basics())
    print("1. Class vs Instance Attrs:", demonstrate_class_and_instance_attributes())
    print("1B. Class & Instance Data:", demonstrate_class_and_instance_data())
    print("2. Constructors:", demonstrate_constructors_and_initialization())
    print("3. Encapsulation & Properties:", demonstrate_encapsulation_and_properties())
    print("4. Inheritance & super():", demonstrate_inheritance_and_super())
    print("5. Multiple Inheritance & MRO:", demonstrate_multiple_inheritance_and_mro())
    print("6. Polymorphism & Duck Typing:", demonstrate_polymorphism_and_duck_typing())
    print("7. Composition vs Inheritance:", demonstrate_composition_vs_inheritance())
    print("8. Magic Dunder Methods:", demonstrate_magic_dunder_methods())
    print("9. Static & Class Methods:", demonstrate_static_and_class_methods())
    print("10. Abstract Base Classes (ABC):", demonstrate_abstract_base_classes())
    print("11. Built-in Subclassing:", demonstrate_builtin_subclassing())
    print("12. Mixins & Descriptors:", demonstrate_mixins_and_descriptors())
    print("13. Exercise 1 - Bank Account:", demonstrate_bank_account_exercise())
    print("14. Exercise 2 - Vehicle Fleet:", demonstrate_vehicle_fleet_exercise())
