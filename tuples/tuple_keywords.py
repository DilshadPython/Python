"""
Demonstrates tuple variable reference assignment and dir() method inspection.
"""

def demo_tuple_references():
    tpl = ('Python', 'Java', 'PHP', 'JavaScript')
    ref_tpl = tpl

    # Both variables point to the same memory reference
    same_ref = tpl is ref_tpl
    print('tpl is ref_tpl:', same_ref)

    public_methods = [m for m in dir(tpl) if not m.startswith('_')]
    print('Tuple public methods:', public_methods)

    return same_ref, public_methods

if __name__ == '__main__':
    demo_tuple_references()
