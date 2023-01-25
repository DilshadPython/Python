'''
'''


class Animal(object):
    """docstring for Animal"""

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} is eating {1}'.format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('{0} goes after the {1}'.format(self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):
    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print('{0} purrs '.format(self.name))


for obj in (Dog('Raffi'), Cat('Smikey'), Cat('Ali'), Dog('Tilly')):
    obj.show_affection()
