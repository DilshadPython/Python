"""
Demonstrates sequence unpacking vs element indexing on structured tuples.
"""

def demo_tuple_unpacking():
    student = (29, 814747, 'Dilshad Abdulla', 'Python Developer')
    age, st_id, fullname, title = student

    print(f'Student: {fullname}, Age: {age}, ID: {st_id}, Title: {title}')

    player = (7, 814747, 'David Beckham', 'Manchester United')  # Fixed typo
    number, player_id, name, team = player

    print(f'Player: {name}, No: {number}, Team: {team}')

    return student, player

if __name__ == '__main__':
    demo_tuple_unpacking()
