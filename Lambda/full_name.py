'''
 stript removed white spaces
 title function will capitalise the first character of each name
'''

myfullname = lambda fname, lname: fname.strip().title() + " " + lname.strip().title()


print(myfullname(" dilshad", "abdulla"))

names = ['Dilshad Abdulla', 'Nicholas Herriot', 'Paulo Maldini', 'Chris Ederson', 'Steven Case']

# print(help(names.sort))
'''
Help on built-in function sort:

sort(...) method of builtins.list instance
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
'''

# this function will sorted out all name alphabetically via last name
names.sort(key= lambda name: name.split(' ')[-1].lower())

print(names)