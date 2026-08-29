"""
Demonstrates tax bracket calculation functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union

def pay_tax(salary: Union[int, float]) -> Union[int, float]:
    """Calculate annual income tax based on progressive tax brackets."""
    if salary <= 10000:
        return 0
    elif 11000 <= salary <= 35000:
        return salary * 0.17
    else:
        return salary * 0.27

def neto_pay(grosspay: Union[int, float]) -> Union[int, float]:
    """Calculate net pay after tax deduction."""
    return grosspay - pay_tax(grosspay)

if __name__ == '__main__':
    salary = 30000
    print(f"Gross Pay: {salary} | Tax: {pay_tax(salary)} | Net Pay: {neto_pay(salary)}")
