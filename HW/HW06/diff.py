"""diff.py -- finite differentiation functions"""

import poly_deriv
import numpy as np

np.seterr(all='raise')
    
def finite_difference(x, y):
    """
    Given arrays of x and y data, returns finite-difference approximations of the first derivative

    Parameters
    ----------
    x : 1D numpy array, float
        x data
    y : 1D numpy array, float
        y data

    Raises
    ------
    ValueError
        x and y data arrays must be the same size

    Returns
    -------
    dydx : 1D numpy array
        Array of finite-difference approximations of the first derivative

    """
    
    if (x.size != y.size):
        raise ValueError("x and y data arrays must be same size")
    
    dydx = np.zeros(y.size)
    
    try:
        # First data point: first-order accurate forward-difference approximation
        dydx[0] = (y[1] - y[0]) / (x[1] - x[0])
    
        # Last data point: first-order backward difference approximation    
        dydx[y.size - 1] = (y[y.size-1] - y[y.size-2])/(x[x.size-1] - x[x.size-2])
    
        # Interior points: use a second-order accurate central difference approx
        for i in range(1, y.size - 1):
            h1 = x[i + 1] - x[i] 
            h2 = x[i] - x[i - 1]
            
            dydx[i] = (h2/(h1+h2)) * ((y[i+1] - y[i])/h1) + (h1/(h1+h2)) * ((y[i] - y[i-1])/h2)
      
    except FloatingPointError:
        print("x values must be unique")
        raise
    
    return dydx
    
    