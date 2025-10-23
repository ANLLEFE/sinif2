import numpy as np
A = np.array([[1/9, 8/9, -4/9], [4/9,-4/9,-7/9 ], [8/9, 1/9,4/9] ])
B = np.array([[1/9, 4/9,8/9], [8/9, -4/9, 1/9], [-4/9, -7/9,4/9]])

A_transpose = A.T
print("A matrisi:")
print(A * A.T )