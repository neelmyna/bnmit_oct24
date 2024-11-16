import numpy as np

arr = [20, 2, 7, 1, 34] 
# mean 
print("mean of arr:", np.mean(arr)) 

# median 
print("median of arr:", np.median(arr)) 

# sum 
print("Sum of arr(uint8):", np.sum(arr, dtype = np.uint8)) 
print("Sum of arr(float32):", np.sum(arr, dtype = np.float32)) 

# min and max 
print("maximum element:", np.max(arr)) 
print("minimum element:", np.min(arr)) 

# var 
print("var of arr:", np.var(arr)) 
print("var of arr(float32):", np.var(arr, dtype = np.float32)) 

# standard deviation 
print("std of arr:", np.std(arr)) 
print ("More precision with float32", np.std(arr, dtype = np.float32))
