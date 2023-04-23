import numpy as np
v = np.array([2, 6, 3])
w = np.array([1, 0, 0])
u = np.array([7, 7, 2])
result1 = 2*v - w
result2= 3 * result1
result3 = 2 * u
ans = np.dot(result2, result3)
print(ans)
