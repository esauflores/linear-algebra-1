import numpy as np


def qr_decomposition(A):
    A = A.astype(float)

    m, n = A.shape
    Q = A.copy()
    R = np.zeros((n, n))

    for i in range(n):
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:, i] / R[i, i]
        for j in range(i + 1, n):
            R[i, j] = Q[:, j].T @ Q[:, i]
            Q[:, j] = Q[:, j] - R[i, j] * Q[:, i]

    return Q, R
