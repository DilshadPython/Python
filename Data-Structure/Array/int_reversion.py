'''
# Example 568724 = 427865
reversed_int = 0
n = 1234

while n > 0: {
    reminder = n % 10
    n = n / 10
    reversed_int = reversed_int * 10 + reminder
}

Notice 1:
n = 123
reminder = 123 % 10 = 3
n = 12
reversed_int = 4 * 10 + 3 = 43

notice 2:
n = 12
remainder = 12 % 10 = 2
n = 1
reversed_int = 3 * 10 + 2 = 32

notice 3:
remainder = 1 % 10 = 1
n = 0
reversed_int = 32 * 10 + 1 = 321

Notice 4:
No more interations because n > 0 is not true
Solution: 321
'''

# We select last digit in every interation, to do that we use modular operator and the last digit is the reminder
# when dividing by 10

def reverse_integer(num):
    reversed_int = 0

    while num > 0:
        remainder = num % 10
        reversed_int = reversed_int * 10 + remainder
        # 15 / 10 = 1.5 but 15 // 10 = 1 <== (return int no float)
        num = num // 10

    return reversed_int

# this is the main of the function example num = 76583
if __name__ == '__main__':
    num = int(input('Enter a number: '))
    print(reverse_integer(num))
