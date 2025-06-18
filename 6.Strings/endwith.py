txt = 'Welcome to the Europe to watch the fantastic football.'

print(txt.endswith('ll.')) # it should return True
print('==========\n')

# string.endswith(value, start, end)
# here check the position 6 to 15 with the phrase 'fantastic football'
x = txt.endswith('fantastic football.', 6, 15)
print(x)
print('==========\n')

# position 46 and end with 56 which is False
a = txt.endswith('football.', 46, 56)
# position 45 end with 55 which is True
a = txt.endswith('football.', 45, 55)
print(a)
print('==========\n')

#Check if the string ends with either the phrase "world." or "castle.":
msg = 'Welcome to the Europe to watch the fantastic Basketball.'
y = msg.endswith(('football.', 'Basketball.'))
print(y)

