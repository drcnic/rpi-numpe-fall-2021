"""quadrature.py -- integral approximation utilities"""

def midpoint(fvals, dx):
    """
    Calculates and returns an approximation of the area under a curve given by fvals using midpoint method    

    Parameters
    ----------
    fvals : 1D numpy array
        values of unkown function f(x)
    dx : float
        x interval between each fval entry

    Raises
    ------
    ValueError
        dx must be positive

    Returns
    -------
    approx : float
        the integral midpoint approximation

    """
    approx = 0.
    
    if (dx <= 0):
        raise ValueError
    
    for i in range(0, fvals.size):
        approx += fvals[i]*dx
    
    # approx *= dx
    
    return approx


def trapezoidal(fvals, dx):
    """
    Calculates and returns an approximation of the area under a curve given by fvals using trapezoidal method    

    Parameters
    ----------
    fvals : 1D numpy array
        values of unkown function f(x)
    dx : float
        x interval between each fval entry

    Raises
    ------
    ValueError
        dx must be positive

    Returns
    -------
    approx : float
        the integral approximation

    """
    if (dx <= 0):
        raise ValueError
    
    approx = fvals[0] + fvals[fvals.size-1]
    
    for i in range(1, fvals.size-1):
        approx += 2*fvals[i] 
        
    approx *= dx / 2.    
    
    return approx
    
    
    