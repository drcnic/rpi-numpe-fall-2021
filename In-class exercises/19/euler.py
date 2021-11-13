"""euler.py -- """

import numpy as np

def forward_euler(func, tspan, y0, num_steps):
    """
    

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
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1)
    y = np.zeros(num_steps+1)
    y[0] = y0
    
    delta_t = (tspan[1] - tspan[0]) / float(num_steps)
    
    for i in range(0, num_steps):
        y[i+1] = y[i] + delta_t*func(y[i], t[i])
    
    return t, y

def backward_euler(func, tspan, y0, num_steps):
    """
    


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
    
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1)
    y = np.zeros(num_steps+1)
    y[0] = y0
    
    delta_t = (tspan[1] - tspan[0]) / float(num_steps)
    
    for i in range(0, num_steps):
        G = lambda x : x - y[i] - delta_t*func(x, t[i+1])
        
        #root = y[i]
        #root_new = root + delta_t * func(t[i+1], root)
        root = np.zeros(3)
        root[0] = y[i]
        root[1] = root[0] + delta_t * func(t[i+1], root[0])
        for j in range(0, 100):
            #df = float(G(root_new) - G(root))/(root_new-root)
            #root_new = root - G(root)/df
            df = float(G(root[1]) - G(root[0]))/(root[1]-root[0])
            root[2] = root[1]
            root[1] = root[0] - G(root[0])/df
            root[0] = root[2]
        
        y[i+1] = root[1]
    
    return t, y