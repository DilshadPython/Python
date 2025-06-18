employes = [
    {
        'name': 'Dilshad',
        'last_name': 'Abdulla',
        'age': 44,
        'languages': ['English', 'German', 'Kurdish', 'Arabic']
    },
    {
        'name': 'Adam',
        'last_name': 'Smith',
        'age': 50,
        'languages': ['English', 'Swdish', ]
    },
    {
        'name': 'Wictoria',
        'last_name': 'John',
        'age': 41,
        'languages': 'English',
    },
    {
        'name': 'Kim',
        'last_name': 'Jason',
        'age': 37,
        'languages': ['English', 'German', 'Italian']
    }
]

for employe in employes:
    print(employe['name'], employe['last_name'], employe['age'], employe['languages'], sep=', ')