
f = open('Assignment/config_file.txt')

try:
    print('\n\tThe file exists and open, read it')
    print('\n', f.read())
except Exception:
    print('\n\tThe file cannot be opened.')