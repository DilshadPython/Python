"""
Demonstrates complex nested filtering on list of dictionaries using comprehensions.
"""

def filter_students():
    students = [
        {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44, 'languages': ['English', 'German', 'Kurdish']},
        {'name': 'Adam', 'last_name': 'Smith', 'age': 50, 'languages': ['German']},
        {'name': 'Victoria', 'last_name': 'John', 'age': 41, 'languages': ['Italian', 'English', 'Greek']},
        {'name': 'Sophia', 'last_name': 'Loren', 'age': 28, 'languages': ['English', 'French']}
    ]

    # Filter students older than 40
    over_40 = [s['name'] for s in students if s['age'] > 40]
    print('Students over 40:', over_40)

    # Filter students who speak English
    english_speakers = [
        s['name'] for s in students
        if isinstance(s['languages'], list) and 'English' in s['languages']
    ]
    print('English speaking students:', english_speakers)

    return over_40, english_speakers

if __name__ == '__main__':
    filter_students()
