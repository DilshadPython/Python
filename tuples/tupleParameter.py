"""
Demonstrates tuple parameter unpacking (*args) and dict unpacking (**kwargs).
"""

def calculate(one, two, three, four, five):
    return one + two - three * four / five

def print_kwargs(**kwargs):
    print('Keyword arguments received:', kwargs)
    return kwargs

def demo_star_unpacking():
    collection = (6, 54, 8, 3, 7)

    # Unpack tuple as positional function arguments
    result = calculate(*collection)
    print('Result of calculate(*collection):', result)

    person1 = {'Alan': 32, 'Fabio': 29, 'Amanda': 28}
    kw_res = print_kwargs(**person1)

    return result, kw_res

if __name__ == '__main__':
    demo_star_unpacking()
