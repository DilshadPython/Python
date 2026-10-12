"""
Track 08: Databases, Concurrency & Storage Engines

Description: Master Senior Python Track 08: Databases, Concurrency & Storage Engines. B-Tree indexes, EXPLAIN ANALYZE, MVCC, FOR UPDATE SKIP LOCKED, Optimistic Locking, and ORM N+1 mitigations (joinedload vs selectinload).
Level: Senior
URL: http://127.0.0.1:5000/python/senior/databases_concurrency_storage
"""

# --- Code Snippet 1 ---
WHERE version = :v

# --- Code Snippet 2 ---
-- High-Throughput Queue Worker (Pessimistic Lock without Contention)
SELECT * FROM task_queue 
WHERE status = 'pending' 
ORDER BY priority DESC 
FOR UPDATE SKIP LOCKED 
LIMIT 10;

-- Optimistic Concurrency Control (Application Retry Pattern)
UPDATE accounts 
SET balance = balance - :amount, version = version + 1 
WHERE id = :acc_id AND version = :expected_version;

# --- Code Snippet 3 ---
from sqlalchemy.orm import joinedload, selectinload

# 1-to-1 Relationship: Use joinedload (Single SQL LEFT OUTER JOIN)
stmt_user_profile = select(User).options(joinedload(User.profile))

# 1-to-Many Collection: Use selectinload (Secondary SELECT ... WHERE id IN (...))
# Avoids Cartesian row bloat caused by table joins across large collections!
stmt_user_orders = select(User).options(selectinload(User.orders))

