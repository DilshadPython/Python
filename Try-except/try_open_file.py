
try:
    # The file not exist to make sure how it work
    f = open('config_file.txt')
    name = bad_name
except FileNotFoundError:
    print('\n\tSorry. This file does not exist.')
except Exception:
    print('\n\tSorry. Exception last option something went wrong.')

############################################################################

try:
    # The folder is spelt wrong to make sure second option is correct
    f = open('assignment/config_file.txt')
    name = bad_name
except FileNotFoundError:
    print('\n\tSorry. FineNotFoundError folder spell wrong.')
except Exception:
    print('\n\tSorry. last option something went wrong.')

##############################################################################

try:
    # The file not exist to make sure how it works
    f = open('config_pile.txt')
    print('\n', f.read())
except FileNotFoundError:
    print('\n\tSorry. This file does not found or maybe spelt wrong.')
except Exception:
    print('\n\tSorry. the file name is spelling wrong.')