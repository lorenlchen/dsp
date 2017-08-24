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

print("1.1) " + str(A.shape))
print("1.2) " + str(B.shape))
print("1.3) " + str(C.shape))
print("1.4) " + str(D.shape))
print("1.5) " + str(u.shape))
print("1.6) " + str(v.shape))
print("1.7) " + str(w.shape))
print("\n")

print("2.1) " + str(np.add(u,v)))
print("2.2) " + str(np.subtract(u,v)))
print("2.3) " + str(alpha * u))
print("2.4) " + str(np.vdot(u,v)))
print("2.5) " + str(np.linalg.norm(u)))
print("\n")

try:
    print("3.1) " + str(np.add(A, C)))
except ValueError:
    print("3.1) Not defined")

try:
    print("3.2) " + str(np.subtract(A, C.T)))
except ValueError:
    print("3.2) Not defined")

try:
    print("3.3) " + str(np.add(C.T, 3 * D)))
except ValueError:
    print("3.3) Not defined")
try:
    print("3.4) " + str(B @ A))
except ValueError:
    print("3.4) Not defined")

try:
    print("3.5) " + str(B @ A.T))
except ValueError:
    print("3.5) Not defined")

try:
    print("3.6) " + str(B @ C))
except ValueError:
    print("3.6) Not defined")

try:
    print("3.7) " + str(C @ B))
except ValueError:
    print("3.7) Not defined")

try:
    print("3.8) " + str(np.linalg.matrix_power(B, 4)))
except ValueError:
    print("3.8) Not defined")

try:
    print("3.9) " + str(A @ A.T))
except ValueError:
    print("3.9) Not defined")

try:
    print("3.10) " + str(D.T @ D))
except ValueError:
    print("3.10) Not defined")