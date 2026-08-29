"""
Backwards-compatible wrapper alias for calculate_func.py (corrected spelling).
"""
from Function.calculate_func import calculate

__all__ = ["calculate"]

if __name__ == "__main__":
    add_res, sub_res, mul_res, div_res = calculate(10, 2)
    print(f"Add: {add_res}, Sub: {sub_res}, Mul: {mul_res}, Div: {div_res}")
