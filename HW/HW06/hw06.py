import numpy as np
import matplotlib.pyplot as plt
from diff import finite_difference
from poly_deriv import polynomial_derivative
from fitdata import eval_fit, calc_fit

data    = np.loadtxt("S1.txt", skiprows=2)
xdata   = data[:,0]     # curvature, m^-1
ydata   = data[:,1]     # moment, Nm
bound = 15 # yield point is 14th data point

# coefficients
fit_coeff_elastic = calc_fit(xdata[:bound], ydata[:bound], 1) # elastic region
fit_coeff_plastic = calc_fit(xdata[bound:], ydata[bound:], 3) # plastic region

### Bending moment
fit_data_moment  = np.zeros(xdata.size)
fit_data_moment[:bound] = eval_fit(fit_coeff_elastic, xdata[:bound]) # fit moments in elastic region
fit_data_moment[bound:] = eval_fit(fit_coeff_plastic, xdata[bound:]) # fit moments in plastic region


### Bending stiffness
stiffness_fit = np.zeros(xdata.size)
stiffness     = np.zeros(xdata.size)

stiffness_fit[:bound] = polynomial_derivative(fit_coeff_elastic, xdata[:bound])
stiffness_fit[bound:] = polynomial_derivative(fit_coeff_plastic, xdata[bound:])

stiffness[:bound] = finite_difference(xdata[:bound], ydata[:bound])
stiffness[bound:] = finite_difference(xdata[bound:], ydata[bound:])



# Moment vs. curvature graph
plt.figure(figsize=[6,8])

plt.subplot(2, 1, 1)
plt.grid()
plt.title("Moment-curvature and Bend Stiffness of T Section (niclad)")
plt.xlabel("Curvature (k)")
plt.ylabel("Moment [Nm]")
plt.plot(xdata, ydata, 'k.', label="data")
plt.plot(xdata[:bound], fit_data_moment[:bound], 'g-', label="elastic")
plt.plot(xdata[bound-1:], fit_data_moment[bound-1:], 'r-', label="plastic")
plt.legend()

# stiffness vs curvature
stiff_coeff = np.zeros(fit_coeff_plastic.size-1)
stiff_coeff = [fit_coeff_plastic[1], fit_coeff_plastic[2]*2, fit_coeff_plastic[3]*3]



plt.subplot(2, 1, 2)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.grid()
plt.xlabel("Curvature (k)")
plt.ylabel("Bending Stiffness [$Nm^2$]")
plt.plot(xdata, stiffness, 'b.', label="finite difference")
plt.plot(xdata[:bound], stiffness_fit[:bound], 'g-', label="elastic")
plt.plot(xdata[bound:], stiffness_fit[bound:], 'r-', label="plastic")
plt.ylim(bottom=-.5e5)
plt.text(0, -.25e5,  r"$BendStiff=" + "{:.1e}".format(stiff_coeff[0]) + "" + "{:.1e}".format(stiff_coeff[1]) + "x +" + "{:.2e}".format(stiff_coeff[0]) + "x^2$")
plt.legend()


plt.savefig("hw06_plot.png")
plt.show()