hight = 22.367453
width = 778.98763

print(f'{hight}', ' and ', f'{width}')

'''
Now we replace the float to two dight after dot or one dight or 3 dight
'''
print('{}'.format(hight))
print('{}'.format(width))

print('\n##########')
print('{:}'.format(width))
print('{:}'.format(hight))

print('\n########## << :f ')
print('{:f}'.format(width))
print('{:f}'.format(hight))

print('\n############ << :.1f ')
print('{:.1f}'.format(width))
print('{:.1f}'.format(hight))

print('\n############ << :.2f')
print('{:.2f}'.format(width))
print('{:.2f}'.format(hight))

print('\n############ << :.3f ')
print('{:.3f}'.format(width))
print('{:.3f}'.format(hight))


print('\n############ << .2f')
number = 232.45678231
print(format(number, '.2f'))

print('==========\n')
msg = f'To multiply tow number in the string { 4 * 7} '
print(msg)
