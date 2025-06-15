msg = 'Hello world'

print

print(len(msg))

# try to change one character
# msg[2] = 'X'
# print('Try to overwritten but get an error not possible because string is immutable')
# print(msg)

newmsg = msg + ' Hello London'

print(newmsg)

print

change = newmsg.upper()

print(change)
print(change.lower())

print

# I use split method where display l lowercase removed or display to nothing
test = msg.split('l')
print(test)

print()
# print count how many times o repated
print(newmsg.count('o'), ' << count()')

print()
# start from index 6
print(msg.find('world'), ' << find()')

print()
# we use replace() method
print(msg.replace('world', 'Python'))