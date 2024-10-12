#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 03 10:13:41 2016

Ejemplo 2.7, diagrama de fase y dibujo de estados nodo estable

@author: Ramiro Irastorza
"""
import matplotlib.pyplot as plt
import numpy as np
import pylab as p
import scipy.integrate as integrate

def df1(x1, x2):
    return a11*x1 + a12*x2

def df2(x1, x2):
    return a21*x1 + a22*x2

def derivs(state, t):
    x1, x2 = state  
    deltaf1 = df1(x1, x2)  
    deltaf2 = df2(x1, x2) 
    return deltaf1, deltaf2


#Sistema del ejemplo2.7
a11, a12 = -3.0, 1.0
a21, a22 = 1.0, -3.0

x10 = 2.0
x20 = -1.5

t = np.arange(0.0, 0.6, 0.01)

y0 = [x10, x20]
y = integrate.odeint(derivs, y0, t)
x1 = y[:,0]  
x2 = y[:,1] 

p.figure()
p.plot(t, x1, label='x1')
p.plot(t, x2, label='x2')
p.xlabel('Tiempo')
p.ylabel('Estados')
#p.title('Estados')
p.grid()
p.legend()
p.savefig('ejemplo2.7_estados.png', dpi=150)

p.figure()
p.plot(x1, x2)
p.xlabel('x1')
p.ylabel('x2')
p.title('Plano de fase')
X1, X2 = np.meshgrid(np.arange(-3.0, 3.0, .5), np.arange(-3.0, 3.0, .5))
dX1 = df1(X1, X2)
dX2 = df2(X1, X2)
p.quiver(X1, X2, dX1, dX2)
X1, X2 = np.meshgrid(np.arange(-3.0, 3.0, .01), np.arange(-3.0, 3.0, .01))
dX1 = df1(X1, X2)
dX2 = df2(X1, X2)
p.ylabel('x2')
p.title('Trayectoria y direcciones')
w,v = np.linalg.eig([[a11,a12],[a21,a22]])
print('Autovalores:',w)
print('Autovectores:',v)

p.savefig('ejemplo2.7_planodefase.png', dpi=150)

p.show()
