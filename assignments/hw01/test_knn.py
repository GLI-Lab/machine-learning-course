"""
Doctests for hw1_knn.py
No changes needed to this file.

Setup
-----
>>> import numpy as np

Define example dataset with N=6 points in 2D (F=2)
>>> data_NF = np.array([
...     [ 1.,  0.],
...     [ 0.,  1.],
...     [-1.,  0.],
...     [ 0., -1.],
...     [ 2.,  0.],
...     [ 0.,  2.]])
>>> query_QF = np.array([
...     [0.9,  0.2],
...     [0.0, -0.9],
...     [0.1,  1.8]])


Test euclidean_distances
------------------------
>>> dist_QN = euclidean_distances(data_NF, query_QF)
>>> dist_QN.shape
(3, 6)

# Distance from [0.9, 0.2] to [1, 0] should be sqrt(0.05)
>>> np.allclose(dist_QN[0, 0], np.sqrt(0.05))
True

# Distance from [0, -0.9] to [0, -1] should be 0.1
>>> np.allclose(dist_QN[1, 3], 0.1)
True

# Distance from [0.1, 1.8] to [0, 2] should be sqrt(0.05)
>>> np.allclose(dist_QN[2, 5], np.sqrt(0.05))
True


Test find_k_nearest_indices
---------------------------
>>> dist_QN = euclidean_distances(data_NF, query_QF)
>>> indices_QK = find_k_nearest_indices(dist_QN, K=3)
>>> indices_QK.shape
(3, 3)

# [0.9, 0.2] is closest to data[0]=[1,0], then data[4]=[2,0], then data[1]
>>> indices_QK[0].tolist()
[0, 4, 1]

# [0, -0.9] is closest to data[3]=[0,-1], then data[0] and data[2] (tie, smaller index first)
>>> indices_QK[1].tolist()
[3, 0, 2]

# [0.1, 1.8] is closest to data[5]=[0,2], then data[1]=[0,1], then data[0]=[1,0]
>>> indices_QK[2].tolist()
[5, 1, 0]


Test calc_k_nearest_neighbors K=1
----------------------------------
>>> neighb_QKF = calc_k_nearest_neighbors(data_NF, query_QF, K=1)
>>> neighb_QKF.shape
(3, 1, 2)

>>> neighb_QKF[0]
array([[1., 0.]])

>>> neighb_QKF[1]
array([[ 0., -1.]])

>>> neighb_QKF[2]
array([[0., 2.]])


Test calc_k_nearest_neighbors K=3
----------------------------------
>>> neighb_QKF = calc_k_nearest_neighbors(data_NF, query_QF, K=3)
>>> neighb_QKF.shape
(3, 3, 2)

>>> np.allclose(neighb_QKF[0], np.array([[1., 0.], [2., 0.], [0., 1.]]))
True

>>> np.allclose(neighb_QKF[1], np.array([[0., -1.], [1., 0.], [-1., 0.]]))
True

>>> np.allclose(neighb_QKF[2], np.array([[0., 2.], [0., 1.], [1., 0.]]))
True


Test predict_knn_classification
-------------------------------
>>> labels_N = np.array([0, 1, 1, 0, 2, 2])
>>> indices_QK = find_k_nearest_indices(euclidean_distances(data_NF, query_QF), K=3)

# Query 0 neighbors: indices [0,4,1] -> labels [0,2,1] -> tie -> smallest label 0
# Query 1 neighbors: indices [3,0,2] -> labels [0,0,1] -> majority 0
# Query 2 neighbors: indices [5,1,0] -> labels [2,1,0] -> tie -> smallest label 0
>>> predict_knn_classification(labels_N, indices_QK).tolist()
[0, 0, 0]

>>> labels_N2 = np.array([0, 0, 1, 1, 2, 2])

# Query 0 neighbors: indices [0,4,1] -> labels [0,2,0] -> majority 0
# Query 1 neighbors: indices [3,0,2] -> labels [1,0,1] -> majority 1
# Query 2 neighbors: indices [5,1,0] -> labels [2,0,0] -> majority 0
>>> predict_knn_classification(labels_N2, indices_QK).tolist()
[0, 1, 0]

"""

import numpy as np
from hw1_knn import (
    euclidean_distances,
    find_k_nearest_indices,
    calc_k_nearest_neighbors,
    predict_knn_classification,
)
