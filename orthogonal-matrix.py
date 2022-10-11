import numpy as np

A = np.array([
    [1.0, 0.0],
    [0.0, 1.0]
])


print("A:\n", A)

# checking for A*AT == AT*A

comparison_1 = np.dot(A.transpose(), A) == np.dot(A, A.transpose())
print(comparison_1)


# checking for A*AT = Identity matrix
comparison_2 = np.dot(A.transpose(), A) == np.eye(2)
print(comparison_2)

# comparing both the comparison done earlier
comparison_3 = comparison_1 == comparison_2

# checking if all elements of matrix comparison are true
equal_arrays = comparison_3.all()
print("A it an orthogonal matrix: ", equal_arrays)
