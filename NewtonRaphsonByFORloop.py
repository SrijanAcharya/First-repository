# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 16:22:24 2025

@author: Student
"""

def fn(x):
    return x**2+2*x-35
def fn1(x):
    return 2*x+2
tol=float(input("Enter tolerance like 0.01,0.001,0.0001 etc. "))
a=float(input("Enter any number that can be solution: "))

for i in range(1,51):
    a=a-(fn(a)/fn1(a))
    if abs(fn(a))<=tol:
        break
print("Solution is ",a)