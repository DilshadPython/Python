"""
Section 5: Clean Architecture & Domain-Driven Execution Flow

Description: Master Clean Architecture in Python: framework-agnostic business logic, application use cases, abstract repository contracts, and infrastructure adapters.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/clean_architecture
"""

# --- Code Snippet 1 ---
# ─── 1. PURE DOMAIN ENTITY & ABSTRACT REPOSITORY CONTRACT ─────────────────
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Order:
    id: str | None
    user_id: str
    total_amount: float

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> Order:
        ...

# ─── 2. APPLICATION USE CASE ───────────────────────────────────────────────
class CreateOrderUseCase:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def execute(self, user_id: str, amount: float) -> Order:
        order = Order(id=None, user_id=user_id, total_amount=amount)
        return self.repository.save(order)

# ─── 3. INFRASTRUCTURE POSTGRESQL ADAPTER ─────────────────────────────────
class PostgresOrderRepository(OrderRepository):
    def save(self, order: Order) -> Order:
        # SQL INSERT into postgres DB
        order.id = "ord_9988"
        return order

# ─── 4. API DELIVERY ROUTER (FASTAPI / FLASK) ──────────────────────────────
@router.post("/orders")
def create_order_endpoint(payload: dict, db=Depends(get_db)):
    repo = PostgresOrderRepository(db)
    use_case = CreateOrderUseCase(repo)
    return use_case.execute(payload["user_id"], payload["amount"])

