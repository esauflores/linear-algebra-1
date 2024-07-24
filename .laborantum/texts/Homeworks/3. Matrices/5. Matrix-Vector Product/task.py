import numpy as np


a = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 1]], dtype=np.int64)
x = np.array([1, 1, -1], dtype=np.int64)


a_x = a @ x

task_1 = np.linalg.norm(a_x) / np.linalg.norm(x)

answer = {"task1": task_1}
