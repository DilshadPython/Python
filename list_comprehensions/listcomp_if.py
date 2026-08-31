"""
Demonstrates multi-condition filtering and tuple pair building with comprehensions.
"""

def demo_multi_condition_comp():
    # Filter even numbers from 1 to 102
    even_numbers = [x for x in range(1, 103) if x % 2 == 0]

    sentence = (
        'Hello welcome to the party next week on '
        'Wednesday at 18:30 in London'
    )
    words = sentence.split()
    word_lengths = [(word, len(word)) for word in words]

    print(f'Count of even numbers: {len(even_numbers)}')
    print('Word length pairs (first 4):', word_lengths[:4])

    return even_numbers, word_lengths

if __name__ == '__main__':
    demo_multi_condition_comp()
