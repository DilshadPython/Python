"""
Demonstrates empty dictionary creation and method listing.
"""

def demo_lib_dict():
    new_dict = {}
    methods = [m for m in dir(new_dict) if not m.startswith('_')]
    print('Available dict methods:', methods)
    return methods

if __name__ == '__main__':
    demo_lib_dict()
