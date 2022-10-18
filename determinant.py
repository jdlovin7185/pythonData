import numpy as np

# creating a matrix

matrix = np.array([
    [2, 4, -3],
    [5, 7, 6],
    [-8, 1, 9]
])

# finding the determinant
print(np.linalg.det(matrix))
# I got 441 when I wrote it out but numpy suggests its = -440.9999999999996
