
try:
    # The file not exist to make sure how it work
    f = open('configFile.txt')
    print('\n\tThe file exists and open, read it')
    print('\n', f.read())
except Exception:
    print('\n\tSorry. This file does not exist.')