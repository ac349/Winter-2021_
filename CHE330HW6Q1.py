# -*- coding: utf-8 -*-

#This script intakes lists of liquid mole fractions, gas mole fractions, and pressures, and computes thermodynamic quantites such as partial molar gibbs energies. Additonally, it graphs the data and fits it to a redlich-kister expansion

import math
import scipy.optimize as sp
import numpy as np 
import matplotlib.pyplot as pp
R=8.314
T=323.15
p1vap=54.08
p2vap=29.6
plist=[29.6,44.39,52.56,57.19,59.95,61.26,62.56,63.64,63.52,63.46,61.96,59.51,54.08]
x1list=[0.000000001,0.086,0.168,0.259,0.345,0.416,0.568,0.696,0.706,0.779,0.881,0.945,.9999999]
y1list=[0.00000000001,0.367,0.499,0.567,0.605,0.625,0.654,0.698,0.717,0.728,0.789,0.862,.9999998]
x2list=[]
y2list=[]
x2list=[1-i for i in x1list]
y2list=[1-i for i in y1list]
gamma1=[(i * j)/(k*p1vap) for i, j, k in zip(plist, y1list,x1list)]
gamma2=[(i * j)/(k*p2vap) for i, j, k in zip(plist, y2list,x2list)]  
Giex1=[(R*T*np.log(i)) for i, in zip(gamma1)]
Giex2=[(R*T*np.log(i)) for i, in zip(gamma2)]

Gex=[(i*j+(k*l)) for i,j,k,l in zip(x1list,Giex1,x2list,Giex2)]
print("Giex1=",Giex1,"note, I had to input x1 and y1 as a number very close to zero rather than zero to compute giex (cannot take ln of 0), so the first values of the giexlists are invalid")

print("Giex2=",Giex2)
print("Gex=",Gex)


def func(x1list,A,B):
    return(x1list*(1-x1list)*(A+B*(x1list-(1-x1list))))
Aguess = 1
Bguess = 1
x = np.linspace(0,1,100)
a, cov = sp.curve_fit(func,x1list, Gex,p0=(Aguess,Bguess))
print('A,B=',a)
# save output from curve_fit in more reasonably named variables
A_fit = a[0]
B_fit = a[1]

# Create a very fine spacing of points
x_fine = np.linspace(0,1,100)
# Calculate value of function (with fit parameters) for x_fine
y_fine_fit = func(x_fine,A_fit,B_fit)

# now plot
pp.figure()
# plot the raw data
pp.plot(x1list,Gex,linestyle='',marker='x',label='data')
# plot the fit
pp.plot(x_fine, y_fine_fit,label='fit')
pp.legend()
pp.show()

pp.figure()
pp.plot(x1list,plist,marker='.')
pp.plot(y1list,plist,marker='.')
pp.xlabel("x1,y1")
pp.ylabel("P")
pp.show()


def func2(x1list,B,A):
    for x1 in x1list:
        x2=1-x1
        return x1*x2*(A+B*(x1-x2))
from scipy.optimize import curve_fit
m_guess = 1
b_guess = 1
x = x1list

alph=[((1+(i/j)*(np.log(k)/np.log(l)))**2)*np.log(l) for i,j,k,l in zip(x2list,x1list,gamma2,gamma1)]
beta=[((1+(i/j)*(np.log(k)/np.log(l)))**2)*np.log(l) for i,j,k,l in zip(x1list,x2list,gamma1,gamma2)]
Gexc=[(R*T*(i*j*k*l)/((i*j)+(k*l))) for i,j,k,l in zip(alph,x1list,beta,x2list)]


def func3(x1list,alpha,BETA):
    return (R*T*(alpha*x1list*BETA*(1-x1list))/((alpha*x1list)+(BETA*(1-x1list))))
from scipy.optimize import curve_fit
alpha_guess = 1
BETA_guess = 1
x = np.linspace(0,1,num=100)
a, cov = curve_fit(func3,x1list, Gexc,p0=(alpha_guess,BETA_guess))

alpha_fit = a[0]
BETA_fit = a[1]

# Create a very fine spacing of points
x_fine = np.linspace(0,1,100)
# Calculate value of function (with fit parameters) for x_fine
y_fine_fit = func(x_fine,A_fit,B_fit)

# now plot
pp.figure()
# plot the raw data
pp.plot(x1list,Gexc,linestyle='',marker='x',label='data')
# plot the fit
pp.plot(x_fine, y_fine_fit,label='fit')
pp.legend()
pp.show()

pp.figure()
pp.plot(x1list,plist,marker='.')
pp.plot(y1list,plist)
pp.xlabel("x1,y1")
pp.ylabel("P")
pp.show()
def func(x,m,b):
    return m*x+b
from scipy.optimize import curve_fit
m_guess = 1
b_guess = 1
x = x1list
a, cov = curve_fit(func,x1list, Gex,p0=(m_guess,b_guess))
x1*x2*(A+B*(x1-x2))
