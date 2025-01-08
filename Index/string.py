leason = 'Welcome to Python tutorials'

contents = '''
Django is a popular Python-based web framework. It is batteries included which 
dramatically speeds up web development but also comes with a bit of a learning
curve for newcomers. Whether you are new to web development or already experienced, 
here is an up-to-date list of the best Django books.
'''

print('\n line 10: >> ', leason[0])  # first char
print('\n line 11: >> ', leason[0:])  # first to the end
# first char to char 10 the 11 not include
print('\n line 12: >> ', leason[0:11])
print('\n line 13: >> ', leason[:9])  # form first to char 8
print('\n line 14: >> ', leason[-20:-1])  # reverse from last char to 19 char
print('\n line 15: >> ', leason[:-1])  # start from last to begginning

print('\n line 17: >> ', contents)  # print all
print('\n line 18: >> ', contents[21:60])  #

test = 'It is batteries included which dramatically speeds up web development but also comes with '

copy_test = test[:]

print('\n line 24: >>', copy_test)

name = 'Dilshad Abdulla'

print('\n line 29: >> ', name[1:-1])
