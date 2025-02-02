import sys
"""
if we run py docs.py we will get the Docstr :) in line 6 
but if we run py docs.py -n 2
"""
if len(sys.argv) == 1:
    print('Docstr :)')
elif len(sys.argv) == 3 and sys.argv[1] == '-n':
    n = int(sys.argv[2])
    for _ in range(n):
        print('Hello new python')
else:
    print(f'the current file is: ', sys.argv[1])