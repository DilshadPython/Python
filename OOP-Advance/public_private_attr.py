class Monitor:
    # this is public var
    instance_count = 0

    # this is private private not be subclassed or child class
    __mangled_name = 'no privacy'

    def __init__(self, value):
        # _attributeval means internal use only
        self._attributeval = value
        Monitor.instance_count += 1

    @property
    def var(self):
        print('Getting the "var" attribute')
        return self._attributeval

    @var.setter
    def var(self, value):
        print('Setting the "var" attribute')
        self._attributeval = value

    @var.deleter
    def var(self):
        print('Deleting the "var" attribute')
        self._attributeval = None


obj = Monitor(18)

print(obj._attributeval, ' << private attribute internal use only')
print(obj._Monitor__mangled_name, ' << private attribute Can access only through class name with single underscore  ')
print(obj.__mangled_name, ' << private attribute Can not be accessed without class name. Error  ')

