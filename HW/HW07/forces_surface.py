"""forces_surface -- """
import numpy as np
import quadrature as quad

def panel_midpoints(x, y):
    """
    Computes the midpoint coordinates of each panel

    Parameters
    ----------
    x : 1D numpy array, floats
        x coordinates of panel nodes
    y : 1D numpy array, floats
        y coordinates of panel nodes

    Returns
    -------
    x_mid : 1D numpy array, float 

    y_mid : 1D numpy array, float
                
    """
    
    num_panels = x.size - 1 
    x_mid = np.zeros(num_panels)
    y_mid = np.zeros(num_panels)
    
    for i in range(0, num_panels):
        x_mid[i] = (x[i+1]+x[i])*0.5
        y_mid[i] = (y[i+1]+y[i])*0.5
        #y_mid[i] = quad.midpoint(y[i:i+1], x[i+1]-x[i])
                
    return x_mid, y_mid


# assume the node coordinates x and y are ordered in a counter-clockwise manner over the surface of the body
# in other words, left side of boat hull to right side of boat hull
def panel_midforces(x, y, press):
    """
    Computes the x and y components of the force that each panel experiences

    Parameters
    ----------
    x : 1D numpy array, floats
        x coordinates of panel nodes
    y : 1D numpy array, floats
        y coordinates of panel nodes
    press : 1D numpy array, floats
        coefficient of pressure measured at each of the panel nodes.

    Returns
    -------
    dfx : 1D numpy array, floats 
        approximate pressure-force components on panels in x dir
    dfy : 1D numpy array, floats
        approximate pressure-force components on panels in y dir

    """
    
    num_panels = x.size - 1 
    dfx = np.zeros(num_panels)
    dfy = np.zeros(num_panels)
    nx = np.ones(num_panels)
    ny = np.ones(num_panels)
    
    # get the tip and tail locations of vectors normal to panels
    for i in range(0, num_panels):
        delta_x = x[i+1] - x[i]
        delta_y = y[i+1] - y[i]
        
        slope = delta_y/delta_x
        
        inv_slope = -1.0/slope
        
        length = np.sqrt(delta_x**2 + delta_y**2) # delta s
        dfx[i] = -0.5*(press[i] + press[i+1]) * delta_y
        dfy[i] = -0.5*(press[i] + press[i+1]) * -delta_x 

    return dfx, dfy

def integrate_forces(dfx, dfy):
    """
    Numerically integrates panel forces using midpoint method

    Parameters
    ----------
    dfx : 1D np array, floats
        array of x component forces on each panel
    dfy : 1D np array, floats
        array of y component forces on each panel

    Returns
    -------
    force_x : float
        scalar net force in x direction
    force_y : float
        scalar net force in y direction

    """


    force_x = quad.midpoint(dfx, 1.0) 
    force_y = quad.midpoint(dfy, 1.0) 
    
    return force_x, force_y
     
    

        
    
    
    