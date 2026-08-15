"""
Display Python interpreter version details using the sys module.
"""

import sys

# Notice:
# 1. sys.version returns a string containing the version number and build details.
# 2. sys.version_info returns a named tuple containing (major, minor, micro, releaselevel, serial).

# -----------------------------------------------------------------
# [Old Version / Legacy print]
# -----------------------------------------------------------------
print('Your python version')
print(sys.version)

print('-' * 40)

# -----------------------------------------------------------------
# [New Version / Python 3.6+ f-string formatting]
# -----------------------------------------------------------------
v = sys.version_info
print(f"Python Version (formatted): {v.major}.{v.minor}.{v.micro}")
print(f"Release Level: {v.releaselevel.capitalize()}")
print(f"Full System Version:\n{sys.version}")