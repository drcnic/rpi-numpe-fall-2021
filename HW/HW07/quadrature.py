"""quadrature.py -- integral approximation utilities"""
import numpy as np

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
    
    
    

def gauss_quad(func, numpts, a=-1, b=1):
    """
    

    Parameters
    ----------
    func : Python function
        Unlike midpoint and trapezoid, func is a python function
    numpts : int
        the number of nodes
    a : float, optional
        integration limit. The default is -1.
    b : float, optional
        integration limit. The default is 1.

    Returns
    -------
    None.

    """
    
    if (not a <= b):
        raise ValueError
        
    s = np.zeros(numpts)
    w = np.zeros(numpts)
    
    if (numpts == 1):
        s = [0.]
        w = [2.]
    elif (numpts == 2):
        s = [-1./np.sqrt(3.), 1./np.sqrt(3.)]
        w = [1.,1.]
    elif (numpts == 3):
        s = [-np.sqrt(3./5.), 0., np.sqrt(3./5.)]
        w = [5./9., 8./9., 5./9.]
    else:
        raise ValueError
    
    approx = 0.0
    for i in range(0, numpts):
        w_i_hat = w[i] * ((b-a)/2.)
        x_i = (b+a)/2. + ((b-a)/2.)*s[i]
        
        approx +=  w_i_hat * func(x_i)
    
    return approx
        
        