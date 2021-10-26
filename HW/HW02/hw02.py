import numpy as np
from math import pi, sqrt


# evaluate bending moment and torque on the tower
# due to a potential imbalance in the accumulated mass

g = -9.81    # accel due to gravity


def dot_product(vec1, vec2):
    """
    Calculates and returns the dot product of two vectors
    
    Input:
        
    Output:
        

    """
    
    dot = 0.0
    
    for i in range(len(vec1)):
        dot += vec1[i]*vec2[i]
    
    return dot

def cross_product(a, b):
    """
    Calculates and returns the cross product of two vectors
    a x b
    
    Input:
        
        
    Output:
        

    """
    
    #clunky and lazy-- assume 1D array with 3 elements
    vec = np.zeros(3)
    
    vec[0] = a[1]*b[2] - a[2]*b[1]  #   *
    vec[1] = a[2]*b[0] - a[0]*b[2]  # brute force it!
    vec[2] = a[0]*b[1] - a[1]*b[0]  #   *
    
    return vec

def tower_moment_torque(m, rBG, h, b, omega):
    """
    Calculates the moment and torque
    
    
    
    
    
    Input:
        
    Output:
        

    """
    #M = np.zeros(3)
    #T = 0.0
    
    
    ### Getting resultant force at G
    W   = np.zeros(3) # weight force vector of the rotor
    Fc  = np.zeros(3) # centripetal force 
    
    W[2] = m*g
    Fc = (m)*(omega*omega)*(rBG)
    F = Fc + W
    
    #print(W)
    #print(Fc)
    #print(F)
    
    ### Calculating moment at O
    rOG = np.array([0, -b, h]) + rBG 
    M = cross_product(rOG, F)
    
    #print(rBG)
    #print(rOG)
    #print(M)
    
    ### Moment about line OA
    
    T = dot_product([0,0,1.], cross_product([0, -b, 0], F))
    #print(T)
    
    return M, T



m   = 1000. #kg
rBG = np.array([0.03, 0.0, -0.04])   # m
h   = 135 # m
b   = 1.2 # m
omega = 10. * pi # rad/s

bend_moment, torque = tower_moment_torque(m, rBG, h, b, omega)

