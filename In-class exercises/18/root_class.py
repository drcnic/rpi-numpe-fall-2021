"""Class for solving nonlinear root-finding problems"""

import numpy as np
from scipy.optimize import root

class NonlinearFunc:
    """Defines a class with methods to find roots of nonlinear functions"""

    def __init__(self, func, pert=1e-5):
        """Creates a new NonlinearFunc to solve func = 0.

        The given function `func` takes in a NumPy 1d array and returns a 1d
        array of the same size.  The optional parameter `pert` defines the
        finite-difference step-size used in the `jacobian` method.
        """
        if (pert <= 0):
            raise ValueError
        
        self._func = func
        self._pert = pert

    def jacobian(self, x):
        """Compute and return the Jacobian of the nonlinear function.

        Uses the second-order central difference method to evaluate the Jacobian
        of the function `self._func`.  The step size used for the finite-
        difference approximation is `self._pert`.  Returns the Jacobian as a 2d
        NumPy array.
        """
        n = x.size
        h = self._pert
        
        jac = np.ndarray((n,n))
        
        xp = x.copy()
        xm = x.copy()
        
        for i in range(0, n):
            xp[i] += h
            xm[i] -= h
            
            fp = self._func(xp)
            fm = self._func(xm)
            
            jac[:,i] = (fp - fm) / (2.*h)
            
            xp = x.copy()
            xm = x.copy()
        
        return jac
        

    def find_root(self, x0):
        """Returns the root of the nonlinear system defined by `self._func`.

        Uses `scipy.optimize.root` to solve for the root of `self._func(x) = 0`.
        The input `x0` is provided as the inital guess for the root.  Returns
        the solution as a NumPy 1d array.
        """
        soln = root(self._func, x0, jac=self.jacobian)
        return soln.x
