"""
Demonstrates string extraction and regex/parsing using list comprehensions.
"""

def filter_movies():
    movies = [
        'Are We There Yet? (2005)',
        'Bachelor Mother (1939)',
        'Carnival Night (1956)',
        'Four Rooms (1995)',
        'Get Crazy (1983)',
        'Ghostbusters II (1989)',
        'The Gold Rush (1925)',
        'The Hudsucker Proxy (1994)',
        "New Year's Day (2001)",
        'Party Party (1983)',
        'Radio Days (1987)',
        'Trading Places (1983)',
        'After the Thin Man (1936)',
        'Better Luck Tomorrow (2002)',
        'Dhoom (2004)',
        'Entrapment (1999)',
        'The Godfather Part II (1974)',
        'Little Caesar (1931)'
    ]

    # Extract movies released in the 1980s
    movies_80s = [m for m in movies if '(198' in m]
    print('1980s movies:', movies_80s)

    return movies_80s

if __name__ == '__main__':
    filter_movies()
