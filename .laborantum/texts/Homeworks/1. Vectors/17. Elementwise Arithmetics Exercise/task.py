import numpy as np

a = np.array([2, 2, -1, 1])
b = np.array([1, -1, 1/2, -1/2])

task1_v = (2*a + b)/2 + 5
task2_v = np.sqrt(2*(a+2*b)/a)

# both vectors as int64

task1_v = np.array(task1_v, dtype=np.float64)
task2_v = np.array(task2_v, dtype=np.int64)

answer = {
    'task1': task1_v,
    'task2': task2_v
}