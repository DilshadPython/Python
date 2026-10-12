"""
Demonstrates single-element tuple comma requirements and tuple instantiation.
"""

def demo_tuple_syntax():
    empty_tuple = ()

    # Note: ('a') is a string, not a tuple! Single element tuples MUST have a trailing comma: ('a',)
    not_a_tuple = ('a')
    single_element_tuple = ('a',)
    multi_element_tuple = ('a', 'b', 'c')

    print('empty_tuple type:', type(empty_tuple))
    print('("a") type:', type(not_a_tuple))
    print('("a",) type:', type(single_element_tuple))
    print('("a", "b", "c") type:', type(multi_element_tuple))

    return type(not_a_tuple), type(single_element_tuple), multi_element_tuple

if __name__ == '__main__':
    demo_tuple_syntax()
