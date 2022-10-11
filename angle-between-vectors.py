import numpy as np


def angle_between(vec1, vec2):
    dot_pr = vec1.dot(vec2)
    norms = np.linalg.norm(vec1) * np.linalg.norm(vec2)

    return np.rad2deg(np.arccos(dot_pr / norms))


vector_1 = np.array([3, -1, 2])
vector_2 = np.array([2, 4, -1])

print("v1 = ", vector_1, "\nv2 = ", vector_2)
# finding the angle between these 2 vectors by using the function angle_between()

print("Angle between the vectors v1 and v2 in 'degree' is : ", angle_between(vector_1, vector_2))
