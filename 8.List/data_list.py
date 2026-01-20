# add to the list append()
# add new language in specific location
# sort the list alphabetic
# reverse the list alphabetic
languages = ['python', '.Net', 'Java', 'JavaScript', 'C++']
print('\n', languages)

#  Add new language to the end of the list as default!
languages.append('C language')
print('\n', languages)

#  Here add new language in specific position like from beginning!
languages.insert(0, 'Java')
print('\n The language is add in the beginning in is : ', languages[0])
print('\n', languages)

languages.insert(3, 'C#')
print('\n The second languages in the list is : ', languages[3])
print('\n', languages)

print('\n The number of Java in the list are: ', languages.count('Java'))
print('\n Here sorted the list alphabetic: ', sorted(languages))

print('\n Now reverse the list alphabetic: ', list(reversed(languages)))
print('\n Another way to reverse the list: ', languages[::-1] )

databases = ['MySql', 'PostgreSQL', 'SQL']

languages.extend(databases)
print('\n', languages, '\n')
