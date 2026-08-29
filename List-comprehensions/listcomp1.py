"""
Demonstrates string method invocation inside list comprehensions.
"""

def demo_string_case_conversion():
    cars = ['AUDI', 'BMW', 'TOYOTA', 'VOLVO', 'VOLKSWAGEN', 'FORD']
    lowercase_cars = [car.lower() for car in cars]
    print('Original cars:', cars)
    print('Lowercase cars:', lowercase_cars)
    return lowercase_cars

if __name__ == '__main__':
    demo_string_case_conversion()
