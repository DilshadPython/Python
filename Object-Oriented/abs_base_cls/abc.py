'''
The abc module module enables the reaction of abstract base class
'''
import abc

'''
Create abstract class which can't create an object to access subclass
The abstract class not designed to contruct instance but can be subclassed 
by regular classes
'''
class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, input):
        ''' Set a value in the instance '''
        return

    @abc.abstractmethod
    def get_val(self):
        ''' Get and return a value from the instance '''
        return


class MyClass(GetterSetter):

    ''' setter func '''

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

'''
You can't instationate the Abstract class only the Subclass
'''
obj = MyClass()
print(obj)
