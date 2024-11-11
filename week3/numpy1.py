import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)