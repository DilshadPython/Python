'''
Notice if you define var in the class it's not Encapsulation data 
it will be Class data 
'''

class Monitor:
    def __init__(self, maximum):
        self.max_size = maximum
        self.storedlist = []

    def push(self, num):
        self.storedlist.append(num)
        if len(self.storedlist) > self.max_size:
            self.storedlist.pop(0)

    def get_list(self):
        return self.storedlist


# We set the size of first obj to 4 the maximum size is 4 monitors
obj = Monitor(4)
# The second obj1 size is 2 can get 2 monitors
obj1 = Monitor(2)


obj.push('Samsung')
obj.push('Nokia')
obj.push('Lenovo')
obj.push('HP')
obj.push('LG Ultra')


obj1.push('Samsung')
obj1.push('Nokia')
obj1.push('Lenovo')
obj1.push('HP')
obj1.push('LG Ultra')

print(obj.get_list())
print(obj1.get_list())
