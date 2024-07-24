
import numpy as np
X = np.array([1, 2, 3])
Y = np.array([3, 4, 5])

basis_a = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
basis_b = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])

x_a_contra = np.dot(np.linalg.inv(basis_a.T), X)
x_a_co = np.dot(basis_a, X)

x_b_contra = np.dot(np.linalg.inv(basis_b.T), X)
x_b_co = np.dot(basis_b, X)

y_a_contra = np.dot(np.linalg.inv(basis_a.T), Y)
y_a_co = np.dot(basis_a, Y)

y_b_contra = np.dot(np.linalg.inv(basis_b.T), Y)
y_b_co = np.dot(basis_b, Y)


answer = {
    'x_a_contra': x_a_contra,
    'x_a_co': x_a_co,
    'x_b_contra': x_b_contra,
    'x_b_co': x_b_co,
    'y_a_contra': y_a_contra,
    'y_a_co': y_a_co,
    'y_b_contra': y_b_contra,
    'y_b_co': y_b_co
}