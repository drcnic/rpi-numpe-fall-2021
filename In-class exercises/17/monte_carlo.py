""""""

import random
from math import sqrt

def estimate_area(func, xlo, xhi, ylo, yhi, n=100):
    """
    Estimates arbitrary 2D area defined by a function

    Parameters
    ----------
    func : function
        Function of x and y
    xlo : float
        Minimum x value of region
    xhi : float
        Maximum x value of region
    ylo : float
        Minimum y value of region
    yhi : float
        Maximum y value of region
    n : int, optional
        Number of iterations. The default is 100.

    Raises
    ------
    ValueError

    Returns
    -------
    area : float
        estimated area in region

    """
    
    if (n <= 0):
        raise ValueError("n must be greater than zero")
    if (xlo >= xhi or ylo >= yhi):
        raise ValueError
    
    total_A = (xhi-xlo)*(yhi-ylo)
    pts = pts_in = 0
    for i in range(0, n):
        x = (xhi+xlo)*random.random() - xlo
        y = (yhi+ylo)*random.random() - ylo
        
        if (func(x,y) < 0.0):
            pts_in += 1
            
        pts += 1
        
    area = (float(pts_in)/float(pts)) * total_A
    return area

def mc_integral(func, a, b, n):
    """
    Estimates the integral of a given function using monte carlo

    Parameters
    ----------
    func : function
        returns a y value given x
    a : float
        lower x bound
    b : float
        upper x bound
    n : int
        number of random points to use between bounds

    Raises
    ------
    ValueError

    Returns
    -------
    integral : float
        the estimated integral
    sigma : float
        the estimated standard deviation

    """
    
    if (n <= 0):
        raise ValueError
        
    if (a >= b):
        raise ValueError
    
    ac2 = ac = 0.
    for i in range(0, n):
        x = (a+b)*random.random() - a
        ac  += func(x)
        ac2 += func(x)**2
    
    ac  /= n
    ac2 /= n
    
    integral = ac*(b-a)
    sigma = (b-a)*sqrt( (ac2 - ac**2)/n )
    
    return integral, sigma