"""conical_tank.py -- methods and variables related to conical tank drainage problem"""

import numpy as np
from math import nan

# --- physical constants ---
g = 9.80665     # gravitational acceleration (m/s**2)
H = 1.0         # conical tank height (m)
R = 1.5         # conical tank radius (m)
r_0 = 0.02      # conical tank discharge orifice radius (m)
C_d = 0.6       # discharge coefficient (measure of non-ideal losses across discharge orifice, dimensionless)
A_0 = np.pi*(r_0)**2    # area of tank discharge orifice (m**2)


def conical_tank_drain_time():
    """
    Analytically determines the tank drain time based on physical constants

    Returns
    -------
    t : float
        Time it takes for tank to drain, in seconds.

    """
    
    # analytical solution determined by rearranging, integration, and setting h(t) = 0
    t = (2. * R**2 * H**(5./2.)) / (5. * C_d * (r_0)**2 * H**2 * (2*g)**(1./2.))    # time in seconds
    
    return t

def conical_tank_analytical(t):
    """
    Analytical -- computes the height of fluid h(t) in tank given tank physical constants at a time t in seconds

    Parameters
    ----------
    t : float
        Point in time, in seconds.

    Returns
    -------
    h : float
        Height of the water in the conical tank at given time t, in meters.

    """
    
    #
    h = ( ((-5. * C_d * r_0**2 * H**2 * (2*g)**(1./2.)) / (2.*R**2)) * t + H**(5./2.) )**(2./5.)    # height of water in tank, meters
    
    return h

def conical_tank_model(h, t):
    """
    

    Parameters
    ----------
    h : float
        Height of the water in the conical tank at given time t, in meters.
    t : float
        Point in time, in seconds.

    Returns
    -------
    dh_dt : float
        First order differential equation modeling the height of the water draining from the tank.

    """
    if (h <= 0):
        return nan
    
    dh_dt = (-C_d * A_0 * (2.*g*h)**(1./2.)) / (np.pi * ((h*R)/H)**2.)
    return dh_dt
    