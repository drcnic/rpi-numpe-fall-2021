import numpy as np
import shell_transmission as st
import matplotlib.pyplot as plt


# Paramaters
N   = 100
Ri  = 2
Sig_s = 1.0
Sig_a = 1.0

data1 = st.shell_transmission(Sig_s, Sig_a, Ri, Ri + 1, N)
data2 = st.shell_transmission(Sig_s, Sig_a, Ri, Ri + 2, N)

print(data1)
print(data2)


############
# Plotting #
############
plt.title("Number of transmissions vs. number of simulated neutrons (niclad)")
plt.xlabel("Total Number of Neutrons Simulated")
plt.ylabel("Number of Transmissions")

plt.plot(np.linspace(0,N,N), data1, 'b-', label="Ro = 3 cm")
plt.plot(np.linspace(0,N,N), data2, 'r-', label="Ro = 4 cm")
plt.legend()

plt.savefig("hw08_plot")
plt.show()



print("Out of " + str(N) + " neutrons, " + str(int(data1.max())) + " made it through with outer radius of " + str(Ri + 1) + " cm.")
print("Out of " + str(N) + " neutrons, " + str(int(data2.max())) + " made it through with outer radius of " + str(Ri + 2) + " cm.")



