"""
Demonstrates empty tuple initialization and sub-slicing.
"""

try:
    input = raw_input
except NameError:
    pass

def demo_storage_tuple(interactive=False):
    storage = ()
    is_empty = len(storage) == 0
    print('Is storage empty?:', is_empty)

    if interactive:
        input('\nPlease press Enter to continue...')

    storage = ('Arsenal', 'Southampton', 'Man Utd', 'Liverpool',
               'Man City', 55.687, 5, 'Chelsea', -12, 'Tottenham')

    print('Full storage slice:', storage[:])
    return is_empty, storage

if __name__ == '__main__':
    demo_storage_tuple()
