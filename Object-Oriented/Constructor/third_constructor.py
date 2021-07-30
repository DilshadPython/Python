'''
In this example we defined the number in __init__ method we can pass the number
directly in the obj = Number(3), we define two argument self and number
'''


class Number(object):
    def __init__(self, number):
        print('Call __init__ automatically from instance obj')
        try:
            self.num = int(number)
        except ValueError:
            number = 0
        self.num = number

    def increament(self):
        self.num = self.num + 1


obj = Number(3)
obj.increament()
obj.increament()

print(obj.num)

print('\nThe result is 0 because we set number to 0 if the argument is string:\n')
# We pass a string instead of int or bad argunment
obj = Number('Welcome')

print(obj.num)
