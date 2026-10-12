"""
Demonstrates inspection of dictionary methods using built-in dir().
"""

def demo_dir_dict():
    city = {'name': 'Berlin', 'population': 3.28, 'country': 'Germany', 'capital': True}

    public_methods = [m for m in dir(city) if not m.startswith('_')]
    print('Public dict methods:', public_methods)

    return public_methods

if __name__ == '__main__':
    demo_dir_dict()
