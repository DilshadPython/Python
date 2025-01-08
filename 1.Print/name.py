# strip() remove the emptyspaces
# The title() capitalize first letter of fname and lname
# The end stop new line
fname = str(input('Enter first name: '))
lname = str(input('Enter last name: '))

remove_empty_space = '      world       '

print('Hello, ', remove_empty_space.strip(), ' in Python')

full_name = (fname + ' ' + lname).title()
print('Hi, ', full_name)
