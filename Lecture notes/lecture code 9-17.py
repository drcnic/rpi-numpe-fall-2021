import numpy as np


# 2x2 matrices
#   LU = A
#   AL^-1 = U
#   let L^-1 =M
#   MA = U
#
#
#
#
A = np.array([ [1.0, 2.0], [3.0, 4.0] ])
M = np.eye(2)   # makes a 2x2 identity matrix
M[1][0] -= A[1][0]/A[0][0]
U = M @ A   # @ is matrix multiplication

# L^-1 = M
# therefore, L = M^-1
# need to invert matrix M: negate every element below the main diagonal
L = np.eye(2)
L[1][0] = -M[1][0]


# 3x3 and larger matrices
#   A clever feature of LU decomposition is that L and
#   U can be constructed from A while storing their elements 
#   directly in A as the construction proceeds. Thus, only 
#   one array needs to be stored
#
#   L is stored in the strictly lower part of lu_fac:
#       L[i][j] = lu_fac[i][j] if i > j
#       The ones on the diagonal of L are implied (L[i][i] = 1)
#   U is stored in the upper part of lu_fac
#       U[i][j] = lu_fac[i][j] if i < j
A = np.array([ [1.0,  2.0,  3.0],
               [4.0, 13.0, 18.0],
               [7.0, 54.0, 78.0] ])
M1 = np.eye(3)
M1[1:, 0] -= A[1:,0]/A[0,0]\

    
A = np.array([ [1.0,  2.0,  3.0],
               [4.0, 13.0, 18.0],
               [7.0, 54.0, 78.0],
               [7.0, 54.0, 78.0]])