import numpy as np
import sys

p = list(range(1000))
n = np.arange(1000)

print(sys.getsizeof(0)*len(p))
print(n.size*n.itemsize)


