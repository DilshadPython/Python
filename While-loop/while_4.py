a = 1
while a % 7 != 0:
    print(a,)
    if a % 2 == 0:
        print('0')
        print(a,)   # added for test
    elif a == 2:
        print(a,)
        print('X')
        print(a,)   # added for test
    a = a + 1
print('\n***********')
print(1 % 2 == 0)
print(2 % 2) #== 0
print(2 % 2 == 0)
