"""
Demonstrates the fundamental difference between identity 'is' and equality '=='.
"""

def demo_identity_vs_equality():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a  # c references the exact same list object as a

    print('a:', a)
    print('b:', b)
    print('c:', c)
    print()

    # Equality check compares list contents
    print('a == b (Value equality):', a == b)  # True
    print('a == c (Value equality):', a == c)  # True

    # Identity check compares memory addresses (id())
    print('a is b (Identity check):', a is b)  # False (different objects in memory)
    print('a is c (Identity check):', a is c)  # True (same object memory reference)

    return (a == b, a is b, a is c)

if __name__ == '__main__':
    demo_identity_vs_equality()
