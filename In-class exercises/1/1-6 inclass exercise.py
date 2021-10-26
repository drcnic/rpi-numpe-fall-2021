from math import pi

diameter = 2.0
sm_side = 0.75

a_rect = sm_side*diameter
a_tri  = 0.5*(sm_side**2)
a_circ = 0.5*(pi*(diameter/2.0))

area = a_rect+a_tri+a_circ

print(area)