import numpy as np
ar = np.array
v = ar([846835985, 9834798552], dtype='i8')
u = ar([87502093, 123094980], dtype='i8')
v1, v2 = u, v
if np.linalg.norm(v2) < np.linalg.norm(v1):
    print('swap')
    v1, v2 = v2, vi
m = int(np.dot (v1, v2) / np.dot(v1, v1))
print(m)
v2 = v2 - m * v1
print(v2)
if np.linalg.norm(v2) < np.linalg.norm(v1):
    print('swap')
    v1, v2 = v2, v1
m = int(np.dot (v1, v2) / np.dot(v1, v1))
print(m)
print(v1)
print(v2)
print(np.dot (v1, v2))
