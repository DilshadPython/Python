languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']

print('\n If is exist: ', 'Ruby' in languages)

print('\n If not exist: ', 'Postgres' in languages, '\n')

for lang in languages:
    print('\t - ', lang)

print()
# Display the position of the language and language
for index, lang in enumerate(languages):
    print('\t :', index, lang)

# Display horizontal and separate by , use join
print('\n .join(): ', ', '.join(languages))

# Display horizontal but use split()
create_list = ' - '.join(languages)
new_list = create_list.split(' - ')
# Display to default list
print('\n .split(): ', new_list)

# Display to default list
create_list = ' | '.join(languages)
new_list = create_list.split(' | ')
print('\n .split(): ', new_list)

print("\n .join(): ", ' | '.join(languages), '\n')
