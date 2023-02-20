import yaml

obj = (
    [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
    [
        {
            'a': 'Alpha',
            'b': 'Barbara',
            'c': 'Charly',
            'd': 'David',
            'e': 'Ela',
            'f': 'Flask',
            'g': 'Google',
            'h': 'Henry',
            'i': 'Inga',
            'j': 'Jack',
            'k': 'Kilo',
        },
        5, 22, 33, 44, 55, 11, 66, 77, 88
    ],
    {
        'a': [1, 2, 3, 4, 5],
        'b': ['Flask', 'Django', 'Python', 'CSS', 'JS'],
        'c': (33, 22, 11, 10, 44)
    }
)
print(yaml.dump(obj, default_flow_style=False))
