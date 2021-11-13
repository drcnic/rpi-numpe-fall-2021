import numpy as np
from scipy.optimize import root


x0 = np.array([0.5, 0.3])

def fun(x):
    f = np.array([ x[0]**4 + 100*x[1]**4 - 1.0, x[0]**3 + x[1] - 1/2 ])    
    return f

def jac(x):
    j = np.ones((2,2))
    j[0,0] = 4*x[0]**3
    j[1,0] = 3*x[0]**2
    j[0,1] = 400*x[1]**3
    j[1,1] = 1
    return j


root = root(fun, x0, jac=jac)
root = root.x