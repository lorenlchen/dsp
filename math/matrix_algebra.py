#Matrix Algebra

import numpy as np
import pprint

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6,0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([1, 8, 0, 5]).T
alpha = 6

print("1.1) " + str(A.shape))  # 1.1) (2, 3)
print("1.2) " + str(B.shape))  # 1.2) (2, 2)
print("1.3) " + str(C.shape))  # 1.3) (3, 2)
print("1.4) " + str(D.shape))  # 1.4) (2, 3)
print("1.5) " + str(u.shape))  # 1.5) (1, 4)
print("1.6) " + str(w.shape))  # 1.6) (4, 1)
print("\n")

print("2.1) " + str(np.add(u,v)))         # 2.1) [[ 9  7 -4  9]]
print("2.2) " + str(np.subtract(u,v)))    # 2.2) [[ 3 -3 -2  1]]
print("2.3) " + str(alpha * u))           # 2.3) [[ 36  12 -18  30]]
print("2.4) " + str(u @ v.T))             # 2.4) [[51]]
print("2.5) " + str(np.linalg.norm(u)))   # 2.5) 8.60232526704
print("\n")

try:
    print("3.1) " + str(np.add(A, C)))
except ValueError:
    print("3.1) Not defined")

# 3.1) Not defined

try:
    print("3.2) " + str(np.subtract(A, C.T)))
except ValueError:
    print("3.2) Not defined")

# 3.2) [[-4 -7 -3]
#       [ 3  6  4]]

try:
    print("3.3) " + str(np.add(C.T, 3 * D)))
except ValueError:
    print("3.3) Not defined")

# 3.3) [[14  3  3]
#       [ 2  7  9]]

try:
    print("3.4) " + str(B @ A))
except ValueError:
    print("3.4) Not defined")

# 3.4) [[-1 -5 -1]
#       [ 2  7  4]]

try:
    print("3.5) " + str(B @ A.T))
except ValueError:
    print("3.5) Not defined")

# 3.5) Not defined

try:
    print("3.6) " + str(B @ C))
except ValueError:
    print("3.6) Not defined")

# 3.6) Not defined

try:
    print("3.7) " + str(C @ B))
except ValueError:
    print("3.7) Not defined")

# 3.7) [[ 5 -6]
#       [ 9 -8]
#       [ 6 -6]]

try:
    print("3.8) " + str(np.linalg.matrix_power(B, 4)))
except ValueError:
    print("3.8) Not defined")

# 3.8) [[ 1 -4]
#       [ 0  1]]

try:
    print("3.9) " + str(A @ A.T))
except ValueError:
    print("3.9) Not defined")

# 3.8) [[14 28]
#       [28 69]]

try:
    print("3.10) " + str(D.T @ D))
except ValueError:
    print("3.10) Not defined")

# 3.10) [[10 -4  0]
#        [-4  8  8]
#        [ 0  8 10]]

