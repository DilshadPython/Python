

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  -9, -8, -7, -6, -5, -4, -3, -2, -1

# list[start:end:step]

print(' ', num, ' ******  just print num')

print('Index zero: ', num[0], ' ****** [0] ')

print('Index 4 is: ', num[4], ' ****** [4]')

print('Index -2 is: ', num[-2], ' ****** [-2]')

print('Index -6 is: ', num[-6], ' ****** [-6]')

print('Index from 1 to 5 is: ', num[:5], ' ****** [:5] ')

print('############################################')

print('All Index: ', num[:], ' ****** [:] ')

print('Index from 3 to the end : ', num[3:], ' ****** [3:] ')

print('Index between -6 to -2: ', num[-6:-2], ' ****** [-2:-3]')

print('Index start from 2 to 7: ', num[2:7], ' ****** [2:7]')

print('Index from right -5 to the beginning left: ', num[:-5], ' ****** [:-5]')

print('Index from right -2 to the end right: ', num[-2:], ' ****** [-2:]')

print('Index start from 2 each time -2 to the end: ', num[2:-2:2], ' ****** [2:-2:2]')

print('Index start from 1 each time -2 to the 3 index: ', num[1:-2:3], ' ****** [1:-2:3]')

print('Index >>: ', num[-1:2:-1], ' ****** [-1:2:-1]')

print('Index ==>>: ', num[-2:1:-1], ' ****** [-2:1:-2]')

print('Index start from -1 right to the beginning left -->>: ', num[::-1], ' ****** [::-1]')
