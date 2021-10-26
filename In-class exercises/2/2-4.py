import numpy 
from math import sqrt

u = numpy.array([0.5, -0.6, 1.3])
dot_prod = 0.0


for x in u:
    dot_prod += x*x
    
u /= sqrt(dot_prod)

print(u)