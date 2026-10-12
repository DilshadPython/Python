"""
Track 01: Data Flow & Evaluation Semantics

Description: Master Senior Python Track 01: Data Flow & Evaluation Semantics. Generators, yield from, bytecode LIST_APPEND optimization, collections.deque, itertools.batched, and operator C lookups.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/data_flow_evaluation
"""

# --- Code Snippet 1 ---
from typing import Generator

def stream_log_records(log_lines: list[str]) -> Generator[str, None, None]:
    """Streams cleaned log lines with O(1) memory bound."""
    for line in log_lines:
        if line.strip():
            yield line.strip()

def aggregate_cluster_logs(node_files: dict[str, list[str]]) -> Generator[str, None, None]:
    """Delegates sub-generator streaming across cluster nodes."""
    for node_id, lines in node_files.items():
        yield from stream_log_records(lines)

# --- Code Snippet 2 ---
# Optimized C-level opcode loop (LIST_APPEND)
scores = [60, 75, 80, 45, 95]
doubled = [x * 2 for x in scores if x > 50]

# Keep comprehensions flat; multi-nested loops belong in explicit generator pipelines
def extract_high_value_orders(clients: list[dict]) -> Generator[dict, None, None]:
    for client in clients:
        for order in client.get("orders", []):
            if order.get("total", 0) > 1000:
                yield order

# --- Code Snippet 3 ---
from collections import deque
import itertools
import operator

# 1. O(1) Double-ended sliding window
buffer = deque(maxlen=1000)
buffer.append("new_event")
oldest = buffer.popleft() # O(1) left pop

# 2. itertools.batched zero-copy iterator chunking
for batch in itertools.batched(range(10000), 500):
    pass # Process 500 items per DB batch

# 3. C-speed key extraction with operator.itemgetter & attrgetter
users = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 88}]
top_user = max(users, key=operator.itemgetter("score"))

