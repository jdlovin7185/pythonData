import matplotlib.pyplot as plt
import numpy as np

# f(x) + 2 = vertical shift up
# f(x) - 3 = vertical shift down
# f(x-4) = horizontal shift right by 4 units
# f(x+3) = horizontal shift left by 3 units
#  -f(x) = reflects over the x-axis
#  f(-x) = reflects over the y-axis
#  -f(-x) = reflects over the origin
# 2f(x) = vertical stretch
#  1/2f(x) = shrink vertically, (if you put a fraction in front of the function)
# f(2x) = horizontal shrink
# f(1/2x) = horizontal stretch, (if you put a fraction in front of x)
#


vec_a = np.array([3, -4, 5])
vec_b = np.array([2, 7, -3])

x_points = np.array([0, 6])
y_points = np.array([0, 250])
plt.plot(vec_a, vec_b)

# chart2 = plt.plot(vec_a, vec_b)

plt.show()


