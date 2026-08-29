"""
Usages:
./test.py     (reads out the entrie config dict)
./test.py     (printing the value associated with this key)
./test.py this-key this-value    (sets 'this-key and 'this-value' in the dict)
"""

import sys

from solutions import ConfigDict

obj = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('Writing date: {0}, {1}'.format(key, value))
    obj[key] = value
# if 1 arg on command line, treat is as a key show the value
elif len(sys.argv) == 2:
    print('Reading a value')
    key = sys.argv[1]
    print("The value for {0} is {1}".format(sys.argv[1], obj[key]))
else:
    print('Reading data')
    for key in obj.keys():
        print('  {0} = {1}'.format(key, obj[key]))
