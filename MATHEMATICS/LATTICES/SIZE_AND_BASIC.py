 import numpy as np
# v = np.array( 4, 6, 2, 5)
import math
v = [ 4, 6,2,5]
# tícgh vô hướng với nó lun
cal = sum([a**2 for a in v])
ans = math.sqrt( cal)
print ( int (ans))
