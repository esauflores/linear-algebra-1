import numpy as np


# At this state A IS a upper triangular matrix with unit diagonal
# B is the right hand side of the system
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