import sys


def duplicate(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    num = x * 2
    return num


def doublelines(filename):
    with open(filename) as fname:
        new_list = [str(duplicate(int(num))) for num in fname]
    with open(filename, 'w') as fname:
        fname.write('\n'.join(new_list))


if __name__ == '__main__':
    new_num = sys.argv[1]
    duplicate_num = input(duplicate(new_num))
    print('The value of {0} is {1}'.format(new_num, duplicate_num))
