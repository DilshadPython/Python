# This options is the best to identify the error
try:
    # The file not exist to make sure how it work
    f = open('config_file.txt')
    name = bad_name
except FileNotFoundError as e:
    print('\n\t', e)
except Exception as e:
    print('\n\t', e)

############################################################################

try:
    # The folder is spelt wrong to make sure second option is correct
    f = open('assignment/config_file.txt')
    name = bad_name
except FileNotFoundError as e:
    print('\n\t', e)
except Exception as e:
    print('\n\t', e)

##############################################################################

try:
    # The file not exist to make sure how it works
    f = open('config_pile.txt')
    print('\n', f.read())
except FileNotFoundError as e:
    print('\n\t', e)
except Exception as e:
    print('\n\t', e)