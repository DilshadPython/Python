# Abstract Base Classes
 ## Abstruct class is kind of (model) for other classes to be defined. It is not desiged to 
 ## construct instance but can be subclasses by regular classes

 ## Abstruct classes can define an interface, or methods that must be implemented by its subclsses.

 # In abstruct class setter and getter cann't be instansiated:
    @abc.abstractmethod
    def set_val(self, input):
        ''' Set a value in the instance '''
        return

    @abc.abstractmethod
    def get_val(self):
        ''' Get and return a value from the instance '''
        return