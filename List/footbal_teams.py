storage = ['Arsenal', 'Southampton' ,'Man Utd', 'Liverpool', 'Man City', 'Chelsea' ,-12, 'Tottenham']

print('\nThe teams in your storage are: \n', storage)

print('--'*20)
print('Display the team between 1 -4')
print('--'*20)
print(storage[1:4])

print('--'*20)
print('Display the teams in the list virticaly')
print('--'*20)

for teams in storage:
    print(teams)

print('--'*20)
# get the length of each teams
print('Display the length of the list in the storage: ')
print('--'*20)
print('The length of storage are: ', len(storage))


list1 = ['hello', 'bye', 'good']
list2 = ['bad', 'hi', 'well']


print('--'*20)
print('List 1: ', list1)
print('List 2: ', list2)
mylist= list1 + list2[::-1]

print('--'*20)
print('Add two lists together and reversed the second list from right to left:')
print('--'*20)
print(mylist)

name = ['Dilshad']
print(name * 4)