"""
Demonstrates iterating over list elements using standard 'for' loops.
"""

def iterate_list():
    languages = ['Python', 'JavaScript', 'C++', 'Rust']
    output = []
    
    for lang in languages:
        msg = f'Language: {lang}'
        print(msg)
        output.append(msg)

    return output

if __name__ == '__main__':
    iterate_list()
