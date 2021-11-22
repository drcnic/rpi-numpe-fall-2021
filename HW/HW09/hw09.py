"""hw09.py -- analysis and graphing of Euler numerical methods"""

import numpy as np
import conical_tank as ct
import euler as eu
import time
import matplotlib.pyplot as plt


tspan = np.array([0, 1000]) # model conical tank draining from 0 to 1000 seconds

# =============================================================================
# Plot Solutions for Both Numerical Methods
# =============================================================================

# Calculate and plot approximate solutions to conical drain tank problem
steps = 40

x, y = eu.forward_euler(ct.conical_tank_model, tspan, ct.H, steps)
plt.plot(x, y, 'g-', label="forward Euler solution")
x, y = eu.backward_euler(ct.conical_tank_model, tspan, ct.H, steps)
plt.plot(x, y, 'y-', label="backward Euler solution")

# Plot a line denoting when tank is drained (h(t) = 0) according to analytical solution
drain_time = ct.conical_tank_drain_time()
plt.plot(np.array([drain_time,drain_time]), np.array([0, ct.H]), 'r-')

# Plot settings
plt.rcParams['font.family'] = "Consolas"

plt.grid(linestyle=':', linewidth=1)
plt.xlabel("time, t [seconds]")
plt.ylabel("water height, h(t) [meters]")

str_title  = "Water drains in "
str_title += "{:.1f}".format(drain_time)
str_title += " seconds (per analytical solution)"
plt.title(str_title)

legend_title = "For " + "{:d}".format(steps) + " steps"
plt.legend(title=legend_title)

plt.savefig("hw09_drain")
plt.show()


# =============================================================================
# Plot Accuracy for Both Numerical Methods
# =============================================================================

# Calculate absolute error for both numerical approximation methods
test_N = np.array([10, 30, 100, 300, 1000, 3000, 10000])
test_time = 600 # time in seconds at which we want to get the abs error
exact  = ct.conical_tank_analytical(test_time)

fe_abs_err = np.zeros(test_N.size)
be_abs_err = np.zeros(test_N.size)

for i in range(0, test_N.size):
    i_600 = -1
    
    # both have same tspan -> same returned t
    t, fe_h = eu.forward_euler(ct.conical_tank_model, tspan, ct.H, test_N[i])
    t, be_h = eu.backward_euler(ct.conical_tank_model, tspan, ct.H, test_N[i])
    
    # get the first index where time is greater than or equal to 600 seconds
    for j in range(0 , test_N[i]):
        if (t[j] >= test_time):
            i_600 = j
            break
    
    # calculate absolute error for both methods
    fe_abs_err[i] = abs(exact - fe_h[i_600])
    be_abs_err[i] = abs(exact - be_h[i_600])


# Get calculation times for 10000 steps
#   FE
fe_time = time.perf_counter()
t, fe_h = eu.forward_euler(ct.conical_tank_model, tspan, ct.H, test_N[-1])
i_600 = 0
for j in range(0 , test_N[-1]):
    if (t[j] >= test_time):
        i_600 = j
        break
abs(exact - fe_h[i_600])
fe_time = time.perf_counter() - fe_time

#   BE
be_time = time.perf_counter()
t, be_h = eu.forward_euler(ct.conical_tank_model, tspan, ct.H, test_N[-1])
i_600 = 0
for j in range(0 , test_N[-1]):
    if (t[j] >= test_time):
        i_600 = j
        break
abs(exact - be_h[i_600])
be_time = time.perf_counter() - be_time


# Construct plot of accuracy 
plt.xscale('log')
plt.yscale('log')
plt.grid(linestyle=':', linewidth=1)

leg_str = '{:.3f}'.format(fe_time) + " seconds"
plt.plot(test_N, fe_abs_err,'g-', label="forward Euler, in "  + leg_str)
leg_str = '{:.3f}'.format(be_time) + " seconds"
plt.plot(test_N, be_abs_err,'y-', label="backward Euler, in " + leg_str)

plt.title("Accuracy of numerical solution at 600 s")
plt.xlabel("number of steps")
plt.ylabel("absolute error")

legend_title = "For " + "{:d}".format(test_N[-1]) + " steps"
plt.legend(title=legend_title)

plt.savefig("hw09_accuracy")
plt.show()

