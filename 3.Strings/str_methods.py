msg = 'How many years you have Python experiences?'

print('The length of the msg is :', len(msg))

print(msg.upper())

print(msg.lower())

print('\n isupper() >> ', msg.isupper())

print('\n split() >> ', msg.split(','))

print('\n replace() >> ', msg.replace('Python', 'JavaScript'))

print('\n find() >> ', msg.find('Python'), ' find the word Python from index 24 ')

print('\n in >> ', 'Python' in msg)
print('\n in >> ', 'python' in msg)

print('\n title() >> ', msg.title(), ' << Change all first char of each words to Upper' )