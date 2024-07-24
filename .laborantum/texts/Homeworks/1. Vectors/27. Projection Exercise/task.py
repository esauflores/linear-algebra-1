import numpy as np


a = np.array([6, 3, 2, 1, 0])
b = np.array([1, 1, 3, 3, 4])

proj_a_b = np.dot(a, b) / np.dot(b, b) * b
orth_a_b = a - proj_a_b

proj_b_a = np.dot(b, a) / np.dot(a, a) * a
orth_b_a = b - proj_b_a

answer = {
    "proj_a_b": proj_a_b,
    "orth_a_b": orth_a_b,
    "proj_b_a": proj_b_a,
    "orth_b_a": orth_b_a,
}
