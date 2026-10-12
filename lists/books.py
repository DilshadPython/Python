"""
Demonstrates managing a collection of books using Python list operations.
"""

def manage_books():
    books = ['Python Crash Course', 'Clean Code', 'Design Patterns']
    print('Initial books:', books)

    # Adding a book
    books.append('Fluent Python')
    print('After append:', books)

    # Sorting alphabetically
    books.sort()
    print('Alphabetical order:', books)

    # Checking existence
    has_clean_code = 'Clean Code' in books
    print('Is "Clean Code" in collection?:', has_clean_code)

    return books

if __name__ == '__main__':
    manage_books()
