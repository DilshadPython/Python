# We create a variable which is global to the program
# can get access to it inside or outside the program

# The function created to get access to the global.
def your_name():
	print(language)

def get_number():
	print(number)

# global variable
name = 'Dilshad'
language = 'Python'

number = 123

# Notice: the func can get access to global var from both way created func before
# or after global variable, it works from both way

print('Access general: ', name)
print('General: ', number)

print('Access from function: ')
your_name()
get_number()