"""
Demonstrates element mutation via list comprehensions vs imperative loops.
"""

def demo_grade_boosting():
    grades = [22, 44, 55, 33, 77, 12, 85, 17]
    print('Original grades:', grades)

    # Imperative element mutation
    boosted_loop = grades.copy()
    for i in range(len(boosted_loop)):
        boosted_loop[i] += 8

    # Declarative list comprehension
    boosted_comp = [x + 8 for x in grades]

    print('Boosted via loop:', boosted_loop)
    print('Boosted via comprehension:', boosted_comp)

    return boosted_loop, boosted_comp

if __name__ == '__main__':
    demo_grade_boosting()
