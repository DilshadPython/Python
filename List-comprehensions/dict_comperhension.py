users = ['John', 'Mike', 'Cludia', 'George', 'Kim', 'Elena']

# using dictionary comprehension instead of list comprehension
sort_dict = {user: 'Berlin' for user in sorted(users) }

print(sort_dict)

print('\n#################################################################\n')