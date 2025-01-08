name_list = ['Python', 'Django', 'Flask']

print(name_list)

count_names = len(name_list)
print(count_names)

# we initiaze the string we want to add
addnewname = 'FastAPI'

# very important we have to put the addnewname between []
name_list += [addnewname]

print(str(name_list))
update_count_names = len(name_list)
print(update_count_names)
