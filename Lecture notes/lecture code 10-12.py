# zip
# enumerate
# [] list comprehensions




import numpy as np
arr = np.linspace(1.,10.,10)

print(arr)


### two ways to make a for loop

# don't care about the index
for a in arr:
    print(a)
    
# need the index
for i in range(arr.size):
    print(arr[i])
    
### enumerate
# like a for loop, but you get the index and a variable
for i,a in enumerate(arr):
    print(a)

### zip 
arr = np.linspace(1.,10.,10)
brr = 2.*arr

print(arr)
print(brr)

for a,b in zip(arr,brr):
    print(a,b)
    
    
### list comprehension
from math import sin
y = [ sin(a) for a in arr ]