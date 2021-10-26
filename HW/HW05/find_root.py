"""module with utilities for determining the roots of functions"""

import numpy as np


def bisection(func, xlow, xupp, ftol = 1.0e-12, xtol = 1.0e-7, maxiter=100):
    """
    Using the bisection method, determines the root of a function

    Parameters
    ----------
    func : Python function
        Python function that returns a value
    xlow : float
        Lower bound to test
    xupp : float
        Upper bound to test
    xtol : float, optional
        Tolerance for the minimum difference in xupp and xlow. The default is 1.0e-7.
    ftol : float, optional
        Tolerance for the minimum value of func(f_m). The default is 1.0e-12.
    maxiter : int, optional
        Max number of iterations. The default is 100.

    Returns
    -------
    Root of the function within given bounds.

    """
    
    assert (xlow < xupp)    # check that bounds are correct
    assert (abs(func(xlow)) - xtol != 0 and abs(func(xupp)) - xtol != 0)    # make sure user did not supply exact root
    assert (func(xlow)*func(xupp) < 0)
    assert (maxiter >= 1 and maxiter <= 1000)   # max iterations must be at least 1 and at most 1000
    
    i = 0
    while(i <= maxiter):
        i += 1
        
        x_m = (xlow + xupp) / 2. # initial x_m value
    
        f_lo = func(xlow)
        f_hi = func(xupp)
        f_m  = func(x_m)
        
        if (f_lo*f_m < 0):
            # the root is between xlow and x_m
            xupp = x_m
            continue
            
        if (f_lo*f_m > 0):
            # the root is between x_m and xupp
            xlow = x_m
            continue
        
        if (f_lo*f_m == 0 or abs(xupp-xlow) < xtol or abs(f_m) < ftol):
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