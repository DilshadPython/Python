"""
Demonstrates adding elements using append() and insert() methods.
"""

def demo_add_methods():
    languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']
    print('Initial languages:', languages)

    # Append to end
    languages.append('C language')
    print('After append("C language"):', languages)

    # Insert at index 0 (front of list)
    languages.insert(0, 'Java')
    print('After insert(0, "Java"):', languages)

    # Insert at index 3
    languages.insert(3, 'Go')
    print('After insert(3, "Go"):', languages)

    return languages

if __name__ == '__main__':
    demo_add_methods()
