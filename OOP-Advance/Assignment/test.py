"""
Usages:
./test.py     (reads out the entrie config dict)
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
else:
	print('Reading data')
	for key in obj.keys():
		print('  {0} = {1}'.format(key, obj[key]))