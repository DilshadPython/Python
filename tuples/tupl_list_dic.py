"""
Demonstrates text word frequency analysis using dictionaries and sorting via tuples.
"""

import os

# Cross-version input shim
try:
    input = raw_input
except NameError:
    pass

def process_file_words(file_name=None):
    if not file_name:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(dir_path, 'sname.txt')

    w_dic = dict()
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            words = line.split()
            for word in words:
                w_dic[word] = w_dic.get(word, 0) + 1

    # Convert dict items to sorted tuple list (sort by frequency count descending)
    sorted_words = sorted([(count, word) for word, count in w_dic.items()], reverse=True)
    print('Top 5 most frequent words:', sorted_words[:5])

    return sorted_words

if __name__ == '__main__':
    process_file_words()
