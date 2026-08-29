"""
Demonstrates empty dictionary instantiation and element insertion.
"""

def demo_empty_dict():
    vehicles = {}
    vehicles['Car'] = 'Audi'
    vehicles['truck'] = 'Lorry'

    print('Vehicles dict:', vehicles)
    return vehicles

if __name__ == '__main__':
    demo_empty_dict()
