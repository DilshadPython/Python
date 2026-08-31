"""
Demonstrates dictionary update() method and key deletion with del.
"""

def demo_dict_update():
    account = {
        'fname': 'Dilshad', 'lname': 'Abdulla',
        'address': '16 Glebe Road', 'date_of_birth': '28/03/1973', 'age': 41
    }
    print('Original account:', account)

    # Update account details in-place
    account.update({
        'fname': 'Azad', 'lname': 'Abdulla',
        'address': '206 Valence Road', 'age': 39
    })
    print('Updated account:', account)

    # Delete key
    del account['date_of_birth']
    print('Account after deleting date_of_birth:', account)

    return account

if __name__ == '__main__':
    demo_dict_update()
