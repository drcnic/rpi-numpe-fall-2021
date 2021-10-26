"""hw04.py"""
import fitdata as fd
import numpy as np
import matplotlib.pyplot as plt

files = ["MS00.dat", "MS10.dat", "MS20.dat", "MS30.dat"]

xlow  = 0.
xhigh = 0.
ylow  = 0.
yhigh = 0.

deg_fit     = [2,2,2,2]
fit_color   = ['r-', 'g-', 'b-', 'y-']
labels      = [r'$\sigma_m=0$',r'$\sigma_m=10$',r'$\sigma_m=20$',r'$\sigma_m=30$']

for i in range(0, len(files)):
    data = np.loadtxt(files[i], skiprows=2)
    life_data = data[:,0]       # x-values: number of cycles
    maxstress_data = data[:,1]  # y-values: yield strength at x cycles
    
    life_data_logn = np.log(life_data)
    life_data_log  = np.log10(life_data)
    
    
    # get max/min values of all datasets
    xlow_i  = np.min(life_data)
    xhigh_i = np.max(life_data)
    ylow_i  = np.min(maxstress_data)
    yhigh_i = np.max(maxstress_data)
    
    if (xlow > xlow_i):
        xlow = xlow_i
    if (xhigh < xhigh_i):
        xhigh = xhigh_i
    if (ylow > ylow_i):
        ylow = ylow_i
    if (yhigh < yhigh_i):
        yhigh = yhigh_i
    
    
    
    fit_coeff = fd.calc_fit(life_data_logn, maxstress_data, deg_fit[i])
    yfit = fd.eval_fit(fit_coeff, life_data_logn)
    
    
    plt.plot(life_data, maxstress_data, 'k.')   # plot actual data
    plt.plot(life_data, yfit, fit_color[i], label=labels[i]+":[P"+str(deg_fit[i])+"]")            # plot fit data
    

plt.legend(prop={'size': 8})
plt.xscale('log')
plt.axis([xlow, xhigh+10**7, ylow, yhigh+5])
plt.rcParams['font.family'] = "Consolas"
plt.title("Fatigue life of Aluminium 2024 alloy")
plt.xlabel("Fatigue Life [log(cycles)]")
plt.ylabel("Maximum Stress [ksi]")
plt.gca().grid()
plt.savefig("hw04_plot.png", dpi=300, edgecolor="none")
plt.show()

