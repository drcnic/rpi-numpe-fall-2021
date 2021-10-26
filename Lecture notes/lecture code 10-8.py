# Lecture 10: Newton's method for root finding

### CLASS NOTES: MATH
#   
#   Newton's method for root finding
#       f(x), f and x -> real numbers (for now -- later they will be vectors)
#       Given f(x) find x such that f(x_r) = 0
#       


### CLASS NOTES: CODE
import numpy as np


# code block 1 (normal code: may fail)
try:    # try this block...
    dx = -f/df

except: # ... and if it fails, do this block.
    # code block 2 (work around code)
    x = x + delta
    f, df = funcdf(x)
    dx = -f/df
    
    
    
x = 1
y = 0

try:
    z = x/y     # but y *could* go to zero
except:
    z = 1.0
    
print(z)


except ZeroDivisionError:
except 