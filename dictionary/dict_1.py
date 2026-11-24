"""
Demonstrates dictionary creation, key addition, and value indexing.
"""

def demo_dict_mapping():
    details = {
        'name': 'Dilshad',
        'last_name': 'Abdulla',
        'age': 44,
        'languages': ['English', 'German', 'Kurdish', 'Arabic']
    }

    # Add email key
    details['email'] = 'dilshad.abdulla@gmail.com'

    print('Name:', details['name'])
    print('Last name:', details['last_name'])
    print('First letter of last name:', details['last_name'][0])

    return details

if __name__ == '__main__':
    demo_dict_mapping()
