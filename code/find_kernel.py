from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2

import numpy as np

def find_kernel(A):
    A = np.array(A)
    b = np.zeros(A.shape[0])
    A = np.column_stack((A,b))
    P, U, C = gauss_elimination_1(A, b)
    U, C = gauss_elimination_2(U, C)
    
    pivot_columns = []
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            if U[i, j] != 0:
                pivot_columns.append(j)
                break
            
    A = A[:,pivot_columns]
    A = np.delete(A, pivot_columns, axis=1)


    return A