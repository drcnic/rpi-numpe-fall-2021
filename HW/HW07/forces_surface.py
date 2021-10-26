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
    x_mid, y_mid = np.zeros(num_panels)
    
    for i in range(0, num_panels):
        x_mid[i] = (x[i+1]+x[i])/2.
        y_mid[i] = quad.midpoint(y[i:i+1], x[i+1]-x[i])
                
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
    dfx, dfy = np.zeros(num_panels)
    nx, ny   = np.ones(num_panels)
    
    # get the tip and tail locations of vectors normal to panels
    for i in range(0, num_panels):
        delta_x = x[i+1] - x[i]
        delta_y = y[i+1] - y[i]
        
        slope = delta_y/delta_x
        
        inv_slope = -1.0/slope
        scalar = 1.0/np.sqrt(1.0 + (inv_slope**2))  # we need to divide the vector by the square root of the dot product with itself
        
        nx[i] *= scalar            # normal unit vector, x component
        ny[i]  = inv_slope*scalar  # normal unit vector, y component
        
        #p_mag  = -0.5*(press[i] + press[i+1]) * np.sqrt(delta_x**2 + delta_y**2)
        dfx[i] = -0.5*(press[i] + press[i+1]) * nx[i] * np.sqrt(delta_x**2 + delta_y**2)
        dfy[i] = -0.5*(press[i] + press[i+1]) * ny[i] * np.sqrt(delta_x**2 + delta_y**2)
        
    return dfx, dfy

        
    
    
    