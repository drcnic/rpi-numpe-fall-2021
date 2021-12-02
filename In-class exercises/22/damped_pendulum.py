import odesys
import numpy as np
import matplotlib.pyplot as plt

g, L = 9.8, 0.1
c, m = 1.0, 1.0
#c, m = 101.0, 1.0

def func(u, t):
    F = np.array([u[1], -(g/L)*np.sin(u[0])-(c/m)*u[1]])
    return F

tspan = np.array([0,6*np.pi/np.sqrt(g/L)])
u0 = np.array([20*np.pi/180, 0.0]) # start at rest
num_steps = 24
t, u = odesys.runge_kutta_4th(func, tspan, u0, num_steps)
plt.plot(t,u[0,:],label="u[0]: Angular position")
plt.plot(t,u[1,:],label="u[1]: Angular velocity")
plt.plot([0,1.7],[0,0],'k-.',linewidth=0.5)
plt.xlim([0,1.7])
plt.ylim([-5,5])
plt.legend(loc=4)
plt.title("Damped pendulum [c=1.0,nstep=24]")
plt.xlabel('time')
