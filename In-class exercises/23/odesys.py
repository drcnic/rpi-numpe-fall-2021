"""odesys.py -- """
import numpy as np
from scipy.optimize import root

def runge_kutta_4th(func, tspan, u0, num_steps):
    """
    Solves system of ODEs using classical Runge-Kutta method

    Parameters
    ----------
    func : Python function
        function representing F(u,t)
    tspan : 1D array
        initial time and final time
    u0 : 1D array
        ODE system initial condition
    num_steps : int
        number of time steps

    Raises
    ------
    ValueError

    Returns
    -------
    t : 1D np array
        collection of every t value.
    u : 2D np array
        approximated solution to ODE system.

    """
    
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1)
    u = np.zeros((u0.size,t.size))
    
    for i in range(0, u0.size):
        u[i,0] = u0[i]
    
    for i in range(0, num_steps):
        dt = t[i+1] - t[i]
        
        #k1 = del_t * func(y[i], t[i])
        #k2 = del_t * func(y[i] + 0.5*k1, t[i] + 0.5*del_t)
        #k3 = del_t * func(y[i] + 0.5*k2, t[i] + 0.5*del_t)
        #k4 = del_t * func(y[i] + k3, t[i] + del_t)
        #y[i+1] = y[i] + (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
        #k1 = np.zeros((u0.size,t.size))
        #k2 = np.zeros((u0.size,t.size))
        #k3 = np.zeros((u0.size,t.size))
        #k4 = np.zeros((u0.size,t.size))
        
        k1 = dt * func(u[:,i], t[i])
        k2 = dt * func(u[:,i] + 0.5*k1, t[i] + 0.5*dt)
        k3 = dt * func(u[:,i] + 0.5*k2, t[i] + 0.5*dt)
        k4 = dt * func(u[:,i] + k3, t[i] + dt)
        
        #u[:,i+1] = u[:,i] + dt * func(u[:,i], t[i])
        u[:,i+1] = u[:,i] + (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t, u

def trapezoidal(A, tspan, u0, num_steps):
    """
    Solves system of ODEs using the trapezoidal method

    Parameters
    ----------
    A : square 2D np array, appears in du/dt = Au
        function representing F(u,t)
    tspan : 1D array
        initial time and final time
    u0 : 1D array
        ODE system initial condition
    num_steps : int
        number of time steps

    Raises
    ------
    ValueError

    Returns
    -------
    t : 1D np array
        collection of every t value.
    u : 2D np array
        approximated solution

    """
    
    if (tspan[0] > tspan[1] or num_steps < 1) or u0.size != A.shape[1]:
        raise ValueError
    
    t = np.linspace(tspan[0], tspan[1], num_steps+1)
    u = np.zeros((u0.size,t.size))
    
    dt = t[1] - t[0]
    idnt = np.eye(u0.size)
    
    u[:,0] = u0[:]
    #for i in range(0, u0.size):
    #    u[i,0] = u0[i] 
    
    M       = idnt + 0.5*dt*A
    M_inv   = np.linalg.inv(idnt - 0.5*dt*A)
    N = M @ M_inv
    
    
    for i in range(0, num_steps):
        u[:,i+1] = N @ u[:,i]
        
    return t, u

def backward_euler(func, jac, tspan, u0, num_steps):
    """
    Solves system of ODEs using backward euler

    Parameters
    ----------
    func : Python function
        Function representing F(u, t)
    jac : Python function
        Function returning partial of F with respect to u
    tspan : 1D array
        start and end times
    u0 : 1D array
        initial guess column
    num_steps : int
        number of steps between start and end time

    Returns
    -------
    t : 1D array
        times
    u : 2D array
        approximated solutions

    """
    if (tspan[0] > tspan[1] or num_steps < 1):
        raise ValueError
        
    t = np.linspace(tspan[0], tspan[1], num_steps+1)    
    u = np.zeros((u0.size, t.size))
    u[:,0] = u0[:]
    
    for i in range(0, num_steps):
        dt = t[i+1] - t[i]
        f = lambda x : x - u[:,i] - dt * func(x, t[i+1])
        jac_f = lambda x : np.eye(u.shape[0]) - dt * jac(x, t[i+1])
        res = root(f, u[:,i], jac=jac_f)
        u[:,i+1] = res.x
        

    return t, u