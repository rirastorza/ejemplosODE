#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
En matlab:
>> x0=.05;v0=.5;k=200;m=5;
>> t=[0:.01:10];
Resultado teorico:
>> y = x0*cos(sqrt(k/m)*t)+sqrt(k/m)*v0*sin(sqrt(k/m)*t)+m*9.8/k;

@author: Ramiro Irastorza
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def resorte(y, t, m, k):
    a, x = y
    dydt = [-k*x/m , a]
    return dydt

#Constantes
x0 = .05 #posicion inicial
v0 = .5 #velocidad inicial
k = 200.0 #constante del resorte
m = 5.0 #masa del bloque

y0 = [v0, x0]

t = np.linspace(0,5,num=100) # tiempo en que tendré la solución
solnum = odeint(resorte,y0,t, args=(m, k)) # integrate

ynum = solnum[:,1] + m*9.8/k #Corro la solución 

#Solución teórica
y = x0*np.cos(((k/m)**.5)*t) +((m/k)**.5)*v0*np.sin(((k/m)**.5)*t)+m*9.8/k

# plot resultados
plt.figure(1)
plt.plot(t,ynum,'b.')
plt.plot(t,y,'r-')
#plt.plot(t,x3,'g-.')
plt.xlabel('Tiempo (s)')
plt.ylabel('y (m)')
plt.legend(['Numerico','Teorico'])
plt.show() 
