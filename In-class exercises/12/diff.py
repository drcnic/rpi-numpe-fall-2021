import numpy as np
from math import factorial

def finite_diff(y, h):
    """
    

    Parameters
    ----------
    y : 1D numpy array
        y data.
    h : float, optional
        Spacing of the data. The default is 1.0.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    dydx : 1D numpy array
        Array of finite-difference approximations of the first derivative

    """
    
    if (h <= 0):
        raise ValueError
    
    dydx = np.zeros(y.size)
    dydx[0] = (y[1] - y[0])/h
    
    for i in range(1, y.size - 1):
        dydx[i] = (y[i+1]-y[i-1])/(2.*h)
        
    dydx[y.size - 1] = (y[y.size-1] - y[y.size-2])/h
    
    return dydx


def fd_formula(x, deriv=1):
    """
    Return a set of specified order central difference coefficients for h=1

    Parameters
    ----------
    x : 1D np array
        Array of x-values
    deriv : int, optional
        The desired order of coefficients. The default is 1.

    Raises
    ------
    TypeError
        DESCRIPTION.
    ValueError
        DESCRIPTION.

    Returns
    -------
    coef : 1D np array
        The array of calculated coefficients.

    """
    if (type(deriv) != int):
        raise TypeError
    if (deriv < 0):
        raise ValueError
    if (deriv > x.size-1):  # why? because matrices won't match up for multiplication otherwise
        raise ValueError
    
    # linear system A*coeff = b where
    #   A is array built from x-values
    #   coeff is array of the constants
    #   b is the array of answers to linear system, where qth entry is q factorial
    
    A = np.zeros([x.size,x.size]) # x.size by x.size array
    A[0,:] = 1.
    
    coef = np.zeros(x.size)
    
    b = np.zeros(x.size)
    b[deriv] = factorial(deriv)
    
    for i in range(1, x.size):
        for j in range(0, x.size):
            A[i,j] = x[j]**i
    
    coef = np.linalg.solve(A, b)
    
    return coef
    