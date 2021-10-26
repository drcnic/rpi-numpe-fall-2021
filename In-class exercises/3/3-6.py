import numpy as np

arr = np.load("data.npy")

b0 = b1 = b2 = b3 = b4 = 0

for x in arr:
    if (x < 185.0):
        b0+= 1
    elif (x >= 185.0 and x < 195.0):
        b1+= 1
    elif (x >= 195.0 and x < 205.0):
        b2+= 1
    elif (x >= 205.0 and x < 215.0):
        b3+= 1
    else:
        b4+= 1
        
print(b0)
print(b1)
print(b2)
print(b3)
print(b4)