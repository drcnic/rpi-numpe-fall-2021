"""euler.py -- euler numerical methods module"""

import numpy as np
from math import nan, ceil
from scipy.optimize import root

def forward_euler(func, tspan, y0, num_steps):
    """
    Numerically approximates a function using forward Euler

    Parameters
    ----------
    func : Python function
        Function representing F(y, t)
    tspan : array
        Span of independent variable values; tspan[0] = t0, tspan[1] = tf
    y0 : float
        initial condition of dependent variable
    num_steps : int
        number of independent variable steps (time steps)

    Returns
    -------
    t : float array
        time values
    y : float array
        estimated independent values

    """
    c_num_steps = ceil(num_steps)
    
    if (tspan[0] > tspan[1] or c_num_steps < 1):
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], c_num_steps+1)
    y = np.zeros(c_num_steps+1)
    y[0] = y0
    
    delta_t = (tspan[1] - tspan[0]) / float(c_num_steps)
    
    for i in range(0, c_num_steps):
        y[i+1] = y[i] + delta_t*func(y[i], t[i])
    
    return t, y

def backward_euler(func, tspan, y0, num_steps):
    """
    Numerically approximates a function using backward Euler

    Parameters
    ----------
    func : Python function
        Function representing F(y, t)
    tspan : array
        Span of independent variable values; tspan[0] = t0, tspan[1] = tf
    y0 : float
        initial condition of dependent variable
    num_steps : int
        number of independent variable steps (time steps)

    Returns
    -------
    t : float array
        time values
    y : float array
        estimated independent values

    """
    
    c_num_steps = ceil(num_steps)
    
    if (tspan[0] > tspan[1] or c_num_steps < 1):
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], c_num_steps+1)
    y = np.zeros(c_num_steps+1)
    y[0] = y0
    
    delta_t = (tspan[1] - tspan[0]) / float(c_num_steps)
    
    for i in range(0, c_num_steps):
        G = lambda x : x - y[i] - delta_t*func(x, t[i+1])
        ret = root(G, t[i+1])
        if (ret.success):
            y[i+1] = ret.x
        else: 
            y[i+1] = nan
        
    
    return t, y