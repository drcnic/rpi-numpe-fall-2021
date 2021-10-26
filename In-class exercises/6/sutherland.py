"""
 sutherland module: contains constants, variables, and functions related to Sutherland's law
"""

C1  = 1.458e-6
S   = 110.4


def calc_viscosity(temp):
    """
    return sutherland viscosity of air of given temperature, 'temp'

    Parameters
    ----------
    temp : float
        temperature of air

    Output: 
        returns the sutherland viscosity of air 

    """
    

    return ( (C1)*(temp)**(3/2) )/(temp + S)


if __name__ == "__main__":
    import sys
    T = float(sys.argv[1])    # convert string to float
    mu = calc_viscosity(T)
    string  = "Viscosity at T = " + '{:.1f}'.format(T)
    string += " [K] is "          + '{:.3e}'.format(mu)
    string += " [kg/m.s]"
    print(string)
