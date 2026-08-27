"""
Demonstrates constructing lists of dictionaries using list comprehensions.
"""

def demo_dict_list_creation():
    users = ['John', 'Mike', 'Claudia', 'George', 'Kim', 'Elena']

    # Imperative approach with for-loop
    user_dicts_loop = []
    for user in users:
        user_dicts_loop.append({'name': user})

    # Declarative list comprehension approach
    user_dicts_comp = [{'name': user, 'city': 'Brentwood'} for user in users]

    # Comprehension with sorted iterable
    sorted_user_dicts = [{'name': user, 'city': 'Brentwood'} for user in sorted(users)]

    print('Loop approach:', user_dicts_loop[:2])
    print('Comprehension approach:', user_dicts_comp[:2])
    print('Sorted comprehension approach:', sorted_user_dicts[:2])

    return user_dicts_loop, user_dicts_comp, sorted_user_dicts

if __name__ == '__main__':
    demo_dict_list_creation()
