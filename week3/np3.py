import numpy as np

import numpy as np
def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

my_array[[0, 1, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')
