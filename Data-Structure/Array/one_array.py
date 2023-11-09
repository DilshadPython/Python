
mylist = [3, 5, 7, 9, 11, 13, 15]

# this is one d array the index of the item in my list wisll display the
# location
print(mylist[3])

# If I want to ad a new item to my list will automatically added to the end:
mylist.append(17)

print(mylist)

# adding another one
mylist.append(4)
print(mylist)

'''
now we adding a number in knowen index: add number 88 to index 3 which number 9 in the list
What is happening: will add the number 88 and replace the 9 to 88 when you print there is no 9
'''
mylist[3] = 88
print(mylist)

# now we add a string to the list
mylist[6] = 'Welcome home'
print(mylist)
print()

for num in mylist:
    print(num, ' : ', type(num))

print()
print('###################')
for x in range(len(mylist)):
    print(mylist[x])

print()
print('###################')

print(mylist[2:7])

# we print fromindex 2 to 7 and each time with 2 steps
print()
print(mylist[2:7:2])

print()
print(mylist[::])
print(mylist[::-1])

# print all expect the last one
print()
print(mylist[:-1])

print()
print(mylist[1::-1])
print(mylist[1:-1])

print()
print('Maximum:')

numbers = [3, 5, 22, 7, 9, 11, 13, 15, 'str']
maximum = numbers[0]
for num in numbers:
    if num == str(num):
        pass
    elif num > maximum:
        maximum = num

print(maximum)
