# we create palindrome another way like in python itself
'''
It has O(word) basically linear running time  complexity as far as the number of letter in the string is concern
like radar, madam, dad, 404, 101
example radar, madam, dad, 101, 404. the function to check before we swap the word, is_palindrome()
'''
def is_palindrome(word):
    real_word = word
    # we will follow the swaping function as another way

    reversed_word = reverse(word)

    if real_word == reversed_word:
        # if is correct
        return True
    # else return
    return False

# O(N) linear running time where N is a number of letters in the string word N=len(word)
def reverse(data):
    # string into a list of characters
    data = list(data)

    start_index = 0

    end_index = len(data) - 1

    while start_index < end_index:

        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    # transform the list of letters into a string
    return ''.join(data)

if __name__ == '__main__':
    word = 'radar'
    print(is_palindrome(word))
    # or
    # print(is_palindrom('python'))


