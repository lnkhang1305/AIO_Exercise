import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector * vector))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    return vector1.dot(vector2)


def cosine_similarity(vector1,vector2):
    return compute_dot_product(vector1,vector2)/(compute_vector_length(vector1)*compute_vector_length(vector2))


if __name__ == '__main__':
    vector1 = np.array([1,2,3])
    vector2 = np.array([4,5,6])
    print(cosine_similarity(vector1,vector2))