#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Ramiro Irastorza
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def malthus(x,t):
    # constants
    k = .5 #tasa de crecimiento
    #ecuación diferencial       
    dxdt = k * x
    return dxdt

t = np.linspace(0,10) # tiempo en que tendré la solución
x0 = [1]            # condición inicial
x1 = odeint(malthus,x0,t) # integrate

x0 = [2]            # condición inicial
x2 = odeint(malthus,x0,t) # integrate

x0 = [3]            # condición inicial
x3 = odeint(malthus,x0,t) # integrate

# plot results
plt.figure(1)
plt.plot(t,x1,'b-')
plt.plot(t,x2,'r--')
plt.plot(t,x3,'g-.')
plt.xlabel('Tiempo (hrs)')
plt.ylabel('Cantidad de bacterias')
plt.legend(['x0=1','x0=2','x0=3'])
plt.show() 

#Ahora con sympy, solución analítica

from sympy import Function, dsolve, Derivative, checkodesol
from sympy.abc import t,k
x = Function('x')
result = dsolve(Derivative(x(t), t, 1) - k*x(t), x(t))
print(result)
print(checkodesol(Derivative(x(t), t, 1) - k*x(t), result))
