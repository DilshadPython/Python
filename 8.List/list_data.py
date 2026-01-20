# copy of the list .sopy()
# Display the position .index()
# remove lang in the lst .remove()
# delete lang is the list .pop()
# make list empty .clear()

languages = ['python', '.Net', 'Java', 'JavaScript', 'C++']
lang = languages.copy()
# copy the list using .copy()
print('\n', lang)

# display the position of JS in the list
print('\n The position of JS in the list is : ', languages.index('JavaScript'))

# remove Java in the list
lang_re = languages.remove('Java')
print('\n', lang_re)

 # remove python is the list
pop_lang = languages.pop(0)
print('\n', pop_lang)

 # clear the list
languages.clear()
print('\n', languages)


