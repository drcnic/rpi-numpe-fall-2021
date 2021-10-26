# Object oriented programming
# Notes from lecture on 10/26
from math import pi

"""Ellipse method"""

class Ellipse():
    """
    Class defining ellipse objects
    
    Data attributes:
            major axis
            minor axis
            orientation
    """
    
    # Class attribute -- same for every single instance!
    _name = "Ellipse" 
    
    def __init__(self, major, minor, orient = 0.0):    # first argument must ALWAYS be self
        """ Constructor method for ellipse class 
        
        Inputs:
                major: major axis 
                minor: minor axis
                orient: (optional) orientation of ellipse (deg)
        """
        self._mj = major
        self._mn = minor
        self._or = orient
        
        return None
    
    def calc_area(self):
        area = pi * self._mj * self._mn
        return area
    
e1 = Ellipse(3.0, 1.0, 0.0)
e1 = Ellipse(4.0, 2.0, 10.0)

ae1 = e1.calc_area()

# if there is an underscore under a class attribute, IT SHOULD NOT BE CHANGED OUTSIDE OF THE CLASS
# USE OBJECT METHODS TO MODIFY ATTRIBUTES


class Student():
    
    
    def __init__(self, RIN):
        self._rin = RIN
        return None
    
    
class Complx():
    """complex numbers"""
    
    def __init__(self, real, imag):
        """Complex number constructor
        
        Input:
            real part
            imag part
        """
        self._r = real
        self._i = imag
        
        return None
    
    def conjugate(self):
        """"""
        cong = Complx(self._r, -self._i)
        return cong
    
    def __str__(self): # special function! Defines what will be printed when you print an object instance!
        """"""
        str1 = '{}'.format(self._r)
        str1 += ', '
        str1 += '{}'.format(self._i)
        return str1
    
    def __add__(self, comp2):   # special function! defines how Complx objects are added!
        """"""
        rr = self._r + comp2._r
        ii = self._i + comp2._i
        cc = Complx(rr, ii)
        return cc
    
    def __eq__(self, comp2): # another special function! describes how 
        """"""
        tol = 1.e-15
        if (abs(self._r - comp2._r) < tol and abs(self._i - comp2._i) < tol):
            return True
        else:
            return False
    
c1 = Complx(1.0, 0.0)
print(c1)   # prints some memory location
        
c1c = c1.conjugate()
print(c1c)
        
        
        
        
        