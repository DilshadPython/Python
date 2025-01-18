import sys

from call_name import morning, night

if len(sys.argv) == 2:
    morning(sys.argv[1])
    night(sys.argv[1])
