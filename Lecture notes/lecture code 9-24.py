"""plotting cos(x)"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

x = np.linspace(0,5*pi,1000)    # create linearly spaced array
y = np.cos(x)

plt.plot(x,y, 'r--')
plt.xlim([0., 7.*pi])
plt.ylim([-2, 1.5])
plt.title()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()


dat = np.loadtxt("filename.txt")