"""cloud_app/tutorials/software_architecture_basics.py

Software Architecture & Enterprise Design Patterns Masterclass
================================================================
Comprehensive tutorial module demonstrating Python software architecture concepts:
1. Layered Architecture
2. MVC / MVT Framework Patterns
3. Service Layer Pattern
4. Repository Pattern
5. Dependency Injection (DI)
6. SOLID Architecture Principles
7. Gang of Four (GoF) Design Patterns (Singleton, Factory, Strategy, Observer, Decorator, Adapter)
8. Modular Architecture
9. Clean Architecture (Entities, Use Cases, Interface Adapters)
10. Domain-Driven Design (DDD) Concepts (Entities, Value Objects, Aggregates, Domain Events)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar
import uuid

T = TypeVar("T")


# ==============================================================================
# 1. DOMAIN-DRIVEN DESIGN (DDD) CONCEPTS: VALUE OBJECTS, ENTITIES & EVENTS
# ==============================================================================


@dataclass(frozen=True)
class Money:
    """DDD Value Object: Immutable monetary value with currency validation."""

    amount: float
    currency: str = "USD"

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Monetary amount cannot be negative.")
        if not self.currency or len(self.currency) != 3:
            raise ValueError("Currency must be a 3-letter ISO code (e.g. USD, EUR).")

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}.")
        return Money(amount=self.amount + other.amount, currency=self.currency)

    def multiply(self, factor: float) -> "Money":
        return Money(amount=round(self.amount * factor, 2), currency=self.currency)


@dataclass(frozen=True)
class DomainEvent:
    """DDD Domain Event representing a significant state change."""

    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    name: str = "DomainEvent"


@dataclass(frozen=True)
class OrderPlacedEvent(DomainEvent):
    order_id: str = ""
    customer_id: str = ""
    total_amount: float = 0.0
    name: str = "OrderPlaced"


@dataclass
class OrderLineItem:
    """DDD Entity inside Order Aggregate."""

    product_id: str
    product_name: str
    unit_price: Money
    quantity: int

    @property
    def subtotal(self) -> Money:
        return self.unit_price.multiply(self.quantity)


class OrderAggregate:
    """DDD Aggregate Root: Guarantees consistency invariants for order items."""

    def __init__(self, order_id: str, customer_id: str) -> None:
        self.order_id: str = order_id
        self.customer_id: str = customer_id
        self._items: List[OrderLineItem] = []
        self._status: str = "PENDING"
        self._events: List[DomainEvent] = []

    @property
    def items(self) -> List[OrderLineItem]:
        return list(self._items)

    @property
    def status(self) -> str:
        return self._status

    @property
    def total_amount(self) -> Money:
        if not self._items:
            return Money(0.0)
        curr = self._items[0].unit_price.currency
        total = sum(item.subtotal.amount for item in self._items)
        return Money(amount=round(total, 2), currency=curr)

    def add_item(
        self, product_id: str, product_name: str, unit_price: Money, quantity: int
    ) -> None:
        """Enforce aggregate invariant: cannot modify fulfilled orders."""
        if self._status != "PENDING":
            raise InvalidOperationError(
                f"Cannot add items to order in {self._status} status."
            )
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        line_item = OrderLineItem(product_id, product_name, unit_price, quantity)
        self._items.append(line_item)

    def checkout(self) -> OrderPlacedEvent:
        """Place order and publish domain event."""
        if not self._items:
            raise InvalidOperationError("Cannot checkout an empty order aggregate.")

        self._status = "PLACED"
        event = OrderPlacedEvent(
            order_id=self.order_id,
            customer_id=self.customer_id,
            total_amount=self.total_amount.amount,
        )
        self._events.append(event)
        return event

    def collect_events(self) -> List[DomainEvent]:
        events = list(self._events)
        self._events.clear()
        return events


# ==============================================================================
# 2. CUSTOM DOMAIN EXCEPTIONS
# ==============================================================================


class ArchitectureError(Exception):
    """Base exception for architecture domain errors."""

    pass


class EntityNotFoundError(ArchitectureError):
    """Raised when requested entity is missing."""

    pass


class InvalidOperationError(ArchitectureError):
    """Raised when an operation violates domain invariants."""

    pass


# ==============================================================================
# 3. REPOSITORY PATTERN & DATA ACCESS LAYER
# ==============================================================================


class OrderRepositoryProtocol(ABC):
    """Repository Pattern Interface for Order Aggregates."""

    @abstractmethod
    def save(self, order: OrderAggregate) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[OrderAggregate]:
        pass

    @abstractmethod
    def list_all(self) -> List[OrderAggregate]:
        pass


class InMemoryOrderRepository(OrderRepositoryProtocol):
    """In-Memory Repository Implementation for Testing & Mocking."""

    def __init__(self) -> None:
        self._storage: Dict[str, OrderAggregate] = {}

    def save(self, order: OrderAggregate) -> None:
        self._storage[order.order_id] = order

    def get_by_id(self, order_id: str) -> Optional[OrderAggregate]:
        return self._storage.get(order_id)

    def list_all(self) -> List[OrderAggregate]:
        return list(self._storage.values())


# ==============================================================================
# 4. GANG OF FOUR (GoF) DESIGN PATTERNS
# ==============================================================================


# A. Singleton Pattern
class DatabaseConnectionPool:
    """Singleton Pattern: Ensures a single thread-safe instance exists."""

    _instance: Optional["DatabaseConnectionPool"] = None

    def __new__(cls) -> "DatabaseConnectionPool":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections_available = 10
            cls._instance.is_connected = True
        return cls._instance


# B. Factory Pattern
class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        pass


class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"[EMAIL sent to {recipient}]: {message}"


class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"[SMS sent to {recipient}]: {message}"


class NotificationFactory:
    """Factory Pattern: Instantiates notification strategies dynamically."""

    @staticmethod
    def create_notification(channel: str) -> Notification:
        channel_clean = channel.strip().lower()
        if channel_clean == "email":
            return EmailNotification()
        elif channel_clean == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unsupported notification channel: {channel}")


# C. Strategy Pattern
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float) -> float:
        pass


class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return round(5.0 + (weight_kg * 1.5), 2)


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return round(15.0 + (weight_kg * 3.0), 2)


# D. Observer Pattern
class DomainEventBus:
    """Observer Pattern: Event Dispatcher for Domain Events."""

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Callable[[DomainEvent], None]]] = {}

    def subscribe(
        self, event_type: str, handler: Callable[[DomainEvent], None]
    ) -> None:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event: DomainEvent) -> List[str]:
        logs: List[str] = []
        handlers = self._subscribers.get(event.name, [])
        for handler in handlers:
            handler(event)
            logs.append(f"Handled event {event.name} via {handler.__name__}")
        return logs


# E. Adapter Pattern
class LegacyPaymentSDK:
    """Legacy third-party SDK with non-standard method signatures."""

    def make_charge(self, cents: int, email_addr: str) -> Dict[str, Any]:
        return {"result_code": 200, "tx_id": "legacy_tx_99", "charged_cents": cents}


class PaymentGatewayProtocol(ABC):
    @abstractmethod
    def charge(self, amount: float, customer_email: str) -> Dict[str, Any]:
        pass


class LegacyPaymentAdapter(PaymentGatewayProtocol):
    """Adapter Pattern: Adapts LegacyPaymentSDK to PaymentGatewayProtocol interface."""

    def __init__(self, legacy_sdk: LegacyPaymentSDK) -> None:
        self._sdk = legacy_sdk

    def charge(self, amount: float, customer_email: str) -> Dict[str, Any]:
        cents = int(amount * 100)
        res = self._sdk.make_charge(cents, customer_email)
        return {
            "success": res["result_code"] == 200,
            "transaction_id": res["tx_id"],
            "amount_charged": amount,
        }


# ==============================================================================
# 5. SERVICE LAYER & DEPENDENCY INJECTION (DI)
# ==============================================================================


class OrderService:
    """Service Layer & Use Case Interactor.

    Encapsulates application workflows and orchestrates Domain Aggregates,
    Repositories, and Gateway Services via Dependency Injection.
    """

    def __init__(
        self,
        repository: OrderRepositoryProtocol,
        payment_gateway: PaymentGatewayProtocol,
        event_bus: DomainEventBus,
    ) -> None:
        self._repository = repository
        self._payment_gateway = payment_gateway
        self._event_bus = event_bus

    def create_and_place_order(
        self,
        order_id: str,
        customer_id: str,
        customer_email: str,
        items: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Use Case: Create order aggregate, add items, charge payment, save, and publish events."""

        # 1. Instantiate Aggregate Root
        order = OrderAggregate(order_id, customer_id)

        for item in items:
            price = Money(amount=item["price"], currency=item.get("currency", "USD"))
            order.add_item(
                product_id=item["product_id"],
                product_name=item["name"],
                unit_price=price,
                quantity=item["quantity"],
            )

        # 2. Execute Domain Checkout
        placed_event = order.checkout()

        # 3. Process External Payment Gateway Charge
        payment_result = self._payment_gateway.charge(
            amount=order.total_amount.amount,
            customer_email=customer_email,
        )

        if not payment_result.get("success"):
            raise ArchitectureError("Payment processing failed during checkout.")

        # 4. Save via Repository
        self._repository.save(order)

        # 5. Publish Domain Events
        event_logs = self._event_bus.publish(placed_event)

        return {
            "order_id": order.order_id,
            "status": order.status,
            "total": order.total_amount.amount,
            "currency": order.total_amount.currency,
            "item_count": len(order.items),
            "payment": payment_result,
            "event_logs": event_logs,
        }


# ==============================================================================
# 6. MVC / MVT PATTERN DEMONSTRATION
# ==============================================================================


@dataclass
class OrderViewModel:
    """MVC / MVT Model Representation for UI views."""

    order_id: str
    customer_id: str
    formatted_total: str
    status_badge: str


class OrderViewRenderer:
    """MVC View / Template Component."""

    @staticmethod
    def render_html_card(view_model: OrderViewModel) -> str:
        return f"""<div class="order-card">
  <h3>Order #{view_model.order_id}</h3>
  <p>Customer: <strong>{view_model.customer_id}</strong></p>
  <p>Total: <span class="price">{view_model.formatted_total}</span></p>
  <span class="badge">{view_model.status_badge}</span>
</div>"""


class OrderController:
    """MVC Controller orchestrating HTTP requests to Views."""

    def __init__(self, order_service: OrderService) -> None:
        self._service = order_service

    def handle_checkout_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        result = self._service.create_and_place_order(
            order_id=payload["order_id"],
            customer_id=payload["customer_id"],
            customer_email=payload["customer_email"],
            items=payload["items"],
        )

        view_model = OrderViewModel(
            order_id=result["order_id"],
            customer_id=payload["customer_id"],
            formatted_total=f"${result['total']:.2f} {result['currency']}",
            status_badge=f"Badge: {result['status']}",
        )

        html = OrderViewRenderer.render_html_card(view_model)
        return {"status_code": 201, "html_response": html, "raw_data": result}


# ==============================================================================
# 7. DEMONSTRATION HELPER FUNCTIONS FOR INTERACTIVE STUDIO
# ==============================================================================


def demonstrate_layered_and_clean_architecture() -> Dict[str, Any]:
    """Demonstrate end-to-end Layered & Clean Architecture flow."""
    repo = InMemoryOrderRepository()
    legacy_sdk = LegacyPaymentSDK()
    adapter = LegacyPaymentAdapter(legacy_sdk)
    event_bus = DomainEventBus()

    received_events: List[str] = []

    def on_order_placed(evt: DomainEvent) -> None:
        received_events.append(f"Event {evt.name} received for order")

    event_bus.subscribe("OrderPlaced", on_order_placed)

    service = OrderService(
        repository=repo, payment_gateway=adapter, event_bus=event_bus
    )
    controller = OrderController(service)

    payload = {
        "order_id": "ORD-2026-888",
        "customer_id": "CUST-101",
        "customer_email": "architecture.lead@teachcloud.dev",
        "items": [
            {
                "product_id": "PROD-1",
                "name": "Clean Architecture Book",
                "price": 45.0,
                "quantity": 1,
            },
            {
                "product_id": "PROD-2",
                "name": "DDD Domain Guide",
                "price": 55.0,
                "quantity": 2,
            },
        ],
    }

    response = controller.handle_checkout_request(payload)
    fetched_order = repo.get_by_id("ORD-2026-888")

    return {
        "status_code": response["status_code"],
        "order_total": fetched_order.total_amount.amount if fetched_order else 0.0,
        "items_count": len(fetched_order.items) if fetched_order else 0,
        "html_preview": response["html_response"],
        "received_event_count": len(received_events),
    }


def demonstrate_design_patterns() -> Dict[str, Any]:
    """Demonstrate Singleton, Factory, Strategy, Observer, and Adapter patterns."""
    # Singleton
    pool1 = DatabaseConnectionPool()
    pool2 = DatabaseConnectionPool()
    singleton_valid = pool1 is pool2

    # Factory
    notifier = NotificationFactory.create_notification("email")
    email_msg = notifier.send("dev@teachcloud.dev", "Architecture Build Succeeded")

    # Strategy
    std_ship = StandardShipping()
    exp_ship = ExpressShipping()

    # Adapter
    legacy_adapter = LegacyPaymentAdapter(LegacyPaymentSDK())
    charge_res = legacy_adapter.charge(125.50, "buyer@domain.com")

    return {
        "singleton_is_same_instance": singleton_valid,
        "factory_notification": email_msg,
        "standard_shipping_cost": std_ship.calculate_cost(4.0),
        "express_shipping_cost": exp_ship.calculate_cost(4.0),
        "adapter_charge_success": charge_res["success"],
    }


def demonstrate_ddd_concepts() -> Dict[str, Any]:
    """Demonstrate DDD Value Objects, Entities, and Aggregate Invariants."""
    m1 = Money(100.0, "USD")
    m2 = Money(50.50, "USD")
    m3 = m1.add(m2)

    order = OrderAggregate("ORD-DDD-1", "CUST-999")
    order.add_item("P1", "Domain Handbook", Money(49.99), 2)
    evt = order.checkout()

    return {
        "value_object_sum": m3.amount,
        "aggregate_total": order.total_amount.amount,
        "aggregate_status": order.status,
        "domain_event_name": evt.name,
    }


if __name__ == "__main__":
    print("=== Software Architecture Masterclass Module ===")
    print("Layered & Clean Arch:", demonstrate_layered_and_clean_architecture())
    print("Design Patterns:", demonstrate_design_patterns())
    print("DDD Concepts:", demonstrate_ddd_concepts())
