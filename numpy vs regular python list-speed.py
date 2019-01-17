# addition of two vectors: pure python vs. numpy
import numpy as np
import time

size = 1000000

l1 = list(range(size))
l2 = list(range(size))

n1 = np.arange(size)
n2 = np.arange(size)

t0 = time.process_time()
a = []
for i in range(size):
    a.append(l1[i] + l2[2])
print(time.process_time()-t0)

t0 = time.process_time()
add = n1 + n2
print(time.process_time()-t0)

