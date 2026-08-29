"""
Demonstrates nested dictionary lookups and chaining string operations.
"""

def demo_nested_dict():
    nested_data = {'animal': {'bird': {'car': 'Audi'}}}

    car_val = nested_data['animal']['bird']['car']
    upper_car = car_val.upper()

    print('Nested car value:', car_val)
    print('Upper car value:', upper_car)

    return car_val, upper_car

if __name__ == '__main__':
    demo_nested_dict()
