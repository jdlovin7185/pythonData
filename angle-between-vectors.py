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

# =================================================
# checking my answers as i write them out on paper
vec3 = np.array([-2, 5])
vec4 = np.array([4, 3])

print("Example 2 angle is ->", angle_between(vec3, vec4))

vec_a = np.array([3, -4, 5])
vec_b = np.array([2, 7, -3])

print("Example 3 angle is ->", angle_between(vec_a, vec_b))
