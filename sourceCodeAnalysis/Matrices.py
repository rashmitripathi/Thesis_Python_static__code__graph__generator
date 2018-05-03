from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse as sp
import numpy as np


def cos_cdist_1(matrix, vector):
    v = vector.reshape(1, -1)
    return sp.distance.cdist(matrix, v, 'cosine').reshape(-1)


def cos_cdist_2(matrix1, matrix2):
    return sp.distance.cdist(matrix1, matrix2, 'cosine').reshape(-1)

def compare(list1,list2):
    matrix1 = np.asarray(list1)
    matrix2 = np.asarray(list2)

    results = []
    for vector in matrix2:
        distance = cos_cdist_1(matrix1, vector)
        distance = np.asarray(distance)
        similarity = (1 - distance).tolist()
        results.append(similarity)

    dist_all = cos_cdist_2(matrix1, matrix2)
    results2 = []
    for item in dist_all:
        distance_result = np.asarray(item)
        similarity_result = (1 - distance_result).tolist()
        results2.append(similarity_result)