"""
Demonstrates chaining update operations and dictionary length inspection.
"""

def demo_update_func():
    details = {
        'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44,
        'languages': ['English', 'German', 'Kurdish', 'Arabic']
    }

    details.update({
        'email': 'dilshad.abdulla@gmail.com',
        'age': 45,
        'website': 'https://dilshadabdulla.net'
    })

    del details['website']

    print('Final details count:', len(details))
    print('Keys:', list(details.keys()))

    return details

if __name__ == '__main__':
    demo_update_func()
