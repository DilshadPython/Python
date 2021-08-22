'''
This is how it working:

factorial_recur(-7)
return -7 * factorial_recur(6)   << -36
    return -6 * factorial_recur(5)  << 6
        return -5 * factorial_recur(4)  << 2
            return -4 * factorial_recur(3)
                return -3 * factorial_recur(2)
                    return -2 * factorial_recur(1)
                        return 1
'''
def factorial_recur(num):
    # num = input('Please enter a number: ')
    if num == 1:
        print('\nBefore else: ', num)
        return 1
    else:
        print(' After else : ', num)
        return num * factorial_recur(num + 1)

print(factorial_recur(-7))
