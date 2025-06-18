name = 'python'

for func in dir(name):
    print(func)
print('======\n')

print(name.capitalize(), 'Converts the first character to upper case')
print('======\n')

lang = 'JavaScript'
print(lang.casefold(), 'Converts string to lower case')
print('======\n')

txt = 'Welcome'
#'Returns a centered string add 30 whitespace in the left and right sides'
print(txt.center(30), 'Returns a centered string add 30 whitespace in the left and right sides')
print('======\n')

# print the duplicate word in the line which is like
# string.count(value, start, end)
msg = 'I like oranges, but I don\'t likes bananas.'
print(msg.count('like'))
print('======\n')

# here search from position 2 until 20 and second one from position 2 to 45 it should be 2 times repeat like
print(msg.count('like', 2, 20))
print('======\n')
print(msg.count('like', 2, 45))
print('======\n')

msg = 'I would love to visit Köln in Germany.'
print(msg.encode())
print('======\n')
print(msg.encode('ascii', 'ignore').decode('ascii'))
print('======\n')

"""
encoding	Optional. A String specifying the encoding to use. Default is UTF-8
errors	Optional. A String specifying the error method. Legal values are:

'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
"""
print(msg.encode(encoding="ascii",errors="backslashreplace"))
print(msg.encode(encoding="ascii",errors="ignore"))
print(msg.encode(encoding="ascii",errors="namereplace"))
print(msg.encode(encoding="ascii",errors="replace"))
print(msg.encode(encoding="ascii",errors="xmlcharrefreplace"))