import sys
import os


def reproducesString(input):
    alpha = []
    text = str(input('Enter a test: '))
    for i in range(str(text)):
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
            return print(str(i))

    # return print(testme)

reproducesString(input)
