import numpy as np

# upper triangular matrix witn pure 1s n = 100

A = np.triu(np.ones((100, 100)), 0)

for i in range(100):
    A[i][i] = i + 1

task = A.T @ A

task = np.array(task, dtype=np.int64)

answer = {"task": task}
