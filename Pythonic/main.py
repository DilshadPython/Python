# Duck typing and Easier to ask forgiveness than permission (EAFP)

class Duck:

    def quack(self):
        print('Quack!, quack')

    def fly(self):
        print('Flap!, Flap')

class Person:

    def quack(self):
        print('I am Quacking like a Duck!')

    def fly(self):
        print('I am Flapping my Arms!')


def quack_and_flay(thing):
    # this way
    thing.quack()
    thing.fly()

    # or this way
    # Not Duck Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    print()

obj_d = Duck()
quack_and_flay(obj_d)

obj_p = Person()
quack_and_flay(obj_p)