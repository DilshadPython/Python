import numpy as np
from IPython import get_ipython

import matplotlib.pyplot as plt 
# %matplotlib inline  
get_ipython().run_line_magic('matplotlib', 'inline')


				#start, #end, #steps
points = np.arange(-10, 10, 0.01)

dx, dy = np.meshgrid(points, points)

print('X dimention:\n', dx)
print('\n')
print('Y dimention:\n', dy)

