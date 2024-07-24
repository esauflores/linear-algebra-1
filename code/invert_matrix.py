from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2


import numpy as np


def invert_matrix(A):

    eye = np.eye(A.shape[0])

    P, U, L = gauss_elimination_1(A, eye)

    for i in range(U.shape[0]):
        if U[i, i] == 0:
            return None

    _, inv = gauss_elimination_2(U, L)

    return inv


print(invert_matrix(np.array([[1, 2], [3, 4]])))
