storage = ['Arsenal', 'Southampton' ,'Man Utd', 'Liverpool', 'Man City', 'Chelsea' ,-12, 'Tottenham']

print('The teams in your storage are: \n', storage)

print('--'*20)
print(storage[1:4])

print('--'*20)
for teams in storage:
    print(teams)

print('--'*20)
# get the length of each teams
print('The length of storage are: ', len(storage))

print('--'*20)
list1 = ['hello', 'bye', 'good']
list2 = ['bad', 'hi', 'well']

mylist= list1 + list2[::-1]

print(mylist)

name = ['Dilshad']
print(name * 4)