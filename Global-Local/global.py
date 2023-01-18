# We create a varable which is global to the program 
# can get access to it inside or outside the program

# The function has to be created before the global var to get access to it.
def your_name():
	print(language)

def get_number():
	print(number)

# global varable
name = 'Dilshad'
language = 'Python'

number = 123


print('Access general: ', name)
print('General: ', number)

print('Access from function: ')
your_name()
get_number()