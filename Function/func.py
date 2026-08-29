"""
Backwards-compatible wrapper alias for cave_navigation.py (descriptive filename).
"""
from Function.cave_navigation import create_tunnel, visit_cave, choose_cave

__all__ = ["create_tunnel", "visit_cave", "choose_cave"]

if __name__ == '__main__':
    c = {1: [], 2: []}
    create_tunnel(c, 1, 2)
    print("Cave graph:", c)
