"""shell_transmission.py -- """

import numpy as np
import find_root as fr
from numpy import sin, cos
from random import random
from math import pi, sqrt, log

def random_trajectory():
    """
    Randomly selects and returns two angles (in rad) that define a 3D trajectory vector (omega)

    Returns
    -------
    theta : float
        Angle from z axis on z-y plane; the polar angle. Domain: [0, 2pi]
    phi : float 
        Angle from x axis on x-y plane; the azimuthal angle. Domain: [0, 2pi]

    """
    theta   = (np.pi) * random()
    phi     = (2.*np.pi) * random()
    
    return theta, phi
    
def random_distance_to_collision(Sig_t):
    """
    Calculates a random distance for a neutron to travel

    Parameters
    ----------
    Sig_t : float
        Total probability of interaction per unit length traversed;
        sum of Sig_a and Sig_s

    Raises
    ------
    ValueError
        Sig_t must be greater than 0.

    Returns
    -------
    s : float
        Random magnitude of distance traveled, greater than 0

    """
    if (Sig_t <= 0):
        raise ValueError("Sig_t must be greater than 0")
    
    x = 0.
    while (x == 0):
        x = random()
    
    s = -np.log(1-x) / float(Sig_t)
        
    return s
    
def DxDyDz(s, theta, phi):
    """
    Calculates the change in cartesion coordinates of a neutron

    Parameters
    ----------
    s : float
        Magnitude of distance travelled
    theta : float
        Angle from z axis on z-y plane; the polar angle. Domain: [0, 2pi]
    phi : float 
        Angle from x axis on x-y plane; the azimuthal angle. Domain: [0, 2pi]

    Returns
    -------
    direc : 1D np array, float
        Coordinate changes in x, y, z respectively

    """
    direc = np.zeros(3)   # 0-x, 1-y, 2-z
    direc[0] = s * sin(theta) * cos(phi)
    direc[1] = s * sin(theta) * sin(phi)
    direc[2] = s * cos(theta)
    
    return direc
    
def collision_event(Sig_s, Sig_a):
    """
    Determines whether the collision was an absorbtion or scatter event

    Parameters
    ----------
    Sig_s : float
        Probability from 0-1 that the neutron scatters.
    Sig_a : float
        Probability from 0-1 that the neutron is absorbed.

    Returns
    -------
    bool
        True if neutron scatter; false if neutron absorbtion.

    """
    prob_scatter = (float(Sig_s) / (Sig_s+Sig_a)) # fraction of neutrons that are scattered
    
    
    if (prob_scatter < random()):
        return False
    return True
    
def shell_transmission(Sig_s, Sig_a, Ri, Ro, N):
    """
    Simulates the random walk of N neutrons in the sphere

    Parameters
    ----------
    Sig_s : float
        Probability that the neutron scatters.
    Sig_a : float
        Probability that the neutron is absorbed.
    Ri : float
        Inner radius of shell
    Ro : float
        Outer radius of shell
    N : int
        Number of neutrons to simulate

    Returns
    -------
    arr: 1D np array, int
        Cumulative number of transmissions by n neutrons

    """
    arr = np.zeros(N)
    Sig_t = Sig_a + Sig_s
    cum_nt = 0  # cumulative number of transmissions
    
    for n in range(0, N):
        
        n_loc = np.array([0.,0.,0.])    # starting location of each neutron
        theta, phi = random_trajectory()
        n_loc = DxDyDz(Ri, theta, phi)
        
        while(True): # note: should probably have an iteration cap
            if (not collision_event(Sig_s, Sig_a)): 
                # if the neutron is absorbed, start a new one
                break
            
            n_s = random_distance_to_collision(Sig_t)   # random magnitude of travel distance this iter
            n_theta, n_phi = random_trajectory()        # random angles of travel this iter
            delta = DxDyDz(n_s, n_theta, n_phi)         # anticipated neutron position change this iter    
            loc_test = n_loc + delta                    # anticipated neutron position after this iter
            
            dist = sqrt(loc_test[0]**2 + loc_test[1]**2 + loc_test[2]**2) # distance of neutron at new position from sphere center
            
            if (dist < Ri):
                # neutron is inside inner sphere -> 
                f = lambda s: (n_loc[0] + s * sin(n_theta) * cos(n_phi))**2 + (n_loc[1] + s * sin(n_theta) * sin(n_phi))**2 + (n_loc[2] + s * cos(n_theta))**2 - Ri**2
                new_n_s = fr.bisection(f, 0, Ri)
                n_loc += DxDyDz(new_n_s, n_theta, n_phi)
                continue    
                    
            elif (dist > Ri and dist < Ro):
                # netron is inside shell material -> continue journey
                n_loc = loc_test
                continue
            
            elif (dist > Ro):
                # neutron outside of sphere -> transmission
                cum_nt += 1
                break
            
        arr[n] = cum_nt
        
    
    return arr