import builtins
import re


for x in dir(builtins):
	if re.match(r'^[a-z]', x):
		print(x)
		print(getattr(builtins, x).__doc__)
		print('*'*79)
