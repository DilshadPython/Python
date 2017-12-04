mylist = [2, 4, 6, 8]

print(mylist)
print;

mylist.append('Some text')
print(mylist)

print;

# remove the last element
mylist.pop()
print(mylist)

print; 
mylist.pop()
print(mylist)

print;
newlist = [9, 3, 4, 6, 0, 11, 23]
print(newlist)

remove_lst = newlist.pop(-1)
print(remove_lst)

remove_first = newlist.pop(0)
print(remove_first)

remove_index_num = newlist.pop(3)
print(remove_index_num)

print(newlist)
