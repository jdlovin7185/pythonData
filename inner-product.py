import numpy as np

vector_1 = np.array([1, 2, 3])

vector_2 = np.array([4, 5, 6])

transposed = np.transpose(vector_1)

print("Vector 1: \n", vector_1)
print("Vector 2: \n", vector_2)

# finding the inner product of the vector of same dimensions using inner()
inner_product = np.inner(vector_1, vector_2)
# long_way_inner_product = np.dot(transposed, vector_2)
print("The inner product is -> \n", inner_product)

# there are also orthogonal vectors

vector_3 = np.array([[3], [-1], [2]])
vector_4 = np.array([[2], [4], [-1]])

# finding the transpose of vector 3
transposed_vec_3 = np.transpose(vector_3)

# finding the inner product using the dot() function
result = np.dot(transposed_vec_3, vector_4)
print("Dot product \n", result)
