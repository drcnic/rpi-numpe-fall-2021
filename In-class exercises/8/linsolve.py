"""Module with useful functions for solving linear systems"""

import numpy as np
from math import isnan

def forward_sub(lu_fac, b):
    """
    Does forward substitution to solve linear systen Ly = b

    Parameters
    ----------
    lu_fac : 2D numpy array, matrix L
        
    b : 1D numpy array, matrix b

    Returns solved y

    """
    
    # Ly = b
    # number of elements in y = columns of L OR number of elements in b

    n = len(b)
    y = np.zeros(n) # init array y 
    
    for i in range(0, n):
        sum_ = 0.0
        for j in range(0, i):
            sum_ -= lu_fac[i][j]*y[j]
        y[i] = b[i] + sum_
        
    return y
    

def back_sub(lu_fac, y):
    """
    Does backward substitution to solve linear systen Ux = y

    Parameters
    ----------
    lu_fac : 2D numpy array, matrix U
        
    y : 1D numpy array, matrix y

    Returns solved x

    """
    
    n = len(y)
    x = np.zeros(n) # init array x
    
    # fuck :( 
    lu_fac = lu_fac.astype(float)
    y = y.astype(float)
    x = x.astype(float)
    
    
    
    for i in range(n-1, -1, -1): # row
        x[i] = y[i]
        
        for j in range(i+1, n): # col
            x[i] -= lu_fac[i][j]*x[j]

        x[i] = x[i]/lu_fac[i][i]


    return x
    
    

def lu_factor(A, tol=1.0e-15):
    '''
    Given a matrix A, returns the LU decomposition of said 
    matrix and stores the upper and lower triangular systems 
    in the original matrix variable

    Parameters
    ----------
    A : Numpy matrix of nxn size

    Returns
    -------
    None.

    '''
    assert(A.shape[0] == A.shape[1])
    
    
    A.astype(float)
    
    n = A.shape[0]

    for k in range(0, n-1):
        assert(abs(A[k,k]) > tol)
        A[k+1:, k] = A[k+1:, k] / float(A[k,k])
        
        for j in range(k+1, n):   # col
            for i in range(k+1, n):   # row
                A[i,j] -= A[i,k]*A[k,j]
                
        if abs(A[k,k] <= tol):
            A[k,k] = 0
            
    return True
    

def solve(A, b, tol=1.0e-15):
    """
    Solves for matrix x in linear system Ax=b

    Parameters
    ----------
    A : np array
        nxn matrix
    b : np array
        nx1 vector
    tol : float, optional
        Tolerance for setting components to zero. The default is 1.0e-15.

    Returns
    -------
    nx1 np array (x)

    """
    lu_factor(A, tol)
    if(np.isnan(np.sum(A))):
        raise RuntimeError("Function in lu_factor failed.")
        exit()
    return(back_sub(A, forward_sub(A, b)))
    
    







