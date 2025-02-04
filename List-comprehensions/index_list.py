users = ['John', 'Mike', 'Cludia', 'George', 'Kim', 'Elena']

for user in range(len(users)):
    print(user + 1, users[user])

print()
# Now we will sorted the user alphabetically with number
for user in sorted(users):
    print(user)

print()
for user in range(len(users)):
    print(user + 1, sorted(users[user]))

print()
# print how many character each name in the list
for user in range(len(users)):
    print(len(users[user]), ' = ', users[user])