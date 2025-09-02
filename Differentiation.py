# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 15:51:22 2025

@author: Student
"""

import numpy as np
def f(x):
    return np.cos(x)
tol=float(input("Enter the tolerance very close to 0 like 0.0000000001,0.000000000000001,0.00000000001 etc.:"))
y=float(input("Enter the point at which you find the derivative. for 3pi enter 3 , for pi/2 enter 0.5 etc. :"))
x=np.pi*y
h=0.01
p=(f(x+h)-f(x))/h
k=h/10
q=(f(x+k)-f(x))/k
while abs(p-q)>tol:
    h=h/10
    k=k/10
    p=(f(x+h)-f(x))/h
    q=(f(x+k)-f(x))/k
print("The result will be",q)