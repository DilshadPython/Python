"""
Backwards-compatible wrapper alias for default_parameters.py (descriptive filename).
"""
from Function.default_parameters import myfunc

__all__ = ["myfunc"]

if __name__ == '__main__':
    print("myfunc(4) ->", myfunc(4))
