"""A module for the geometry of polygons"""

from math import sqrt

class Polygon(object):
    """An abstract base class for plane figures with at least 3 sides"""
    _num_sides = 0

    def __init__(self, height, width):
        """initialize a polygon of `height` and `width` dimensions"""
        if height < 0.0 or width < 0.0:
            raise ValueError("height and width must be positive.")
        self._h = height
        self._w = width

    def get_num_sides(self):
        """returns the number of sides the polygon has"""
        return self._num_sides

    def calc_area_perimeter_ratio(self):
        """returns the ratio of the polygon's area to its perimeter"""
        return self.calc_area()/self.calc_perimeter()


class RightTriangle(Polygon):
    """RightTriangle class, extends Polygon"""
    _num_sides = 3
    
    def calc_perimeter(self):
        """Calculate and return perimiter"""
        return self._h + self._w + sqrt(self._h**2 + self._w**2)
    
    def calc_area(self):
        """Calculate and return area"""
        return self._h*self._w*0.5
    
class Rectangle(Polygon):
    """Rectangle class, extends Polygon"""
    _num_sides = 4
    
    def calc_perimeter(self):
        """Calculate and return perimiter"""
        return 2*self._h + 2*self._w 
    
    def calc_area(self):
        """Calculate and return area"""
        return self._h*self._w