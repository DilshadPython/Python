import sys

# we write small msg
sys.stdout.write('Welcome to Python file.\n')


# create file named text.dat and 'a' use as append but is empty now. 
sys.stdout = open('text.dat', 'a')

# we send this message to a file ended with dat using print 
sys.stdout.write('I send this message for text.dat file created above using (sys.stdout.write)\n')
# but if you using python shell use this command
# >>> import sys
# >>> sys.stdout = open('text.dat', 'a')
# >>> print >> text.dat, 'send another msg\n')
# >> print('NED')

# now use print to send another msg to the above file
print('I am using print for another message')