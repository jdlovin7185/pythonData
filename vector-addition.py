import numpy as np

vector_1 = np.array([[2, -1, 1]])
vector_2 = np.array([[1, 2, -1]])

# you can do this as a simple
print(vector_1 + vector_2)

# or you can use the add() function to add them together and get the same thing
print(np.add(vector_1, vector_2))
