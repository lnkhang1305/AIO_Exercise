import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector * vector))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    return vector1.dot(vector2)


def matrix_multi_vector(matrix, vector):
    return matrix.dot(vector)


def matrix_multi_matric(matrix1, matrix2):
    return matrix1.dot(matrix2)


def compute_determinant(matrix):
    return matrix[0, 0]*matrix[1, 1] - matrix[0, 1]*matrix[1, 0]


def inverse_matrix(matrix):
    det_matrix = compute_determinant(matrix)
    if det_matrix <= 0:
        return 'Matrix cant inverse'
    result = np.array([[matrix[1, 1], -matrix[0, 1]],
                      [-matrix[1, 0], matrix[0, 0]]]) / det_matrix
    return result


if __name__ == '__main__':
    vector1 = np.array([1, 2])
    vector2 = np.array([3, 4])
    matrix1 = np.array([[5, 2], [2, 3]])
    matrix2 = np.array([[3, 4, 5], [4, 5, 6]])
    print(compute_vector_length(vector1))
    print(compute_dot_product(vector1, vector2))
    print(matrix_multi_vector(matrix1, vector1))
    print(matrix_multi_matric(matrix1, matrix2))
    print(compute_determinant(matrix1))
    print(inverse_matrix(matrix1))
