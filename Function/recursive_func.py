'''
Factorials
# 5! = 5 * 4 * 3 * 2 *1
# 5! = 5 * 4!
This is how it working:

factorial_recur(4)
return 4 * factorial_recur(3)   << 12
    return 3 * factorial_recur(2)  << 6
        return 2 * factorial_recur(1)  << 2
            return 1
'''
def factorial_recur(num):
    # num = input('Please enter a number: ')
    if num == 1: # if num <= 1: te smae
        print('\nBefore else: ', num)
        return 1
    else:
        print('After else : ', num)
        return num * factorial_recur(num - 1)

print(factorial_recur(num=int(input('Enter a factoril number: '))))
