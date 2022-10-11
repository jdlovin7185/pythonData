import numpy as np


def schwarz(vector_1, vector_2):
    transposed_vector1 = np.transpose(vector_1)
    # multiplied = transposed_vector1 * vector_2
    multiplied_2 = np.dot(transposed_vector1, vector_2)
    # print(multiplied)
    print(multiplied_2)
    norms = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
    print(norms)


vec1 = np.array([[1], [1]])

vec2 = np.array([[2], [2]])

schwarz(vec1, vec2)
