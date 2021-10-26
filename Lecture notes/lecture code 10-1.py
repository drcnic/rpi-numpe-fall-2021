# while, break, continue
import numpy as np

a = np.linspace(0,10,11)
print(a)

i = 0
while (i < 11):
    print(a[i])
    i += 1
    
    
    
for i in range(0,10):
    
    if(i==3):
        continue
    
    print(i)
    if(i==5):
        break