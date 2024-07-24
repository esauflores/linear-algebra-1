import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

task = 5 * a - 4 * b

# force int65
task = np.array(task, dtype=np.int64)

answer = {"task": task}
