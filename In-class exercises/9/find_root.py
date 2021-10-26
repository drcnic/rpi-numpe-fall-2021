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
            