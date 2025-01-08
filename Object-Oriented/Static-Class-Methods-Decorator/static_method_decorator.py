'''
This is shows how the instance methods work
Static method requires no argument and does not work with
class or instance, but stull belongs in the class cod
'''

class InstanceCounter(object):
    """docstring for InstanceCount"""
    count = 0

    def __init__(self, val):
        # filterint() required an integer
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    '''
    This is the static method to explain better don't use self use
    directly the argument which is value called static method not
    bound method.
    Static method is not Bound method
    '''
    print('Decorator is a processor that modifies a function')

    @staticmethod
    def filterint(value):
        # here if the value is not an integer than return 0
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(107)
b = InstanceCounter(22)
c = InstanceCounter(81)
d = InstanceCounter('Dilshad')

for obj in (a, b, c, d):
    print('Value of obj {}'.format(obj.val))
