print('Hello Dilmac')

msg = 'Welcome to python >> '

# concatinate
var = ' are you ready to learning?'

print(msg + var)
print('\n')

# using boolian
print(msg.upper() + var.upper())
print('\n')

print('Show all as lower char:')
print(msg.lower() + var)
print('\n')


print('If both correct return True if no check the output')
print(msg.isupper())
print('\n')

print('Check one:')
print(var.islower())
print('\n')

print('If both correct return False if no check the output')
print(msg.islower())
print('\n')

print('If both correct return 1 if no check the output')
print(msg.islower() + var.islower())
print('\n')

print('Change all to lower and check is done display True')
print(var.lower().islower())
print('\n')

print('Change all to upper and check is done display True')
print(var.upper().isupper())
print('\n')
