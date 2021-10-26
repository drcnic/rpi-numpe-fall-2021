#fsdfs
import numpy as np


def interpolate(xdata, ydata, xeval):
    """
    

    Parameters
    ----------
    xdata : TYPE
        DESCRIPTION.
    ydata : TYPE
        DESCRIPTION.
    xeval : TYPE
        DESCRIPTION.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    yeval : TYPE
        DESCRIPTION.

    """
    if(xdata.size != ydata.size):
        raise ValueError ("xdata and ydata have different lengths")
    
    L = np.ones(xdata.size, dtype=float)
    yeval = np.zeros(xeval.size, dtype=float)
    
    for j in range(0, xeval.size):
        x = xeval[j]
        sum_ = 0.
        for k in range(0, xdata.size):          
            x_k = xdata[k]
            y_k = ydata[k]
            for i in range(0, xdata.size):
                x_i = xdata[i]
                if(i != j):
                    if(abs(x_i - x_k) <= 1.0e-10):
                       raise ZeroDivisionError ("x_i and x_k cannot be equal")
                    L[k] *= (x-x_i)/(x_k-x_i)
        
            sum_ += L[k] * y_k
        yeval[j] = sum_
        
    return yeval