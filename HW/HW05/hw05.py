"hw05.py"
### CLASS NOTES
# red points are where forces are in equilibrium
# gravitational and centripetal forces balances at those points
# if you put an object in those points, it will remain there forever; objects collect there
#   interesting point: nasa put james webb satellite there to shield it from sun heat
# given force balance equation for point L2 in doc
#   gravitational forces and centripetal forces
#   find r such that the relation holds
from find_root import bisection
import numpy as np

m1 = 1.9885e30  # mass of the sun (kg)
m2 = 5.9724e24  # mass of the earth (kg)
R  = 1.49496e11 # distance between the sun and earth (m), also 1 au

def lagrange2_residual(m1, m2, R, r):
    """
    Calculates and returns the residual value of force-balance equation given a distance value, r

    Parameters
    ----------
    m1 : float
        Mass of body 1. Of the two masses, this one should be greater.
    m2 : float
        Mass of body 2.
    R : float
        Center-to-center distance between bodies.
    r : float
        Distance between body with mass m2 and a satellite of negligible mass

    Returns
    -------
    residual: float
        Residiual value of function for given r

    """

    #residual = ( (((m1)/(m1+m2)*R)+r) * ((m1+m2)/(R**3)) ) - ((m1)/(R+r)**2) - m2/r**2
    residual = -( (((m1)/(m1+m2)*R)+r) * ((m1+m2)/(R**3)) ) + ((m1)/(R+r)**2) + m2/r**2     # this one looks more like sample plot
    
    return residual

root = bisection(lambda r: lagrange2_residual(m1, m2, R, r), 0.01, R)

# Bounds for finding root of lagrange equation
r_lower = 0.    # starting at zero: a little weird because division by zero, but the code runs
r_upper = R/65. # determined via inspection of residual graph

r_vals = np.linspace(r_lower, r_upper, 100) # 100 iterations gives satisfactory line resolution
resid_vals = np.zeros(r_vals.size)

# calculate residual values for each r-value
for i in range(0, resid_vals.size):
    resid_vals[i] = (lagrange2_residual(m1, m2, R, r_vals[i]))



# do not let subimtty execute plotting code
Submitty = True
if (not Submitty):
    import matplotlib.pyplot as plt
    plt.figure(1, figsize=(6,4))
    #plt.rcParams["figure.autolayout"] = True
    
    plt.title("L2 of Sun/Earth system (niclad)")
    plt.xlabel("r [AU]")
    plt.ylabel("L2 Residual f(r)")
    plt.grid()
    
    plt.axis([r_lower-0.001, r_upper/R, -5e6, 5e7]) # x-axis in AU
    
    plt.plot(r_vals/R, resid_vals, label="f(r)")                                    # plot data with r converted to AU
    plt.plot(root/R, 0, 'r.', markersize=14, label="L2 at " + "{:.2e}".format(root/R) + "AU")  # plot point L2
    plt.plot(0, 0, 'c.', markersize=28, label="Earth")                              # plot point representing earth
    
    plt.legend()

    plt.savefig("hw05_plot.png", dpi=300, edglecolor='none')
    plt.show()