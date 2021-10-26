def calc_viscosity(temp):
    """return sutherland viscosity of air of given temperature, 'temp'"""
    return ( (1.458E-6)*(temp)**(3/2) )/( temp + 110.4)

