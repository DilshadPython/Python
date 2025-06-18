users = ['John', 'Mike', 'Cludia', 'George', 'Kim', 'Elena']

mylist = []
for user in users:
    mylist.append({'name': user})

print(mylist)
print('\n#################################################################\n')
# using list comprehension instead of for
yourlist = [{'name': user, 'city': 'Brentwood'} for user in users]

print(yourlist)

print('\n#################################################################\n')
# using list comprehension instead of for
sort_list = [{'name': user, 'city': 'Brentwood'} for user in sorted(users)]

print(sort_list)