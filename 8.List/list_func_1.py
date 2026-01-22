languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']
print('\n', languages)

#  Add new language to the end of the list as default!
languages.append('C language')
print('\n .append(): ', languages)

#  Here add new language in specific position like from beginning!
languages.insert(0, 'Java')
print('\n .insert(): ', languages)

languages.insert(3, 'Go')
print('\n .insert(3) : ', languages[3])

print('\n Show the list now: ', languages)

print('\n .count(): ', languages.count('Java'))

sort_lang = sorted(languages)
print('\n .sorted() the list alphabetic: ', sort_lang)

languages.sort(reverse=True)
print('\n sort(reverse=True) ', languages)

print('\n Last item in the list : ', languages[-1] )

databases = ['MySql', 'PostgreSQL', 'SQL']
languages.extend(databases)
print('\n .extend(): ', languages)

languages.reverse()
print('\n .reverse(): ', languages)
print('\n .sorted() the list alphabetic: ', sorted(languages), '\n')