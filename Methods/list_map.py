

temperatures = [
    ('Mosccow', -16),
    ('Warsawa', -9),
    ('New Yourk', 13),
    ('Qairo', 22),
    ('Dubai', 25),
    ('Erbil', 18),
    ('London', 12),
    ('Rom', 15),
    ('Paris', 14),
]

convert_to_function = lambda data: (data[0], (9 / 5) * data[1] + 32)

print(list(map(convert_to_function, temperatures)))
