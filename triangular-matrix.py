import numpy as np

lower_triangle_matrix = np.tril(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

print("lower tri matrix \n", lower_triangle_matrix)

upper_triangle_matrix = np.triu(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)
print("upper tri matrix \n", upper_triangle_matrix)
