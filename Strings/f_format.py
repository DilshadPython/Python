hight = 22.367453
width = 778.98763

print(f'{hight}', ' and ', f'{width}' )

'''
Now we replace the float to two dight after dot or one dight or 3 dight
'''
print('{}'.format(hight))
print('{}'.format(width))

print('##########')
print('{:}'.format(width))
print('{:}'.format(hight))

print('##########')
print('{:f}'.format(width))
print('{:f}'.format(hight))

print('############')

print('{:.1f}'.format(width))
print('{:.1f}'.format(hight))

print('############')
print('{:.2f}'.format(width))
print('{:.2f}'.format(hight))

print('############')
print('{:.3f}'.format(width))
print('{:.3f}'.format(hight))


print('############')
number = 232.45678231
print(format(number, '.2f'))
