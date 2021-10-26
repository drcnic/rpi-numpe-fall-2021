
"""
 sutherland module: contains constants, variables, and functions related to Sutherland's law
"""

C1  = 1.458e-6
S   = 110.4


def calc_viscosity(temp):
    """
    return sutherland viscosity of air of given temperature in kelvin, 'temp'

    Parameters
    ----------
    temp : float
        temperature of air in kelvin

    Output: 
        returns the sutherland viscosity of air 

    """
    assert (type(temp) == type(1.0) or type(temp) == type(1)), "Temperature must be real numbers"
    assert (temp > 0.0), "Temperature must be positive"

    if (temp < 0.0):
        raise Exception("Temperature must be positive (Kelvin)")



    return ( (C1)*(temp)**(3/2) )/(temp + S)


#mu100 = calc_viscosity("100.")
mu100 = calc_viscosity(-100)
print(mu100)


# python sutherland.py      # assert works
# python -O sutherland.py   # assert will not work





import numpy as np

a = np.linspace(0,20.,11) # create array from 0 to 20 with 11 elements
b = np.ones(a.size)
print(a)
print(b)

for i in range(a.size):
    print(i)
    print("a, b = ", a[i], b[i])
    c = a[i] / b[i]
    
    
    
import unittest
# inherit all the properties (functions) from TestCase class
# into our class named TestSutherland
class TestSutherland(unittest.TestCase):
    """ 
    
    """
    def test_constants(self):
        """
        

        Returns
        -------
        None.

        """
        
        #self.assertTrue(condition)
        #self.assertFalse(condition)
        #self.assertEqual(a,b)
        #self.assertAlmostEqual(a, b, places = 9)
        
        self.assertAlmostEqual(1.458e-6, sutherland.C1, places = 9)
        
    def test_viscosity(self):
        mu = sutherland.calc_viscosity()
        self.assertAlmostEqual(musol, mu, places = 10, msg="Viscosity at 100K is not correct")
        












