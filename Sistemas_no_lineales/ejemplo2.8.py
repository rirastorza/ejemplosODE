#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 03 10:13:41 2016

Ejemplo 2.8, producto de matrices, calculo del rango, etc.

@author: Ramiro Irastorza
"""


import numpy as np


#Cálculo del determinante de una matriz
A = np.array([[-2., 17., 4.], [-1.0, 6.0, 1.0], [0.0, 1.0, 2.0]])

lam1 = np.linalg.eig(A)

print('autovalores:', lam1)

print('Rango:',np.linalg.matrix_rank(A))
print('Rango:',np.linalg.matrix_rank(A-2*np.eye(3,3)))

print('(A-lambdaI)^2:',np.linalg.matrix_power(A-2*np.eye(3,3),2))
print('(A-lambdaI)^3:',np.linalg.matrix_power(A-2*np.eye(3,3),3))
