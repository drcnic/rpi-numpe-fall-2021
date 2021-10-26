# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:14:49 2021

@author: Daric
"""
import numpy as np
from hw03 import shuffle_Ab, max_magnitude, applied_load, truss_geometry
from linsolve import solve
## This stuff works
#order = np.array([1,0,2])
#b = np.array([7,8,9])
#A = np.array([[1, 2],[3, 4],[5, 6]])

#print(shuffle_Ab(A,b,order))
#print(max_magnitude(b))


#applied_load(40, 0, 60, 100)
#G = truss_geometry(60, 60)

#print(G)




# A = np.array([[  1,      0,  0,  0,  0,  0],
#               [  0,    0.5,  0,  0,  0,  0],
#               [  0, -0.866,  1,  0,  0,  0],
#               [  0,  0.866,  0,  1,  0,  0],
#               [  1,   -0.5,  0,  0,  1,  0],
#               [  0,      0,  1,  0,  0,  1]])

b = np.array([0, 190.178,407.839,0,0,0])
# print(solve(A, b))

print(max_magnitude(b))