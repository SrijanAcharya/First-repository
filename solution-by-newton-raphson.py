# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 16:13:46 2025

@author: Student
"""

def fn(x):
    return x**2+2*x-35
def fn1(x):
    return 2*x+2
tol=float(input("Enter tolerance like 0.01,0.001,0.0001 etc. "))
a=float(input("Enter any number that can be solution: "))
while abs(fn(a))>tol:
    a=a-(fn(a)/fn1(a))
print("Solution is ",a)