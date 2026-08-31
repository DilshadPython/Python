"""
Demonstrates word frequency counting in files using dictionaries and sorting.
"""

import os

# Cross-version input shim
try:
    input = raw_input
except NameError:
    pass

def count_file_words(file_name=None):
    if not file_name:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(dir_path, 'sname.txt')

    word_counts = {}
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    # Sort word counts by frequency descending
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    print('Top 5 words:', sorted_word_counts[:5])

    return word_counts, sorted_word_counts

if __name__ == '__main__':
    count_file_words()
