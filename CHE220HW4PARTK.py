# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:05:03 2019

@author: Nicholas Carpentieri
"""

Line = "%4s%16s%16s%16s%16s%16s"%("k","xi","Ftot","F1tot","dltxi","xi1")
print(Line)

xi = 70

k_list = []
xi_list = []

for k in range(21):
    Ftot = -27.9 + (24+2*xi)**4/((96-xi)**2*(240+2*xi)**2)
    F1tot = -186624*(xi+12)**3/((xi-96)**3*(xi+120)**3)
    dltxi = -Ftot/F1tot
    xi1 = xi + dltxi
    
    k_list.append(k)
    xi_list.append(xi)
   
    Line = "%4d%16.4e%16.4e%16.4e%16.4e%16.4e"%(k,xi,Ftot,F1tot,dltxi,xi1) #4d outputs integers, giving 4 spaces  
    print(Line)
    
    xi = xi1
    