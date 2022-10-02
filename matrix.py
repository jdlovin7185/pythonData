import numpy as np

matrix_2x2 = np.array(
    [[1, 2],
     [3, 4]]
)

matrix_3x3 = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

print("Matrix 1 of 2x2\n", matrix_2x2)

print("Matrix 2 of 3x3\n ", matrix_3x3)

A = np.array(
    [[2, -2],
     [3, 1],
     [1, 4]]
)

print("printing the index of row [2, 1] = ", A[2, 1])
# printing the transpose of a matrix using the transpose function

print("Matrix A before transpose \n", A)
print("Matrix A Transpose: \n", np.transpose(A))
