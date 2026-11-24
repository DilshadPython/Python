"""
Demonstrates combining list comprehensions with zip() to construct dictionary mappings.
"""

def demo_zip_comprehension():
    cars = ['Audi', 'Mercedes', 'BMW', 'Ford']
    models = ['A7', 'A20', 'XM', 'F16']

    zipped_pairs = list(zip(cars, models))
    car_dict = dict(zip(cars, models))

    keys_list = list(car_dict.keys())
    values_list = list(car_dict.values())

    print('Zipped pairs:', zipped_pairs)
    print('Car dictionary:', car_dict)
    print('Keys list:', keys_list)
    print('Values list:', values_list)

    return zipped_pairs, car_dict, keys_list, values_list

if __name__ == '__main__':
    demo_zip_comprehension()
