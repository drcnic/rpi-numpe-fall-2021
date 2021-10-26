from angles import theta
from math import sin, cos, pi, sqrt

# applied force: 450N
# 30-60-90 truss
# BC length: 0.6m
# 20 < theta < 100

F = 450
theta_R = theta*(pi/180)

#print(theta)
#print(theta_R)

# joint C
Fx = F*cos(pi+theta_R)
Fy = F*cos((pi/2)+theta_R)

T_AC = (-Fy)/cos(pi/3)
T_BC = (-Fx - (T_AC*cos(pi - (pi/6))))/( cos(pi) )

# reaction forces
Ax = (Fy * 0.6) / (0.6/sqrt(3))
Ay = -Fy
Bx = -T_BC

# joint A
T_AB = -((T_AC*cos((pi)+(pi/3)))+Ay)


print(Fy)
print(Fx)
print("T_AC: %f" % (T_AC))
print("T_BC: %f" % (T_BC))
print("T_AB: %f" % (T_AB))
print("Ax: %f" % (Ax))
print("Ay: %f" % (Ay))
print("Bx: %f" % (Bx))