'''
What is Palindrome
It's a word or a number when you read the same in both way forward and backword
like madam, mom, dad, 404, 101, radar, poop, 4004, 330033, but if the length is different it's not palindrome
'''
def palindrom(word):

    if word == word[::-1]:
        print(word)
        return True

    return False


if __name__ == '__main__':
    word = input('Enter a word or a numbers like above: ')
    print(palindrom(word))
