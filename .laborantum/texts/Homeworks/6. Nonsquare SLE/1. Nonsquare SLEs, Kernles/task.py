import numpy as np


def gauss_elimination_1(A, B, permutations=True):
    A = A.astype(float)
    B = B.astype(float)
    P = np.eye(A.shape[0])

    for i in range(A.shape[0]):
        max_index = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_index]] = A[[max_index, i]]
        B[[i, max_index]] = B[[max_index, i]]
        P[[i, max_index]] = P[[max_index, i]]

        if A[i, i] == 0:
            continue

        for j in range(i + 1, A.shape[0]):
            B[j] -= B[i] * A[j, i] / A[i, i]
            A[j] -= A[i] * A[j, i] / A[i, i]

        diag = A[i, i]
        A[i] /= diag
        B[i] /= diag

    return P, A, B


def gauss_elimination_2(A, B):
    A = A.astype(float)
    B = B.astype(float)

    for i in range(A.shape[0] - 1, -1, -1):
        if A[i, i] == 0:
            continue

        B[i] /= A[i, i]
        A[i] /= A[i, i]

        for j in range(i):
            B[j] -= B[i] * A[j, i]
            A[j] -= A[i] * A[j, i]

    return A, B


# basis vectors of the null space
def null_space(A):
    b = np.zeros(A.shape[0])
    P, U, C = gauss_elimination_1(A, b)
    U, C = gauss_elimination_2(U, C)

    # Identify pivot columns
    pivot_columns = []
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            if U[i, j] != 0:
                pivot_columns.append(j)
                break
    # Find the basis vectors of the null space
    null_space_basis = []
    for i in range(U.shape[1]):
        if i not in pivot_columns:
            null_space_basis.append(np.zeros(U.shape[1]))
            null_space_basis[-1][i] = 1
            for j in range(len(pivot_columns)):
                null_space_basis[-1][pivot_columns[j]] = -U[j, i]

    for i in range(len(null_space_basis)):
        null_space_basis[i] = null_space_basis[i].T.astype(dtype=np.int64)
        # make (n, 1) shape
        null_space_basis[i] = null_space_basis[i].reshape(
            null_space_basis[i].shape[0], 1
        )

    return null_space_basis


task_1_A = np.array([[1, 1, 1], [3, 0, 3]])
task_1_b = np.array([3, 6])

task_2_A = np.array([[1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 2, 2, 2]])
task_2_b = np.array([6, 8, 0])

task_3_A = np.array([[1, 2, 3, 4, 5, 6], [1, 1, 2, 3, 4, 5], [1, 1, 1, 2, 3, 4]])
task_3_b = np.array([-4, 2, -3])


answer = {
    "task_1": {
        "partial": np.array([[2, 1, 0]], dtype=np.int64).T,
        "null_space": null_space(task_1_A),
    },
    "task_2": {
        "partial": np.array([[6, 8, 0, 0, 0]], dtype=np.int64).T,
        "null_space": null_space(task_2_A),
    },
    "task_3": {
        "partial": np.array([[3, -11, 5, 0, 0]], dtype=np.int64).T,
        "null_space": null_space(task_3_A),
    },
}
