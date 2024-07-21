import numpy as np


def solve_quard_equation(a, b, c):
    if a == 0:
        return 1, (-c/b)
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + np.sqrt(delta))/(2*a)
        x2 = (-b - np.sqrt(delta))/(2*a)
        return 2, (x1, x2)
    elif delta == 0:
        return 1, (-b/(2*a))
    else:
        return 0, ()


def compute_eigenvector(a, b, c, d, eigenvalue):
    a_minus_lambda = np.array([[a-eigenvalue, b], [c, d-eigenvalue]])

    x = 1
    if a_minus_lambda[0, 1] != 0:
        y = -a_minus_lambda[0, 0]/a_minus_lambda[0, 1]
    else:
        y = -a_minus_lambda[1, 0]/a_minus_lambda[1, 1]
    return (x, y)


def compute_eigenvalue_eigenvector(matrix):
    a = -1
    b = -matrix[0, 0]-matrix[1, 1]
    c = matrix[0, 0]*matrix[1, 1] - matrix[0, 1]*matrix[1, 0]
    n, eigenvalues = solve_quard_equation(a=a, b=b, c=c)

    if n == 0:
        return None
    if n == 1:
        return (eigenvalues[0], compute_eigenvector(matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1], eigenvalues[0]))
    if n == 2:
        return ((eigenvalues[0], compute_eigenvector(matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1], eigenvalues[0])),
                (eigenvalues[1], compute_eigenvector(matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1], eigenvalues[1])))


if __name__ == '__main__':
    matrix = np.array([[0.9,0.2], [0.1, 0.8]])
    eigenvalue_vector = compute_eigenvalue_eigenvector(matrix)
    print(eigenvalue_vector)
