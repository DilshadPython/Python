print()
users = ['John', 'Mike', 'Cludia', 'George', 'Kim', 'Elena']

print('\t', users)

print()
for user in range(len(users)):
    print('\t',user + 1, users[user])

print()
# Now we will sorted the user alphabetically with number
for user in sorted(users):
    print('\t',user)

print()
for user in range(len(users)):
    print('\t', user + 1, sorted(users[user]))

print()
# print how many character each name in the list
for user in range(len(users)):
    print('\t', len(users[user]), ' = ', users[user])