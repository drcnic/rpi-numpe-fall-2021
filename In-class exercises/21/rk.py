"""rk.py -- numerical IVP solving methods"""

import numpy as np

def explicit_midpoint(func, tspan, y0, num_steps):
    """
    Solve IVP using explicit midpoint method    

    Parameters
    ----------
    func : Python function
        Function representing F(y,t) and takes the arguments y and t in that order
    tspan : np array
        t start and end values: tspan[0] = 𝑡0 and tspan[1] = 𝑡𝑓;
    y0 : float
        Initial y value
    num_steps : int
        number of time steps 

    Raises
    ------
    ValueError

    Returns
    -------
    t : 1D np array
        Array of t values for each step
    y : 1D np array
        Array of estimated y values for each t value

    """
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
    
    #t = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1) 
    y[0] = y0
    
    for i in range(0, num_steps):
        del_t = t[i+1] - t[i]
        k1 = del_t * func(y[i], t[i])
        k2 = del_t * func(y[i] + 0.5*k1, t[i] + 0.5*del_t)
        y[i+1] = y[i] + k2
        
    return t, y


def runge_kutta_4th(func, tspan, y0, num_steps):
    """
    Solves IVP using classical 4th-order RK scheme

    Parameters
    ----------
    func : Python function
        Function representing F(y,t) and takes the arguments y and t in that order
    tspan : np array
        t start and end values: tspan[0] = 𝑡0 and tspan[1] = 𝑡𝑓;
    y0 : float
        Initial y value
    num_steps : int
        number of time steps 

    Raises
    ------
    ValueError

    Returns
    -------
    t : 1D np array
        Array of t values for each step
    y : 1D np array
        Array of estimated y values for each t value

    """
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
        
    y = np.zeros(num_steps + 1)
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1) 
    y[0] = y0
    
    for i in range(0, num_steps):
        del_t = t[i+1] - t[i]
        k1 = del_t * func(y[i], t[i])
        k2 = del_t * func(y[i] + 0.5*k1, t[i] + 0.5*del_t)
        k3 = del_t * func(y[i] + 0.5*k2, t[i] + 0.5*del_t)
        k4 = del_t * func(y[i] + k3, t[i] + del_t)
        y[i+1] = y[i] + (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t, y