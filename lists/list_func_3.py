"""
Demonstrates membership operators (in / not in), enumerate(), and string join.
"""

def demo_membership_and_iter():
    languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']

    has_ruby = 'Ruby' in languages
    has_postgres = 'Postgres' in languages

    print('Is "Ruby" in languages?:', has_ruby)
    print('Is "Postgres" in languages?:', has_postgres)
    print()

    print('Enumerating languages:')
    for index, lang in enumerate(languages):
        print(f'  [{index}] {lang}')

    formatted_str = ', '.join(languages)
    print('\nJoined string:', formatted_str)

    return has_ruby, has_postgres, formatted_str

if __name__ == '__main__':
    demo_membership_and_iter()
