"""
Demonstrates contrast between generator functions, generator expressions, and list comprehensions.
"""

def gen_func(numbers):
    for x in numbers:
        yield x * x

def demo_generators():
    numbers = [2, 3, 5, 7, 1, 8]
    gen_obj = gen_func(numbers)
    gen_list = list(gen_obj)
    print('Generator function values:', gen_list)

    # Generator expression (parentheses instead of brackets)
    gen_expr = (x * x for x in range(10))
    gen_expr_values = list(gen_expr)
    print('Generator expression values:', gen_expr_values)

    return gen_list, gen_expr_values

if __name__ == '__main__':
    demo_generators()
