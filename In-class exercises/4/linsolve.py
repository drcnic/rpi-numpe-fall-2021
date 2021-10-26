#
import numpy as np

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
    
    for i in range(n-1, -1, -1): # row
        x[i] = y[i]
        
        for j in range(i+1, n-1): # col
            x[i] -= lu_fac[i][j]*x[j]

        x[i] = x[i]/lu_fac[i][i]

    return x













