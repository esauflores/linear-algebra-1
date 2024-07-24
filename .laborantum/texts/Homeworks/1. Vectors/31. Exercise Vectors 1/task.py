import numpy as np

a = np.array([1, 1, 1, 1])
b = np.array([1, -1, -1, 1])

expression = 2 * a + b

dot_prod = np.dot(a, b)

length_a = np.linalg.norm(a)
length_b = np.linalg.norm(b)

angle = dot_prod / (length_a * length_b)

dir_a = a / length_a
dir_b = b / length_b

a_proj_b = np.dot(a, b) / np.dot(b, b) * b
a_orth_b = a - a_proj_b

b_proj_a = np.dot(b, a) / np.dot(a, a) * a
b_orth_a = b - b_proj_a

answer = {
    "expression": expression,
    "dot_prod": dot_prod,
    "length_a": length_a,
    "length_b": length_b,
    "angle": angle,
    "dir_a": dir_a,
    "dir_b": dir_b,
    "a_proj_b": a_proj_b,
    "b_proj_a": b_proj_a,
    "a_orth_b": a_orth_b,
    "b_orth_a": b_orth_a,
}

print(answer)