# =========================================================================
# PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) BASICS & ARCHITECTURE
# Sourced & Standardized from DilshadPython/Python/Object-Oriented
# =========================================================================
import abc
import sys
from typing import Any, Dict, List, Optional, Tuple, Union


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

    # Class attribute modification applies to class scope
    initial_company = emp1.company_name

    # Instance shadow attribute
    emp2.company_name = "TechCorp Labs"

    # Dynamic attribute addition & deletion using delattr
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

    # Dynamic attribute deletion on instance payload attribute
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
        self.owner: str = owner            # Public
        self._account_type: str = "Savings" # Protected by convention
        self.__balance: float = 0.0        # Private (Name Mangled)
        self.balance = balance             # Property setter validation

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

    # Inspect CPython private name mangling attribute
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
        # Overrides parent method while utilizing parent state
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
        self.engine: Engine = Engine(horsepower)  # Composed Engine instance

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
# 9. STATIC AND CLASS METHODS
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


def demonstrate_static_and_class_methods() -> Dict[str, Any]:
    """Executes static and class method converters."""
    single_f = TemperatureConverter.celsius_to_fahrenheit(100.0)
    list_f = TemperatureConverter.from_celsius_list([0.0, 25.0, 100.0])

    return {
        "boiling_point_f": single_f,
        "converted_list_f": list_f,
        "unit_system": TemperatureConverter.unit_system,
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
    # Attempting to instantiate BaseDatabaseConnector directly raises TypeError
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


if __name__ == "__main__":
    print("=== Python Object-Oriented Programming (OOP) Demo ===")
    print("1. Class vs Instance Attrs:", demonstrate_class_and_instance_attributes())
    print("2. Constructors:", demonstrate_constructors_and_initialization())
    print("3. Encapsulation & Properties:", demonstrate_encapsulation_and_properties())
    print("4. Inheritance & super():", demonstrate_inheritance_and_super())
    print("5. Multiple Inheritance & MRO:", demonstrate_multiple_inheritance_and_mro())
    print("6. Polymorphism & Duck Typing:", demonstrate_polymorphism_and_duck_typing())
    print("7. Composition vs Inheritance:", demonstrate_composition_vs_inheritance())
    print("8. Magic Dunder Methods:", demonstrate_magic_dunder_methods())
    print("9. Static & Class Methods:", demonstrate_static_and_class_methods())
    print("10. Abstract Base Classes (ABC):", demonstrate_abstract_base_classes())
