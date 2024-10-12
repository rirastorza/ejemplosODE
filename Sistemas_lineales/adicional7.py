#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Sat Sep 03 10:13:41 2016

Matrices y sistemas lineales
(varios ejemplos)

@author: Ramiro Irastorza
"""

import numpy as np


#Cálculo del determinante de una matriz
A = np.array([[3.0, 1.0, -2.0], [4.0, 2.0, 1.0], [-2.0, 3.0, 5.0]])
print('La matriz A=',A)
detA = np.linalg.det(A)
print('El determinante es:',detA)
print('-------------------------')


#Cálculo del determinante de una matriz
A = np.array([[1.0, 3.0, 1.0, -1.0], [2.0, 1.0, 0.0, 1.0], [0.0, -2.0, 2.0, 1.0], [5.0, 4.0, 1.0, 0.0]])
print('La matriz A=',A)
detA = np.linalg.det(A)
print('El determinante es:',detA)
print('-------------------------')

#Inversa de una matriz
B = np.array([[1.0, 3.0], [2.0, 1.0]])
invB = np.linalg.inv(B)
print('La matriz B=',B)
print('La inversa de B es=',invB)
print('-------------------------')

#Autovalores y autovectores
C = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
#Autovalores
w,v = np.linalg.eig(C)
print('La matriz C=',C)
print('Autovalores:', w)
print('Autovectores:', v)

#Autovalores y autovectores
D = np.array([[1.0, 2.0], [2.0, 1.0]])
#Autovalores
w,v = np.linalg.eig(D)
print('La matriz C=',D)
print('Autovales:', w)
print('Autovectores:', v)
print('-------------------------')
