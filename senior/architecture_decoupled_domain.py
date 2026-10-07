"""
Track 07: Architecture Patterns & Decoupled Domain Modeling

Description: Master Senior Python Track 07: Decoupled Domain Architecture (Cosmic Python). Domain Aggregates, Repository Pattern, Unit of Work (UoW), Service Layer, and CQRS.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/architecture_decoupled_domain
"""

# --- Code Snippet 1 ---
from dataclasses import dataclass
from typing import Protocol

@dataclass
class AllocationLine:
    order_id: str
    sku: str
    qty: int

class Batch:
    """Pure Domain Aggregate with Zero External Imports."""
    def __init__(self, ref: str, sku: str, qty: int):
        self.ref = ref
        self.sku = sku
        self._available_qty = qty

    def can_allocate(self, line: AllocationLine) -> bool:
        return self.sku == line.sku and self._available_qty >= line.qty

    def allocate(self, line: AllocationLine) -> None:
        if not self.can_allocate(line):
            raise ValueError(f"Cannot allocate {line.qty} of {line.sku}")
        self._available_qty -= line.qty

class AbstractBatchRepository(Protocol):
    def add(self, batch: Batch) -> None: ...
    def get(self, ref: str) -> Batch | None: ...

# --- Code Snippet 2 ---
class AbstractUnitOfWork(Protocol):
    batches: AbstractBatchRepository

    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...

def allocate_order_service(line: AllocationLine, uow: AbstractUnitOfWork) -> str:
    """Service layer coordinating domain workflow via Unit of Work."""
    with uow:
        batch = uow.batches.get_by_sku(line.sku)
        if not batch:
            raise ValueError(f"No batch found for SKU {line.sku}")
        batch.allocate(line)
        uow.commit()
        return batch.ref

# --- Code Snippet 3 ---
from typing import TypedDict

class BatchReadView(TypedDict):
    batch_ref: str
    sku: str
    available_qty: int

def query_allocations_read_path(db_connection, sku: str) -> list[BatchReadView]:
    """CQRS Read Path: Bypasses domain aggregates; executes raw SQL."""
    cursor = db_connection.execute(
        "SELECT ref, sku, available_qty FROM batches WHERE sku = ?", (sku,)
    )
    return [
        {"batch_ref": row[0], "sku": row[1], "available_qty": row[2]}
        for row in cursor.fetchall()
    ]

