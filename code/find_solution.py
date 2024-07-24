from gauss_elimination_1 import gauss_elimination_1
from gauss_elimination_2 import gauss_elimination_2


def find_solution(A, b):
    A = A.astype(float)
    b = b.astype(float)
    
    P, A, b = gauss_elimination_1(A, b)
    A, b = gauss_elimination_2(A, b)
    
    return b
