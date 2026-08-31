"""
Demonstrates working with lists of dictionaries (structured records).
"""

def demo_employee_records():
    employees = [
        {'name': 'Dilshad', 'last_name': 'Abdulla', 'age': 44, 'languages': ['English', 'German', 'Kurdish', 'Arabic']},
        {'name': 'Adam', 'last_name': 'Smith', 'age': 50, 'languages': ['English', 'Swedish']},
        {'name': 'Victoria', 'last_name': 'John', 'age': 41, 'languages': ['English']}
    ]

    print('Employee count:', len(employees))
    for emp in employees:
        print(f"  {emp['name']} {emp['last_name']} ({emp['age']})")

    return employees

if __name__ == '__main__':
    demo_employee_records()
