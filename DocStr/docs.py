import sys
"""
if we run py docs.py we will get the Docstr :) in line 6 but if we run py docs.py 2
"""
if len(sys.argv) == 1:
    print('Docstr :)')
else:
    print(f'the current file is: ', sys.argv[1])