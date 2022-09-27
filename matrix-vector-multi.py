import numpy as np

# Matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A : \n", A)

# Column Vector
v = np.array([[1], [2], [3]])
print("v :\n", v)

#  find the product of the matrix and Vector
product = np.matmul(A, v)
print("Product of A and v is: \n", product)
