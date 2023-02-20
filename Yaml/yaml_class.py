import yaml


class Student:

    class_var = 12

    def __init__(self, val):
        self.val = val

    def increament(self):
        self.val += 1


obj = Student(8)
obj.increament()
obj.increament()
obj.increament()

with open('obj.yaml', 'w') as fhandler:
    yaml.dump(obj, fhandler)


with open('obj.yaml') as fhandler:
    inst = yaml.load(fhandler, Loader=yaml.Loader)

print(inst.val)
