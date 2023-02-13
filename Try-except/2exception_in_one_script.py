import sys

try:
    # we add one arg enter here to make success need to add another number
    # in line 11 explain how
    arg = sys.argv[1]
    num = int(arg)
except(IndexError, ValueError):
    exit('Please enter an integer on the command line')

# to get the last line last print run: python two_args_in_one_script.py 5 (anynumber)
print('Thanks for the int')
