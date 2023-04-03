import sys


def duplicate(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    num = x * 2
    return num


if __name__ == '__main__':
    new_num = sys.argv[1]
    duplicate_num = input(duplicate(new_num))
    print('The value of {0} is {1}'.format(new_num, duplicate_num))
