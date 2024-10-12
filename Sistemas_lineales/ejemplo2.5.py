#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 03 10:13:41 2016

Ecuacion diferencial:

t**2x''-4tx'+6x = t**3

@author: Ramiro Irastorza
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def funcion(y, t):
    x1, x2 = y
    dydt = [1.0*x2 , t+(4.0/t)*x2-(6.0/t**2.0)*x1]
    return dydt

#Constantes
x10 = 0.0 #valor inicial
x20 = 3.0 #valor inicial

y0 = [x10, x20]

t = np.linspace(1,10,num=100) # tiempo en que tendré la solución
solnum = odeint(funcion,y0,t) # integrate

ynum = solnum[:,0] 

#Solución teórica
y = -3.0*t**2.0+3.0*t**3.0+t**2.0*(1.0-t)+t**3.0*np.log(t)

# plot resultados
plt.figure(1)
plt.plot(t,ynum,'b.')
plt.plot(t,y,'r-')
#plt.plot(t,x3,'g-.')
plt.xlabel('Tiempo (s)')
plt.ylabel('x (m)')
plt.legend(['Numerico','Teorico'])
plt.show() 
