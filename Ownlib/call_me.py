import sys

from call_name import morning, night
'''
To run python call_me.py Jack
'''

if len(sys.argv) == 2:
    morning(sys.argv[1])
    night(sys.argv[1])
