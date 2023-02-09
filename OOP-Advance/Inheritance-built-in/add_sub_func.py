class SumList:

    def __init__(self, listy):
        self.mylist = listy

    def __add__(self, var):
        # create new list
        new_list = []
        ziplist = zip(self.mylist, var.mylist)
        for x in ziplist:
            new_list.append(x[0] + x[1])
        return SumList(new_list)

    def __sub__(self, var):
        # create new list
        new_list = []
        ziplist = zip(self.mylist, var.mylist)
        for x in ziplist:
            new_list.append(x[0] - x[1])
        return SumList(new_list)

    # repr method is an instance method, it take the string function to placing the interenal list
    # which is mylist which is the list that sumlist holding and rendering as string
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
