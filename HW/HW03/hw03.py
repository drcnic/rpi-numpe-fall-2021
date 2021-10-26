# forward sub factor backsub
# G t = f
import numpy as np
from linsolve import solve

debug = False

def truss_geometry(L_GA, L_GD):
    """
    Creates matrix G using geometric relationships of truss

    Parameters
    ----------
    L_GA : float
        length of member GA
    L_GD : float
        length of member GD

    Returns
    -------
    G : np array
        linear system matrix    
    
    """
    
    theta1 = np.arctan(L_GA/L_GD)
    L_BF = (2.0/3.0)*(L_GA) # triangle similarity
    theta2 = np.arctan(L_BF/(L_GD/3.))
    
    if (debug):
        print(theta1)
        print(L_BF)
        print(theta2)
        print()
        
        
    S1 = np.sin(theta1)
    S2 = np.sin(theta2)
    C1 = np.cos(theta1)
    C2 = np.cos(theta2)
    
    G = np.zeros([14, 14])
    G = np.array([ 
                    [ C1,   0,   0,  0,  0,  0,  0,   0,  0,   0,  0, 1, 0, 0],
                    [-S1,   0,   0,  0,  0,  0, -1,   0,  0,   0,  0, 0, 1, 0],
                    [-C1,  C1,   0,  0,  0,  0,  0, -C2,  0,   0,  0, 0, 0, 0],
                    [ S1, -S1,   0,  0,  0,  0,  0, -S2, -1,   0,  0, 0, 0, 0],
                    [  0, -C1,  C1,  0,  0,  0,  0,   0,  0, -C1,  0, 0, 0, 0],
                    [  0,  S1, -S1,  0,  0,  0,  0,   0,  0, -S1, -1, 0, 0, 0],
                    [  0,   0, -C1, -1,  0,  0,  0,   0,  0,   0,  0, 0, 0, 0],
                    [  0,   0,  S1,  0,  0,  0,  0,   0,  0,   0,  0, 0, 0, 0],
                    [  0,   0,   0,  1, -1,  0,  0,   0,  0,   0,  0, 0, 0, 0],
                    [  0,   0,   0,  0,  0,  0,  0,   0,  0,   0,  1, 0, 0, 0],
                    [  0,   0,   0,  0,  1, -1,  0,   0,  0,  C1,  0, 0, 0, 0],
                    [  0,   0,   0,  0,  0,  0,  0,   0,  1,  S1,  0, 0, 0, 0],
                    [  0,   0,   0,  0,  0,  1,  0,  C2,  0,   0,  0, 0, 0, 1],
                    [  0,   0,   0,  0,  0,  0,  1,  S2,  0,   0,  0, 0, 0, 0]
                 ])
    
    
    return G
    
    

def shuffle_Ab(A, b, order):
    """
    Shuffles rows of matrix A and vector b given an order matrix

    Parameters
    ----------
    A : np array
        Linear system matrix
    b : np array
        Linear system vector
    order : np array
        

    Returns
    -------
    new_A : np array
        Re-ordered linear system matrix
    new_b : np array
        Re-ordered linear system vector

    """
    new_A = np.copy(A)
    new_b = np.copy(b)
    
    for i in range(0, len(order)):
        new_A[i] = A[order[i]]
        new_b[i] = b[order[i]]
        
    return new_A, new_b

    
def max_magnitude(x):
    """
    Determines and returns the max value (magnitude) and its corresponding index of a 1D array

    Parameters
    ----------
    x : np array
        

    Returns
    -------
    l_indx : int
        index in array where max value is
    l_max : float
        value with greatest magnitude in array

    """
    l_max   = 0.0
    l_indx  = 0
    
    for i in range(0, len(x)):
        if (abs(x[i]) > abs(l_max)):
            l_max  = x[i]
            l_indx = i
    
    return l_indx, l_max


def maximum_force_member(L_GA, L_GD, load, position, L_beam, W_beam, order):
    """
    

    Parameters
    ----------
    L_GA : TYPE
        DESCRIPTION.
    L_GD : TYPE
        DESCRIPTION.
    load : TYPE
        DESCRIPTION.
    position : TYPE
        DESCRIPTION.
    L_beam : TYPE
        DESCRIPTION.
    W_beam : TYPE
        DESCRIPTION.
    order : TYPE
        DESCRIPTION.

    Returns
    -------
    indx : TYPE
        DESCRIPTION.
    mag : TYPE
        DESCRIPTION.

    """
    
    G = truss_geometry(L_GA, L_GD)
    f = applied_load(load, position, L_beam, W_beam)
    
    G2,f2 = shuffle_Ab(G, f, np.array([2,3,7,6,8,10,13,2,11,4,9,0,1,12]))
    
    t = solve(G2, f2)
    indx, mag = max_magnitude(t)
    
    return indx,mag


    
'''Code from Appendix A of Assignment 3'''



def applied_load(load, position, L_beam, W_beam):
    '''Define forces applied to truss based on hoist position and loads.

    Input:  load     - scalar weight of load on hoist plus the hoist [kN]
            position - scalar float position of hoist along beam [meters]
            L_beam   - scalar length of the I beam that the hoist transits [meters]
            W_beam   - scalar weight of the I beam
    Output: f        - 1D numpy float array of applied forces at joints [kN]

    Define 14x1 right side vector of applied forces at joints.

    The weight of the I beam is assumed to be equally shared at the
    two joints F and D.

    The weight of the load (including the hoist) is assumed to be linearly
    distributed between the two joints F and D.  For example,
      - position = 0        => 100% of load is at joint F,   0% at joint D;
      - position = L_beam/4 =>  75% of load is at joint F,  25% at joint D;
      - position = L_beam   =>   0% of load is at joint F, 100% at joint D.
    '''

    # figure out the equations to specify the elements of f, and then make f
    Fd = Ff = W_beam/2
    
    Fd += (position/L_beam)*load
    Ff += (1 - (position/L_beam))*load
    
    f = np.zeros(14)
    f[7]  = Fd
    f[11] = Ff
    
    if (debug):
        print("hoist load [kN] =", load)
        print("hoist position [m] =", position)
        print("I beam length [m], weight [kN] =", L_beam, W_beam)
        print("truss load vector f [kN]:")
        print(f)
        print()

    return f


