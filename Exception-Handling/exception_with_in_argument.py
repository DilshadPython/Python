# return an int 18 at line 12
def temp_convert(var):
    try:
        return int(var)
    except ValueError as argument:
        print('\n\tThe argument does not contain numbers >>', argument)
# Now we call the above function here with string
temp_convert('adb')

print('\n')

print('\tThis is int: ', temp_convert(18))
