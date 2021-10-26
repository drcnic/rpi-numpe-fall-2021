import numpy
import numpy as np   # can give imported packages an alias

a1 = numpy.array([1,2,3,10])
print(a1)

print(a1.size)  # number of elements in arr
print(a1.ndim)  # array dimensions

a2 = numpy.zeros(20)
print(a2)
a2[0] = 100
print(a2)

a3 = 100*numpy.ones(15)
print("a3=",a3)

a4  = numpy.linspace(0,10,11)   # starts at 0, ends at 10, with 10 elements
a4_ = numpy.linspace(1,10,20)   # starts at 1, ends at 10, with 20 elements
print(a4)
print(a4_)

print(a4[0:5])
print(a4[1:10])
print(a4[0:-1:2])


a5 = a4     # does not create new memory
            # this is an ALIAS
a5 = a4.copy()  # this creates new location in memory for a5

mat = numpy.array([ [1,2,3],    # multidimensional arrays
                    [4,5,6],
                    [7,8,9] ])

sm = 0.0
for a in a4:
    print(a)
    sm = sm + a

sm = 0.0
for i in range(4, a4.size): # start at index 4, go to the end
    print(i)
    print(a4[i])
    sm += a4[i]