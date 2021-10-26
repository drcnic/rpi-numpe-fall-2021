from math import sqrt
class RightTriangle():
    """
    Class describing a right triangle
    """
    _num_sides = 3
    
    
    def __init__(self, height, width): 
        """
        RightTrangle constructor

        Parameters
        ----------
        height : float
            Height of the right triangle. Must be +
        width : float
            Width of the right traignle. Must be +

        Returns
        -------
        None.

        """
        if (height < 0 or width < 0):
            raise ValueError
        
        self._h = height
        self._w = width
    
    def calc_area(self):
        """
        Calculates the area of RightTriangle object

        Returns
        -------
        float
            RightTriangle area

        """
        return self._h*self._w*0.5
    
    def calc_perimeter(self):
        """
        Calculates the perimeter of RightTriangle object

        Returns
        -------
        float
            RightTriangle perimeter

        """
        return self._h + self._w + sqrt(self._h**2 + self._w**2)
        
    