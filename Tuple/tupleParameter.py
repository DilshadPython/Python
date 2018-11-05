def example(one, two, three, four, five):
    return one + two - three * four / five
# tuple know before the element hast *

collection = (6, 54, 8, 3, 7)

print(example(*collection))


# **more is like **kwargs
def example2(**more):
    print(more)

person1 = {'Alan': 32, 'Fabio': 29, 'Amanda': 28}

example2(**person1)
