import numpy as np


# function to find the angle between 2 vectors
def angle_between(vector_1, vector_2):
    dot_pr = vector_1.dot(vector_2)
    norms = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
    return np.rad2deg(np.arccos(dot_pr / norms))


vets_1 = np.array([3, -1, 2])
vets_2 = np.array([2, 4, -1])

print("v1 = ", vets_1, "\nv2 = ", vets_2)

# find the angle between them by using the function angle_between()
print("Angle between the vectors v1 and v2 in 'degree' is : ", angle_between(vets_1, vets_2))
