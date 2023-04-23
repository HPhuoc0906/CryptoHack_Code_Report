import numpy as np
import math as mt
v1 = np.array([6, 2, -3])
v2 = np.array([5, 1, 4])
v3 = np.array([2, 7, 1])
matrix = np.vstack((v1, v2, v3))
# Tính định thức
DET = np.linalg.det(matrix)
print(int (round(abs(DET))))modular s
