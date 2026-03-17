"""
Doctests for hw1_knn.py
No changes needed to this file.

Setup
-----
>>> import numpy as np

Define example dataset with N=4 points in 2D (F=2)
>>> data_NF = np.array([
...     [ 1.,  0.],
...     [ 0.,  1.],
...     [-1.,  0.],
...     [ 0., -1.]])
>>> query_QF = np.array([
...     [0.9,  0.0],
...     [0.0, -0.9]])


Test euclidean_distances
------------------------
>>> dist_QN = euclidean_distances(data_NF, query_QF)
>>> dist_QN.shape
(2, 4)

# Distance from [0.9, 0] to [1, 0] should be 0.1
>>> np.allclose(dist_QN[0, 0], 0.1)
True

# Distance from [0, -0.9] to [0, -1] should be 0.1
>>> np.allclose(dist_QN[1, 3], 0.1)
True

# Distance from [0.9, 0] to [-1, 0] should be 1.9
>>> np.allclose(dist_QN[0, 2], 1.9)
True


Test find_k_nearest_indices
---------------------------
>>> dist_QN = euclidean_distances(data_NF, query_QF)
>>> indices_QK = find_k_nearest_indices(dist_QN, K=3)
>>> indices_QK.shape
(2, 3)

# [0.9, 0] is closest to data[0]=[1,0], then data[1] and data[3] (tie, smaller index first)
>>> indices_QK[0].tolist()
[0, 1, 3]

# [0, -0.9] is closest to data[3]=[0,-1], then data[0] and data[2] (tie, smaller index first)
>>> indices_QK[1].tolist()
[3, 0, 2]


Test calc_k_nearest_neighbors K=1
----------------------------------
>>> neighb_QKF = calc_k_nearest_neighbors(data_NF, query_QF, K=1)
>>> neighb_QKF.shape
(2, 1, 2)

>>> neighb_QKF[0]
array([[1., 0.]])

>>> neighb_QKF[1]
array([[ 0., -1.]])


Test calc_k_nearest_neighbors K=3
----------------------------------
>>> neighb_QKF = calc_k_nearest_neighbors(data_NF, query_QF, K=3)
>>> neighb_QKF.shape
(2, 3, 2)

>>> neighb_QKF[0]
array([[ 1.,  0.],
       [ 0.,  1.],
       [ 0., -1.]])

>>> neighb_QKF[1]
array([[ 0., -1.],
       [ 1.,  0.],
       [-1.,  0.]])


Test predict_knn_classification
-------------------------------
>>> labels_N = np.array([0, 1, 1, 0])
>>> indices_QK = find_k_nearest_indices(euclidean_distances(data_NF, query_QF), K=3)

# Query 0 neighbors: indices [0,1,3] -> labels [0,1,0] -> majority 0
# Query 1 neighbors: indices [3,0,2] -> labels [0,0,1] -> majority 0
>>> predict_knn_classification(labels_N, indices_QK).tolist()
[0, 0]

>>> labels_N2 = np.array([0, 0, 1, 1])

# Query 0 neighbors: indices [0,1,3] -> labels [0,0,1] -> majority 0
# Query 1 neighbors: indices [3,0,2] -> labels [1,0,1] -> majority 1
>>> predict_knn_classification(labels_N2, indices_QK).tolist()
[0, 1]

"""

import numpy as np
from hw1_knn import (
    euclidean_distances,
    find_k_nearest_indices,
    calc_k_nearest_neighbors,
    predict_knn_classification,
)
