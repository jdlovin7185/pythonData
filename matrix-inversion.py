import numpy as np

A = np.array([
    [1, 2],
    [4, 5]
])

print("Matrix A: \n", A)

# finding the inverse matrix using np.linalg.inv()

Ainv = np.linalg.inv(A)

print("The inverse of A\n", Ainv)

print("Multiplication of A and the inverse of A is: \n", np.matmul(A, Ainv))
