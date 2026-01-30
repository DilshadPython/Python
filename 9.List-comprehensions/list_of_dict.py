students = [
    {
        'name': 'Jim',
        'last_name': 'Donald',
        'age': 40,
        'languages': 'English',
    },
    {
        'name': 'Dilshad',
        'last_name': 'Abdulla',
        'age': 44,
        'languages': ['English', 'German', 'Kurdish']
    },
    {
        'name': 'Adam',
        'last_name': 'Smith',
        'age': 50,
        'languages': 'German',
    },
    {
        'name': 'Wictoria',
        'last_name': 'John',
        'age': 41,
        'languages': ['Italian', 'English', 'Greece']
    },
    {
        'name': 'Kim',
        'last_name': 'Jason',
        'age': 37,
        'languages': 'English',
    },
    {
        'name': 'Claudia',
        'last_name': 'Williams',
        'age': 41,
        'languages': ['English', 'Swedish', ]
    },
    {
        'name': 'Monika',
        'last_name': 'Liam',
        'age': 40,
        'languages': 'English',
    },
    {
        'name': 'Susanee',
        'last_name': 'George',
        'age': 40,
        'languages': ['English', 'Holland', ]
    },
    {
        'name': 'Tomas',
        'last_name': 'Paul',
        'age': 40,
        'languages': 'German',
    },
    {
        'name': 'Lima',
        'last_name': 'Wills',
        'age': 40,
        'languages': 'English',
    },
]
print()
names = [
    student['name'] for student in students if student['languages'] == 'English'
]

print('\t', names)

print()
name_a = list(map(lambda x: x['last_name'], students))
print('\t', name_a)

print()
name_a = list(map(lambda x: x, students))
print('\t', name_a[0:2])

print()
for name in sorted(names):
    print('\t', name)
