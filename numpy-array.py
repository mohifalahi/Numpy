import numpy as np

n1 = np.array([1, 2, 3])
n2 = np.array([(1, 2, 3),(4, 5, 6)])
n3 = np.array([(1, 2, 3),(4, 5, 6),(7, 8, 9)])

print(f"Array: {n3}")
print(f"Dimension: {n3.ndim}") #The dimension of array
print(f"Size: {n3.size}") #The number of elements in an array
print(f"Item size: {n3.itemsize}") #The size of each element of an array in byte
print(f"Data type: {n3.dtype}") #Data-type of an array
print(f"Shape: {n3.shape}") #number of rows and columns of an array

n2 = n2.reshape(3,2)
print(n2)