"""
Demonstrates constructing dictionaries key-by-key and inspecting keys/values.
"""

def demo_build_dict():
    create_dict = {}

    create_dict['Hello'] = 219
    create_dict['Hi'] = 90
    create_dict['Hey'] = 1
    create_dict['Merci'] = 87

    keys_view = list(create_dict.keys())
    values_view = list(create_dict.values())

    print('Built dictionary:', create_dict)
    print('Keys:', keys_view)
    print('Values:', values_view)

    return create_dict, keys_view, values_view

if __name__ == '__main__':
    demo_build_dict()
