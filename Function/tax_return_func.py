"""
Demonstrates annual income tax computation and net pay calculation.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union, Tuple

def pay_tax(salary: Union[int, float]) -> Union[int, float]:
    """Calculate tax based on salary brackets."""
    if salary <= 10000:
        return 0
    elif 11000 <= salary <= 35000:
        return salary * 0.17
    else:
        return salary * 0.27

def neto_pay(grosspay: Union[int, float]) -> Union[int, float]:
    """Calculate net pay after subtracting tax."""
    return grosspay - pay_tax(grosspay)

if __name__ == '__main__':
    salary = 35000
    tax = pay_tax(salary)
    net = neto_pay(salary)
    print(f"Salary: £{salary} | Tax: £{tax} | Net Income: £{net}")
