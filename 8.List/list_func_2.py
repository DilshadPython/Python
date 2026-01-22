languages = ['python', 'Java', 'JavaScript', 'Ruby', 'PHP']
lang = languages.copy()

print('\n .copy(): ', lang)

print('\n [1:3]', lang[1:3])

web = ['Google', 'Microsoft', 'Apple']

languages.insert(1, web)
print('\n .insert(): ', languages)

# display the position of JS in the list
print('\n .index() : ', languages.index('JavaScript'))

print('\n languages[2]) : ', languages[2])

# remove Java in the list
languages.remove('Java')
print('\n .remove(): ', languages)

# remove python is the list
languages.pop(0)
print('\n .pop(): ', languages)

# clear the list
languages.clear()
print('\n .clear(): ', languages)

numbers = [17, 5, 9, 15, 10, 3]
print('\n :', numbers)

print('\n .sort(): ', numbers)

print('\n .min(numbers): ', min(numbers))

print('\n .max(numbers): ', max(numbers))

print('\n .sum(numbers): ', sum(numbers), '\n')

