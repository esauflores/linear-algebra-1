from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2

import numpy as np


def plu_decomposition(A):
    ## YOUR CODE HERE

    P, U, L = gauss_elimination_1(A, np.eye(A.shape[0]))
    P2, U2, L2 = gauss_elimination_1(U, np.eye(A.shape[0]))

    P = P.T
    L2 = np.linalg.inv(L2)
    U2 = U2

    return P, L2, U2


plu_decomposition(np.array([[1, 2], [3, 4]]))
