import numpy as np

matrix_1 = np.array(
    [[10, 20, 30],
     [-30, -40, -50]]
)

matrix_2 = np.array(
    [[100, -200, 300],
     [30, 50, 70]]
)

# using this is faster by a tiny bit if performance is an issue
print(matrix_1 + matrix_2)

# is a little faster when going about it this way
out = np.add(matrix_1, matrix_2)
print("\nAdding matrices using the add function\n", out)
