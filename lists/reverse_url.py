"""
Demonstrates sequence reversal techniques: slicing vs reversed() built-in.
"""

def demo_reverse_url():
    myweb = 'https://google.co.uk'
    print('Original string:', myweb)

    # Slicing reversal creates a new string
    reversed_str = myweb[::-1]
    print('Reversed via [::-1]:', reversed_str)

    # reversed() returns a reverse iterator object
    rev_iterator = reversed(myweb)
    rev_list = list(reversed(myweb))
    rev_tuple = tuple(reversed(myweb))

    print('reversed() iterator:', rev_iterator)
    print('as list:', rev_list)
    print('as tuple:', rev_tuple)

    return reversed_str, rev_list

if __name__ == '__main__':
    demo_reverse_url()
