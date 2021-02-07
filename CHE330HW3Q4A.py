# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:17:32 2020
#this file computes the natural log of the parital molar gibbs excess energy at different mol fractions for two species and then comparatively plots both series on the same set of axis
@author: Nicholas Carpentieri
"""
import matplotlib.pyplot as pp
import numpy as np
A = 0.2603
B = 0.004396
a1 = A + 3*B
a2 = A - 3*B
b1 = -4*B
b2 = 4*B
xlist = [] 
lngamma1list = []
lngamma2list = []
lngamma1 = 0
lngamma2 = 0

for x1 in np.arange (0,1,.1):
    x2 = 1-x1
    lngamma1 = (a1*(x2**2)+(b1*(x2**3)))
    lngamma2 = (a2*(x1**2)+(b2*(x1**3)))
    xlist.append(x1)
    lngamma1list.append(lngamma1)
    lngamma2list.append(lngamma2)
pp.plot(xlist,lngamma1list, label = "gamma 1")
pp.plot(xlist,lngamma2list, label ="gamma 2")
pp.legend()
pp.xlabel("x1")
pp.ylabel("lngamma")
