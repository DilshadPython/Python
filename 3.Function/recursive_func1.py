'''
n! = n * (n - 1) * (n - 2) & (n - 3) * ... * 1
n! = n * (n - 1)!
4! = 4 * 3 * 2 * 1
4! = 4 * 3!
This is very importantce Factorial or recursive function use for only Posative number or )
0!  = 1
'''

def factorial_recur(num):
    # num = input('Please enter a number: ')
    if num == 1:
        print('\n Before else: ', num)
        return 1
    else:
        print('\n After else: ', num)
        return num * factorial_recur(num - 1)

print('The results: ',factorial_recur(4))

'''
This is how it working:

factorial_recur(4)
return 4 * factorial_recur(3)   << 12
    return 3 * factorial_recur(2)  << 6
        return 2 * factorial_recur(1)  << 2
            return 1 
'''
