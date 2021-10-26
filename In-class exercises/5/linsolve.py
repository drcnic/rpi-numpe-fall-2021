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


mtrx =  np.array([ [1.0,  2.0,  3.0],
               [4.0, 13.0, 18.0],
               [7.0, 54.0, 78.0] ])

def lu_factor(A):
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
    
    
    n = A.shape[0]

    for k in range(0, n-1):
        A[k+1:, k] = A[k+1:, k] / A[k,k]
        for j in range(k+1, n):   # col
            for i in range(k+1, n):   # row
                A[i,j] -= A[i,k]*A[k,j]
    return None
    

#print(mtrx)
#lu_factor(mtrx)
#print (mtrx)









