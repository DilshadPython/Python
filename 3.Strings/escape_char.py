msg = 'To day is "Friday" is very cold but yesterday was "Thursday" very nice weather.'
print(msg)
print('=====================\n')

# The escape character allows you to use double quotes when you normally would not be allowed:
msg = 'To day is \'Friday\' is very cold but yesterday was \'Thursday\' very nice weather.'
print(msg)
print('=====================\n')

# How to use single quote in the message if need it \'
today = 'Today it\'s Friday which is very nice weather.'
print(today)
print('=====================\n')

# How backslash works \\ insert one backslash here
today = 'Today it\'s Friday which is very nice \\(weather).'
print(today)
print('=====================\n')

# \r carriage Return
txt = 'Welcome to\rPython'
print(txt)
print('=====================\n')

msg = 'Welcome\rPython!'
print(msg)
print('=====================\n')

#This example erases one character (backspace):
txt = 'Welcome \bPython!'
print(txt)
print('=====================\n')

# \f here we will enter new line each word and stay in the same position Form Feed
msg = 'Welcome\fto\fPython!'
print(msg)
print('=====================\n')

# #A backslash followed by three integers will result in a octal value:
txt = '\110\145\154\154\157 Java!'
print(txt)
print('=====================\n')

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f JavaScript"
print(txt)
print('=====================\n')

# The \x and
print('\x30, \x31, \x32, \x33, \x34, \x35, \x36, \x37, \x38, \x39,  \x30\x31' )
print('\x40 \x41 \x42 \x43 \x44 \x45 \x46 \x47 \x48 \x49 \x30 \x50')