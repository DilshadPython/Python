"""
Demonstrates positional indexing during iteration using built-in enumerate().
"""

def demo_enumerate():
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    
    indexed_list = []
    print('Iterating with enumerate():')
    for index, fruit in enumerate(fruits, start=1):
        print(f'Item #{index}: {fruit}')
        indexed_list.append((index, fruit))

    return indexed_list

if __name__ == '__main__':
    demo_enumerate()
