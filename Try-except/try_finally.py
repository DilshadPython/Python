# This options is the best to identify the error
try:
    # The file is existed but we try to use else here go to last option
    f = open('config_file.txt')
except FileNotFoundError as e:
    print('\n\t', e)
except Exception as e:
    print('\n\t', e)
else:
    print('\n The else option tells we can read the file, try is correct here but we use else to read it.')
    print('\n', f.read())
    f.close()
finally:
    print('\n The code is executing finally.')

########################################################################################################

try:
    # The file spelt wrong by purposes to show try option is correct, however filly tell the code executing
    f = open('config_pile.txt')
except FileNotFoundError as e:
    print('\n\t', e)
except Exception as e:
    print('\n\t', e)
else:
    print('\n The else option tells we can read the file, try is correct here but we use else to read it.')
    print('\n', f.read())
    f.close()
finally:
    print('\n The code is executing finally.')