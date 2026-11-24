"""
Demonstrates filtering and transforming nested dictionary structures using list comprehensions.
"""

def demo_nested_dict_filtering():
    students = [
        {'name': 'Jim', 'last_name': 'Donald', 'age': 40, 'languages': ['English']},
        {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44, 'languages': ['English', 'German', 'Kurdish']},
        {'name': 'Adam', 'last_name': 'Smith', 'age': 50, 'languages': ['German']},
        {'name': 'Victoria', 'last_name': 'John', 'age': 41, 'languages': ['Italian', 'English', 'Greek']}
    ]

    # Extract full names of students older than 40
    senior_students = [f"{s['name']} {s['last_name']}" for s in students if s['age'] >= 40]
    print('Students aged >= 40:', senior_students)

    return senior_students

if __name__ == '__main__':
    demo_nested_dict_filtering()
