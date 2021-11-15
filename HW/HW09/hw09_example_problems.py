print()
print("--- EXAMPLE 1 - Nan with if-else ---------")
import numpy as np
from math import sqrt, nan   # note Python uses all lower case `nan`
# big long computation
result = np.zeros(8)
for i in range(4, -4, -1):
    idx = 4-i
    if (i >= 0):
        result[idx] = sqrt(float(i))
    else:
        result[idx] = nan
# show the results later
for j in range(result.shape[0]):
    print("j and sqrt(j) =", j, result[j])

print()
print("--- EXAMPLE 2 - NaN with try-except ------")
import numpy as np
from math import sqrt, nan   # note Python uses all lower case `nan`
# big long computation
result = np.zeros(8)
for i in range(4, -4, -1):
    idx = 4-i
    try:           # square root of a negative will raise an exception
        result[idx] = sqrt(float(i))
    except:        # signal NaN if exception was raised
        result[idx] = nan
# show the results later
for j in range(result.shape[0]):
    print("j and sqrt(j) =", j, result[j])

print()
print("--- EXAMPLE 3 - NaNs propagate through calculations ---")
from math import sqrt, nan
y = nan
print("nan is an object of class float: ", type(y))
print()
x = 3.4
print(x+y, x-y, x*y, x/y)
print(y, y**2, sqrt(y), float(y))
print("hey, hey, good bye.")

print()
print("--- EXAMPLE 4 - time.perf_counter ---")
from math import pi
import time
start_time = time.perf_counter()
# measure time to complete this calculation
terms = 1000000      # increase this number to show more time
LM_pi = 1.0
for i in range(3, 2*terms, 4):
    LM_pi -= 1.0/float(i)
    LM_pi += 1.0/float(i+2)
LM_pi *= 4.0
end_time   = time.perf_counter()
elapsed_time = end_time - start_time
string  = "Leibniz estimates pi as\n"
string += str(LM_pi)
string += " with " + str(terms) + " terms\n"
string += "for a " + str((1.0-LM_pi/pi)*100.0) + "% error\n"
string += "in only " + '{:.3f}'.format(elapsed_time) + " seconds."
print(string)

print()
print(LM_pi, "in", terms, "terms")
print("in only " + '{:.3f}'.format(elapsed_time) + " seconds.")