# mylist is inherite from list object but indezes from 1 instead of 0
class MyList(list):

    def __getitem__(self, index):
        if index == 0:
            raise IndexError(" error")
        if index > 0:
            index = index - 1
           	# this method is called when we access a value with subscript (x[1], etc)
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError(" error")
        if index > 0:
            index = index - 1
        return list.__setitem__(self, index, value)


obj = MyList(['ABc', 'DEf', 'GEh', 'IJk']) # __init__ inherited from builtin list

print(obj)  # __repr__ inherited from builtin list

obj.append('LMn')  # __appedn__ inherited from builtin list

print(x[1]) # 'ABc' MyList.__getitem__() customized list superclass method index is 1 but refelect 0
print(x[4]) # idex is 4 but refelect 3

for x in obj: # the index start from 1
    print(x)
