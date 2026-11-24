import numpy as np


a = np.array([['a', 'b', 'c', 'd', 'e'],
				['ab', 'cd', 'ef','gh', 'ij'],
				['kl', 'mn', 'op', 'qr', 'st']])

print(a[0, :])
print(a[1, :])
print(a[2, :3])