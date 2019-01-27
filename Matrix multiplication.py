import numpy as np
import time

A = np.array([[1,2],[3,4]])
B = np.array([[2,1],[4,3]])

# Pure python multiplication
def matrix_mul(x,y):
    C = [[0 for col in range(len(B[0]))] for row in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C
print(matrix_mul(A, B))

# Multiplication using numpy
N = A @ B
print(N)

# Process time evaluation
iter = 1000000
t0 = time.process_time()
for i in range(iter):
    A @ B
print(f"Time for numpy calc: {time.process_time() - t0}")

t0 = time.process_time()
for i in range(iter):
    matrix_mul(A, B)
print(f"Time for pure python calc: {time.process_time() - t0}")
