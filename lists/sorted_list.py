"""
Demonstrates text splitting, word sorting, and frequency counting using a dict.
"""

def analyze_sentence():
    sentence = (
        'To better understand how functions work, let us create one. '
        'To type this program into the file editor and save it.'
    )

    # Split sentence into list of word tokens
    words = sentence.split()
    words_sorted = sorted(words)
    print('Sorted words:', words_sorted)

    # Word count dictionary
    word_counts = {}
    for word in words_sorted:
        word_counts[word] = word_counts.get(word, 0) + 1

    print('\nWord frequencies:')
    for word, count in word_counts.items():
        print(f'  {word:<15}: {count}')

    return words_sorted, word_counts

if __name__ == '__main__':
    analyze_sentence()
