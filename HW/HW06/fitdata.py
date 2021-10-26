"""Module that can fit a polynomial of given degree for a given set of data"""
import numpy as np

def calc_fit(xdata, ydata, degree=1):
    """
    Finds the polynomial that best fits the data in a least
    squares sense

    Parameters
    ----------
    xdata : 1D numpy array
        Denotes the abscissae of a given data set.
    ydata : 1D numpy array
        Denotes the oordinates of a given data set.
    degree : int, optional
        Degree of the polynomial used to fit data. The default is 1.

    Returns
    -------
    Coefficients of polynomial function

    """
    
    assert (degree >= 0), "Polynomial degree must be non-negative."
    assert (xdata.ndim == 1 and ydata.ndim == 1), "Data arrays must be one-dimensional."
    assert (ydata.size == xdata.size), "ydata and xdata arrays must have the same number of elements."
    
    
    coeff = np.zeros(degree + 1, dtype=float)    # deg 0: non-zero constant; deg 1: linear (two coeffs)
                                    # for 2 degree polynomial, coeff has the order c0+c1x+c2x^2 = f(x)
    
    # xdata and ydata are both one-dimensional arrays
    # need to make system Ax = b, where matrix x is coefficients and matrix b are ydata values
    #   for a 2 degree polynomial, given a set of ordered pairs:
    #       c0 + c1*x + c2*x^2 = f(x)   
    #          
    #       ydata[0] = c0 + c1*xdata[0] + c2*xdata[0]^2
    #       ydata[1] = c0 + c1*xdata[1] + c2*xdata[1]^2
    #       ydata[2] = c0 + c1*xdata[2] + c2*xdata[2]^2
    #    
    #   x = [ C0 ],  b = [ ydata[0] ],  A = [ 1, xdata[0], xdata[0]^2 ],
    #       [ C1 ],      [ ydata[1] ],      [ 1, xdata[1], xdata[1]^2 ], 
    #       [ C2 ]       [ ydata[2] ]       [ 1, xdata[2], xdata[2]^2 ]
    # 
    # Ax = b: multiply rows of A by columns of x
    # so, entire left col of A should be 1 for constant coeff
    
    A = np.zeros(shape=(xdata.size, degree + 1), dtype=float)
    A.fill(1.)
    
    # loop through all x values and create an entry in each row of a matrix, A
    for row in range(0, xdata.size):  
        for col in range(1, degree+1): # skipping the first col -- it's already equal to 1 
            A[row, col] = xdata[row]**col
    
    # now we have A, for the equation Ax = b
    # where x is the vector of coefficients we want to solve for, and vector b is ydata
            
    q, r = np.linalg.qr(A)              # QR decomposition
    
    #print(A)
    #print(q)
    #print(r)
    
    coeff = back_sub(r, q.T @ ydata)    # lol what?
    
    return coeff
    
def eval_fit(coeff, x):
    """
    Given best fit coefficients and a set of x values, calculates the corresponding
    y-values.

    Parameters
    ----------
    coeff : 1D numpy array
        Coefficients for line of best fit
    x : 1D numpy array
        X-data points to be tested

    Returns
    -------
    1D numpy array, consisting of y-data points corresponding to given x-data

    """
    y = np.zeros(x.size, dtype=float)
    
    for i in range(0, x.size):
        y[i] = coeff[0]
        for j in range(1, coeff.size):
            y[i] += coeff[j]*x[i]**j
    
    return y
    
def back_sub(U, b):
    """
    Does backward substitution to solve linear systen Ux = y

    Parameters
    ----------
    U : 2D numpy array, matrix U
        
    b : 1D numpy array, matrix y

    Returns solved x

    """
    
    n = len(b)
    x = b.copy() # init array x
 
    U = U.astype(float)
    b = b.astype(float)
    x = x.astype(float)
    
    
    
    for i in range(n-1, -1, -1): # row
        for j in range(i+1, n): # col
            x[i] -= U[i,j]*x[j]

        x[i] /= U[i,i]


    return x


#calc_fit(np.array([1., 2., 3.]), np.array([1., 1., 1.]), 1)


