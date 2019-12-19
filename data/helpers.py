import numpy as np

def get_one_hot_matrix(mtx, n):
    mtx = np.array(mtx)
    matrix = np.zeros([mtx.shape[0], n])
    for i in range(len(mtx)):
        temp = [Id for Id in mtx[i] if Id > -1]
        matrix[i, temp] = 1
    return matrix