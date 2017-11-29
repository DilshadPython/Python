import os
# getcwd Return a string representing the current working directory
print(os.getcwd())
print('\n')

print('--'*30)
print(os, '<<<')

h = 42
if h > 50:
    print('That is not true')
else:
    if h > 20:
        print('Yes that is correct h grater than 20')
    else:
        print('No that is not true')
