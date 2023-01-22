line = "Importing modules and entering the login information along with the URL of the "
line += "Duplicate an existing virtualenv environment and end."

words = line.split(' ')
words = sorted(words)

print('\n The line has to be sorted now:\n')
print(words)

word_dict = {}

for x in range(0, len(words)):
	if words[x] in word_dict:
		word_dict[words[x]] += 1
	else:
		word_dict[words[x]] = 1


print('\nWord list and count: \n')

for key in word_dict.keys():
	print(key, word_dict[key])