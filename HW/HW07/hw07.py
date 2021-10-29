"""hw07.py"""

import matplotlib.pyplot as plt
import numpy as np
import forces_surface as fs

# data organization
data   = np.loadtxt("hydro_pressure.dat")
theta  = data[:,0]
x_data = data[:,1]
y_data = data[:,2]
press_data = data[:,3]




# calculation
x_mid, y_mid = fs.panel_midpoints(x_data, y_data)
dfx, dfy = fs.panel_midforces(x_data, y_data, press_data)
fx, fy = fs.integrate_forces(dfx, dfy)

dfx_t = dfx/1.e6
dfy_t = dfy/1.e6


# plotting
fig, ax = plt.subplots(1,1,figsize=(8,6))
ax.axis('equal')

plt.title("Hydrostatic Pressure in Ship Hull (niclad)", size=16)
plt.xlabel("x", size=16)
plt.ylabel("y", size=16)

q = ax.quiver(x_mid, y_mid, dfx_t, dfy_t, color='r', units='xy', scale=1/24.)
ax.quiverkey(q, X=0.7, Y=0.1, U=1/2., label="Force", labelpos = 'E')
plt.plot(x_data, y_data, 'k-', linewidth=5)
plt.plot(np.array([x_data[0], x_data[x_data.size-1]]), np.array([y_data[0], y_data[x_data.size-1]]), 'k-', linewidth=5) # connect ends of half circle
plt.plot([-30, 30], [-10, -10], 'b-', linewidth=5)      # waterline

# net force vector graphing
mega = 1.e-6
text_string = "Net force vector:\n("
text_string += '{:6.4e}'.format(fx*mega)
text_string += ", "
text_string += '{:6.4e}'.format(fy*mega)
text_string += ")"
plt.text(-30,10, text_string)

plt.savefig("hydrostatic_force.png")
plt.show()
