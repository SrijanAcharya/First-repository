# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 15:38:03 2025

@author: Student
"""

tol=float(input("Enter tolerance like 0.01,0.001,0.0001 etc."))
def func(x):
    return (x**2+2*x-35)
a=float(input("Enter one end point of interval in which solution can be contained: "))
b=float(input("Enter another end point of interval in which solution can be contained: "))
while func(a)*func(b)>=0:
    a=float(input("Enter new end point of the interval: "))
    b=float(input("Enter new other end point of the interval: "))
c=(a+b/2)
while abs(func(c))>tol:
    if (func(a)*func(c))<0:
        b=c
    if (func(b)*func(c))<0:
        a=c
    c=(a+b)/2
print("The required solution adjusted to the tolernce is ",c)