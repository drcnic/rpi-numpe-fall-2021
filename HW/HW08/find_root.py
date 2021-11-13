"""find_root.py -- numerical methods for finding roots"""

import numpy as np


def bisection(func, x_lo, x_hi, xtol = 1.0e-7, ftol = 1.0e-12, maxiter=100):
    """
    Using the bisection method, determines the root of a function

    Parameters
    ----------
    func : Python function
        Python function that returns a value
    x_lo : float
        Lower bound to test
    x_hi : float
        Upper bound to test
    xtol : float, optional
        Tolerance for the minimum difference in x_hi and x_lo. The default is 1.0e-7.
    ftol : float, optional
        Tolerance for the minimum value of func(f_m). The default is 1.0e-12.
    maxiter : int, optional
        Max number of iterations. The default is 100.

    Returns
    -------
    Root of the function within given bounds.

    """
    
    
    i = 0
    while(i <= maxiter):
        i += 1
        
        x_m = (x_lo + x_hi) / 2. # initial x_m value
    
        f_lo = func(x_lo)
        f_hi = func(x_hi)
        f_m  = func(x_m)
        
        if (f_lo*f_m < 0):
            # the root is between x_lo and x_m
            x_hi = x_m
            continue
            
        if (f_lo*f_m > 0):
            # the root is between x_m and x_hi
            x_lo = x_m
            continue
        
        if (f_lo*f_m == 0 or abs(x_hi-x_lo) < xtol or abs(f_m) < ftol):
            # x_m is the root
            break
        
    return x_m


def newton(funcdf, x0, ftol=1e-12, xtola=1e-7, maxiter=100):
    """
    Determine a root using Newton's method

    Parameters
    ----------
    funcdf : Python function 
        Function that takes in x and returns f(x) and f'(x) in that order
        ex: f, df = funcdf(x)
    x0 : float
        initial guess for the root
    ftol : float, optional
        The function's proximity to zero tolerance. The default is 1e-12.
    xtola : float, optional
        The absolute convergence tolerance. The default is 1e-7.
    maxiter : int, optional
        The max number of iterations allowed. The default is 100.

    Returns
    -------
    r, n: float, int
        r - estimated root
        n - number of iterations
    """
    r = 0
    n = 0
    
    while( n < maxiter ):
        n += 1
        f, df = funcdf(x0)
        
        try:
            x0 = x0 - (f/df)    # get the new x0
        except ZeroDivisionError:
            n = -n
            break
        
        if(abs(r-x0) <= xtola or (abs(f) <= ftol)):
            break
        
        r = x0
        
    return r, n