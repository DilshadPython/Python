"""
Demonstrates dictionary comprehension syntax: {key_expr: value_expr for item in iterable}.
"""

def demo_dict_comprehension():
    users = ['John', 'Mike', 'Claudia', 'George', 'Kim', 'Elena']

    # Map each sorted username to a city
    user_city_map = {user: 'Berlin' for user in sorted(users)}
    print('Dictionary comprehension output:', user_city_map)
    return user_city_map

if __name__ == '__main__':
    demo_dict_comprehension()
