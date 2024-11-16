import numpy as np

array1 = np.array([[1, 2], [3, 4]]) 
array2 = np.array([[1, 2], [3, 4]]) 

print(array1 == array2) # Does element wise comparison and returns truth value for every comparison which is again stored in the respective sized np array

comparison = array1 == array2
equal_arrays = comparison.all() # Here all the truth values of the inferred np array is taken and if all are True then it returns True, else False.

print(equal_arrays)