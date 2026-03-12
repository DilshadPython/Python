'''
What is Palindrome
It's a word or a number when you read the same in both way forward and backword
like madam, mom, dad, 404, 101, radar
'''
def palindrom(word):
    if word == word[::-1]:
        print(word)
        return True
    print(word)
    return False


if __name__ == '__main__':
    print(palindrom('madam'))
    # or
    # print(palindrom('hello'))


