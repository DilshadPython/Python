class Monitor:
    def __init__(self, value):
        self.attributeval = value

    @property
    def var(self):
        print('Getting the "var" attribute')
        return self.attributeval

    @var.setter
    def var(self, value):
        print('Setting the "var" attribute')
        self.attributeval = value

    @var.deleter
    def var(self):
        print('Deleting the "var" attribute')
        self.value = 0 # or you can say self.value = None


obj1 = Monitor(18)
obj2 = Monitor(77)

print(obj1.var, obj2.var)

obj1.var = 301
obj2.var = 444

print(obj1.var, ' << first object')
print(obj2.var, ' << second object')

print('We call delete func to delete obj1.var which is 301')
del obj1.var

print(obj1.var, ' << deleted obj1.var')

print(obj2.var, ' << keep obj2.var')
