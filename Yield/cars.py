def main():
    n = int(input('Enter a n: '))
    for x in fly(n):
        print(x)
'''
Yield use for very high of number for example return 100 # one in the time
when we enter 1000 000 the memory is get hot yield print 1000 000 # start from
 0 until reach to 1000000 use for very high number and very fast but still take
 more time to print one 1000 000 in the one line.
 '''
def fly(n):
    for i in range(n):
        yield '#' * i

if __name__ == '__main__':
    main()