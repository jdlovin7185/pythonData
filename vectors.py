import numpy as np

col_vec = np.array([[4], [3]])

row_vec = np.array([[4, -1, 2]])

print("the shape of the column vector - ", col_vec.shape)

print("the shape of the row vector - ", row_vec.shape)


# doing a zero row vector of dimension 3 using np.array()
zero_vector_1 = np.array([[0, 0, 0]])
print(zero_vector_1)
# showing a zero row vector of dimension 3 using np.zeros()
zero_vector_2 = np.zeros(3)
print(zero_vector_2)
# showing a zero column vector of dimension 3 using np.zeros() and reshape()
zero_vector_3 = np.zeros(3).reshape(3, 1)
print(zero_vector_3)

# indexing example of a vector, its like indexing of an array
vector = np.array([[4], [-1], [3]])
print("The index at postion 1 is - ", vector[1])
