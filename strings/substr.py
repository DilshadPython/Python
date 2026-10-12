import sys
import os


def reproducesString(input):
    alpha = []
    text = str(input('Enter a test: '))
    for i in str(text):
        if i == 'a' or 'A':
            return False
        elif i == 'e' or 'E':
            return False
        elif i == 'i' or 'I':
            return False
        elif i == 'o' or 'O':
            return False
        elif i == 'u' or 'U':
            return False
        else:
            print(str(i))

    return print(text)

reproducesString(input)
