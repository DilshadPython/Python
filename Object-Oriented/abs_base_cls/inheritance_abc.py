'''
The abc module module enables the reaction of abstract base class
'''
import abc

'''
Create abstract class which can't create an object to access subclass
The abstract class not designed to contruct instance but can be subclassed
by regular classes
'''

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        ''' Set a value in the instance '''
        self.val = value
        return

    def get_val(self):
        ''' Get and return a value from the instance '''
        return self.val

    @abc.abstractmethod
    def show_docs(self):
        return

'''
We can't instanceated abstruct class very important

myob = GetSetParent()
print(' myob', myob)
Display an error
myob = GetSetParent()
TypeError: GetSetParent.__init__() missing 1 required positional argument: 'value'
'''

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def show_docs(self):
        print('\nGetSetInt object ({0}), only accepts integer values'.format(id(self)))


class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)


    def show_docs(self):
        print('\nGetSetList object, len {0} history of values set'.format(
            len(self.vallist)))

obj = GetSetInt(9)

obj.set_val(7)
print(obj.get_val())
obj.show_docs()

print('\n ############################################################## \n')
print('\nHere we set the set_val 4 times (6, 99, 3, 49 ) the get_val will take the last one which is overloading \
       the other valuse and return the last one which is 49\n')
gsl = GetSetList(6)
gsl.set_val(99)
gsl.set_val(3)
gsl.set_val(49)

print(gsl.get_val())
print('\n')
print(gsl.get_vals())
gsl.show_docs()
