import numpy as np
# Defining both the matrices 
a = np.array([5, 72, 13, 100]) 
b = np.array([2, 5, 10, 30]) 

# Performing addition using numpy function 
print("Addition:", np.add(a, b)) 

# Performing subtraction using numpy function 
print("Subtraction:", np.subtract(a, b)) 

# Performing multiplication using numpy function 
print("Multiplication:", np.multiply(a, b)) 

# Performing division using numpy functions 
print("Division:", np.divide(a, b)) 

# Performing mod on two matrices 
print("Mod:", np.mod(a, b)) 

#Performing remainder on two matrices 
print("Remainder:", np.remainder(a,b)) 

# Performing power of two matrices 
print("Power:", np.power(a, b)) 

# Performing Exponentiation. exp() takes an array and return an array of elements ePOWb[i]
print("Exponentiation:", np.exp(b))
