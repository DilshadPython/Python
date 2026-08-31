"""
Demonstrates list copy(), sub-slicing, list insertion, and index inspection.
"""

def demo_list_operations():
    languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']
    
    # Shallow copy of list
    lang_copy = languages.copy()
    print('Copied list:', lang_copy)
    print('Slice [1:3]:', lang_copy[1:3])

    # Insert list as sub-element
    web_tech = ['Google', 'Microsoft', 'Apple']
    languages.insert(1, web_tech)
    print('After inserting list at index 1:', languages)

    # Retrieve index position
    js_index = languages.index('JavaScript')
    print('Index of "JavaScript":', js_index)

    return lang_copy, js_index

if __name__ == '__main__':
    demo_list_operations()
