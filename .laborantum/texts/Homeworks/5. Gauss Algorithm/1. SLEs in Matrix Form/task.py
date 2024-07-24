import numpy as np


# Ax = b
def gaussian_elimination(A, b):
    return np.linalg.inv(A) @ b


def LU_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]
    return L, U


task_1_A = np.array([[1, 1], [2, 1]], dtype=np.float64)
task_1_b = np.array([17, 10], dtype=np.float64).T
task_1_inv_A = np.linalg.inv(task_1_A)
task_1_L, task_1_U = LU_decomposition(task_1_A)
task_1_x = gaussian_elimination(task_1_A, task_1_b)


task_2_A = np.array([[1, 5], [2, 9]])
task_2_b = np.array([2, 4]).T
task_2_inv_A = np.linalg.inv(task_2_A)
task_2_L, task_2_U = LU_decomposition(task_2_A)
task_2_x = gaussian_elimination(task_2_A, task_2_b)

task_3_A = np.array([[1, 0, 1], [2, 1, -1], [3, 1, -2]])
task_3_b = np.array([3, 2, 3]).T
task_3_inv_A = np.linalg.inv(task_3_A)
task_3_L, task_3_U = LU_decomposition(task_3_A)
task_3_x = gaussian_elimination(task_3_A, task_3_b)

task_4_A = np.array([[1, 1, 1, 1], [2, 1, 1, 1], [3, 2, 1, 1], [4, 3, 2, 1]])
task_4_b = np.array([4, 5, 6, 10]).T
task_4_inv_A = np.linalg.inv(task_4_A)
task_4_L, task_4_U = LU_decomposition(task_4_A)
task_4_x = gaussian_elimination(task_4_A, task_4_b)

answer = {
    "task_1": {
        "A": task_1_A.astype(dtype=np.int64),
        "b": task_1_b.astype(dtype=np.int64),
        "inv_A": task_1_inv_A.astype(dtype=np.int64),
        "L": task_1_L,
        "U": task_1_U,
        "x": task_1_x,
    },
    "task_2": {
        "A": task_2_A.astype(dtype=np.int64),
        "b": task_2_b.astype(dtype=np.int64),
        "inv_A": task_2_inv_A.astype(dtype=np.int64),
        "L": task_2_L.astype(dtype=np.int64),
        "U": task_2_U.astype(dtype=np.int64),
        "x": task_2_x,
    },
    "task_3": {
        "A": task_3_A.astype(dtype=np.int64),
        "b": task_3_b.astype(dtype=np.int64),
        "inv_A": task_3_inv_A.astype(dtype=np.int64),
        "L": task_3_L.astype(dtype=np.int64),
        "U": task_3_U.astype(dtype=np.int64),
        "x": task_3_x,
    },
    "task_4": {
        "A": task_4_A.astype(dtype=np.int64),
        "b": task_4_b.astype(dtype=np.int64),
        "inv_A": task_4_inv_A.astype(dtype=np.int64),
        "L": task_4_L.astype(dtype=np.int64),
        "U": task_4_U.astype(dtype=np.int64),
        "x": task_4_x,
    },
}
