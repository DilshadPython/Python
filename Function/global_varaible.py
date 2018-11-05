# global variables
x = 'Dilshad'


def func():
    y = 'Abdulla'
    print(y)

func()
print(x, ' is my first name')  # This is global variable able to print
# print(y, ' is my last name'	)	# can't access to local vaiable


a = 5


def call():
    b = 10
    print(b)
    print(a)
    c = a + 3
    print(c)

call()
