# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 16:40:05 2025

@author: Student
"""

def f(x):
    return x**2+2*x-24
tol=float(input("Enter the tolerance very close to 0 like 0.0000000001,0.000000000000001,0.00000000001 etc.:"))
x=float(input("Enter the point at which you find the derivative: "))
h=0.01
p=(f(x)-f(x-h))/h
k=h/10
q=(f(x)-f(x-k))/k
for i in range(1,51):
    h=h/10
    k=k/10
    p=(f(x)-f(x-h))/h
    q=(f(x)-f(x-k))/k
    if abs(p-q)<=tol:
        break
print("The result will be",q)