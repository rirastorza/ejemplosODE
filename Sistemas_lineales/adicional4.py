#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 03 10:13:41 2016

Ecuacion diferencial:

x'''+3x''+3x'+x = 30e**(-t)

@author: Ramiro Irastorza
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def funcion(y, t):
    x1, x2, x3 = y
    dydt = [1.0*x2, 1.0*x3 , 30.0*np.exp(-t)-3.0*x3-3.0*x2-x1]
    return dydt

#Constantes
x10 = 3.0 #valor inicial
x20 = -3.0 #valor inicial
x30 = -47.0

y0 = [x10, x20, x30]

t = np.linspace(0,30,num=100) # tiempo en que tendré la solución
solnum = odeint(funcion,y0,t) # integrate

ynum = solnum[:,0] 

#Solución teórica
y = (3.0-25.0*t**2.0)*np.exp(-t)+5.0*t**3.0*np.exp(-t)

# plot resultados
plt.figure(1)
plt.plot(t,ynum,'b.')
plt.plot(t,y,'r-')
#plt.plot(t,x3,'g-.')
plt.xlabel('Tiempo (s)')
plt.ylabel('x (m)')
plt.legend(['Numerico','Teorico'])
plt.show() 
