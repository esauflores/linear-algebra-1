import numpy as np

t1_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


t2_a = np.array([[1, 2], [3, 4]])

t3_a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
t3_b = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])
t3_c = np.array([1, 2])


answer = {
    "task1": np.array(t1_a @ t1_a, dtype=np.int64),
    "task2": np.array(t2_a @ t2_a @ t2_a, dtype=np.int64),
    "task3": np.array(t3_a @ t3_b @ t3_c, dtype=np.int64),
}
