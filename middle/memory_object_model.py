"""
Track 03: Object Model & Memory Mechanics

Description: Master Mid-Level Python Object Model: LEGB Scopes, Mutable vs Immutable objects, Shallow vs Deep Copying, Reference Counting, and Garbage Collection.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/memory_object_model
"""

# --- Code Snippet 1 ---
# Global Scope
config_setting = "PRODUCTION"

def outer_service():
    # Enclosing Scope
    request_count = 0

    def inner_counter():
        nonlocal request_count  # Bind to enclosing variable
        request_count += 1
        return request_count

    return inner_counter

counter = outer_service()
print("Call 1:", counter())  # 1
print("Call 2:", counter())  # 2

# --- Code Snippet 2 ---
import copy

original = [1, 2, [3, 4]]

# Shallow Copy: Outer list is copied, inner list is shared reference
shallow = copy.copy(original)
shallow[2].append(99)
print("Original after shallow mutation:", original)  # [1, 2, [3, 4, 99]]

# Deep Copy: Independent recursive clone
deep = copy.deepcopy(original)
deep[2].append(100)
print("Original after deep mutation:", original)     # [1, 2, [3, 4, 99]]
print("Deep object:", deep)                           # [1, 2, [3, 4, 99, 100]]

# --- Code Snippet 3 ---
import sys
import gc

data = ["heavy_payload_block"]
print("Initial Ref Count:", sys.getrefcount(data) - 1)  # 1

alias = data
print("Ref Count after alias:", sys.getrefcount(data) - 1)  # 2

del alias
print("Ref Count after del alias:", sys.getrefcount(data) - 1)  # 1

# Manually inspect & trigger Garbage Collection
collected = gc.collect()
print("GC Collected Objects:", collected)

