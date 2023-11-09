class SumList:

    def __init__(self, listy):
        self.mylist = listy

    def __add__(self, var):
        new_list = [x + y for x, y in zip(self.mylist, var.mylist)]

        return SumList(new_list)

    def __sub__(self, var):
        new_list = [x - y for x, y in zip(self.mylist, var.mylist)]

        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)


ob1 = SumList([10, 11, 22, 33, 41])
ob2 = SumList([80, 121, 20, 300, 50])

print(ob1)
print(ob2)

new_obj = ob1 + ob2
print(new_obj)

new_obj = ob1 - ob2
print(new_obj)

print('=====================================')

ob3 = SumList([100, 101, 202, 303, 401])
ob4 = SumList([80, 21, 25, 160, 50])

print(ob3, ob4)

new_obj = ob3 + ob4
print(new_obj)

new_obj = ob3 - ob4
print(new_obj)