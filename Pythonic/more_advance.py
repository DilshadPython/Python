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
    # LBYL Non-Pythonic
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()
    #
    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # But EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.drive()
    except AttributeError as e:
        print(e)

    print()

obj_d = Duck()
quack_and_flay(obj_d)

obj_p = Person()
quack_and_flay(obj_p)