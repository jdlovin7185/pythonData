import numpy as np

A = np.array(
    [[2, 3, 1],
     [3, 4, -1],
     [1, -1, 1]]
)
print("A:\n", A)

transposed_matrix = A.transpose()
print("transpose of A: \n", transposed_matrix)

# comparing each element of both matrices and then saving it as a variable
comparison = (A == transposed_matrix)

print(comparison)
equal_arrays = comparison.all()
print(equal_arrays)
