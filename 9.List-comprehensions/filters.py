students = [
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
        'languages': ['Norway', 'German', 'Italian', 'English']
    },
    {
        'name': 'Claudia',
        'last_name': 'Williams',
        'age': 41,
        'languages': ['English', 'Swedish', ]
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
]

def is_there(x):
    return x['languages'] == 'German'

languages = filter(is_there, students)

for lang in languages:
    print(lang['name'])
