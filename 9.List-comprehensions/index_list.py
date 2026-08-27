"""
Demonstrates index mapping and string analysis inside comprehensions.
"""

def demo_index_and_lengths():
    users = ['John', 'Mike', 'Claudia', 'George', 'Kim', 'Elena']

    # List of tuples containing positional index (1-based) and name
    indexed_users = [(idx + 1, name) for idx, name in enumerate(sorted(users))]
    print('Indexed & sorted users:', indexed_users)

    # Dictionary mapping name to character length
    name_lengths = {name: len(name) for name in users}
    print('Name character lengths:', name_lengths)

    return indexed_users, name_lengths

if __name__ == '__main__':
    demo_index_and_lengths()
