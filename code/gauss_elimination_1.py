import numpy as np


# STABLE GAUSSIAN ELIMINATION
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
