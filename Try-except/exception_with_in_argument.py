def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print('The Argument does not contain numbers\n', Argument)
# Now we call the above function here
temp_convert('adb')

print('\n')

print('This is int: ', temp_convert(18))
