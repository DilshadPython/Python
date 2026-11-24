"""
Demonstrates joining string elements of a list into a single delimited string.
"""

def demo_join():
    words = ['Python', 'is', 'a', 'versatile', 'language']
    print('List of words:', words)

    # Join with space separator
    sentence = ' '.join(words)
    print('Joined with space:', sentence)

    # Join with comma separator
    csv_string = ', '.join(words)
    print('Joined with comma:', csv_string)

    return sentence, csv_string

if __name__ == '__main__':
    demo_join()
