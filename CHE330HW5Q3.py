# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:33:05 2020

@author: Nicholas Carpentieri
"""
#This file takes data given for a chemical engineering flash situation and computes the values necesarry to generate a pressure Vs liquid fraction versus gas fraction plot. This plot is essential in the Mccabe-Thiele analysis, a method to determine the number of equilbrium stages during a binary flash distillation. 

import scipy.optimize as sp
import numpy as np 
import matplotlib.pyplot as pp
"""
P=2
T=262.9714580874944
x1=.45
x2=1-x1
p1vap=10**((-1051.38/T)+4.517190)
p2vap=10**((-1183.44/T)+4.47)
dp1vap=(2420.89*(10**(-1051.38/T)+4.517190))/T**2
dp2vap=(2724.97*(10**(-1183.44/T)+4.47))/T**2
f=(x1*p1vap)+(x2*p2vap)-P
df=(x1*dp1vap)+(x2*dp2vap)
Tnext=T-(f/df)
print(Tnext)
"""
T=262.9714580874944 
q=1.5
xd=.99
fd= 2.4
xb=.06
ylist=[]
Plist=[]
striplist=[]
rectlist=[]
p1vap=10**((-1051.38/T)+4.517190)
p2vap=10**((-1183.44/T)+4.47)
x1 = .45
xlist=np.arange(0,1.1,.1)
for i,x1 in enumerate(xlist):
    P = p1vap*x1 + p2vap*(1-x1)
    y1 = (p1vap*xlist[i])/P
    stripline=(xlist[i]*(q/(1+q)))+(xd/1+q)
    rectline=(xlist[i]*((q+fd)/q+1))-((fd-1)/(q+1))
    striplist.append(stripline)
    rectlist.append(rectline)
    Plist.append(P)
    ylist.append(y1)

print(striplist)
print(rectlist)
print(Plist)
print(xlist)
print(ylist)

def xyplt():
    fig, ax1 = pp.subplots()
    ax1.set_xlabel('x1')
    ax1.set_ylabel('P')
    ax1.plot(xlist,Plist, '--', color = "red")
    ax1.tick_params(axis = 'y')
    ax2 = ax1.twinx()
    ax2.set_ylabel("y1")
    ax2.plot(xlist,ylist, color = "blue")
    ax2.tick_params(axis = 'y')
    fig.tight_layout()

    pp.show()
pp.show(xyplt())

res = [(i * j)/k for i, j, k in zip(list1, list2,list3)]
