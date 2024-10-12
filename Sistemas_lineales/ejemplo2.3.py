#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ecuacion diferencial:

x''+4x = 2t

@author: Ramiro Irastorza
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def funcion(y, t):
    x1, x2 = y
    dydt = [1.0*x2 , 12.0*t-4.0*x1]
    return dydt

#Constantes
x10 = 1.0 #valor inicial
x20 = 5.0 #valor inicial

y0 = [x10, x20]

t = np.linspace(0,30,num=100) # tiempo en que tendré la solución
solnum = odeint(funcion,y0,t) # integrate

ynum = solnum[:,0] 

#Solución teórica
y = np.cos(2.0*t) +np.sin(2.0*t)+3.0*t

# plot resultados
plt.figure(1)
plt.plot(t,ynum,'b.')
plt.plot(t,y,'r-')
#plt.plot(t,x3,'g-.')
plt.xlabel('Tiempo (s)')
plt.ylabel('x (m)')
plt.legend(['Numerico','Teorico'])
plt.show() 
