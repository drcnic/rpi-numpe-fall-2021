"""Functions for solving an over-determined linear system"""

import numpy as np
import linsolve

def solve_ls(A, b):
    """
    Returns the least squares solution to an over-determined system Ax = b

    Parameters
    ----------
    A : np array
        matrix 
    b : np array
        vector

    Returns
    -------
    least squares solution (np array)

    """
    
    q, r = np.linalg.qr(A)
    
    return linsolve.back_sub(r, q.T @ b)
    
    
    
# A = np.array([[1,2], [3,5], [7,11]])    # a 3x2 matrix
# b = np.array([1, 2, 3]) # a 3-vector
# AtA = A.T @ A   # now we have a 2x2 matrix
# AtB = A.T @ b   # and a 2-vector
