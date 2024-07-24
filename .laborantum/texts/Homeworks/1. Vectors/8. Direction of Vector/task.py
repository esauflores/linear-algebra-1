
import numpy as np
task1_v = np.array([-6])
task2_v = np.array([-4, -3])
task3_v = np.array([1, -1, -1, 1])
task4_v = np.array([4, 3, 2, 1, 2, 1, 1])

answer = {
    'task1': task1_v/np.linalg.norm(task1_v),
    'task2': task2_v/np.linalg.norm(task2_v),
    'task3': task3_v/np.linalg.norm(task3_v),
    'task4': task4_v/np.linalg.norm(task4_v)
}