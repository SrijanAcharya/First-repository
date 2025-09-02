# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 16:42:45 2025

@author: Student
"""

def fn(x):
    return x**2+2*x-35

def fn1(x):

    def f(x):
        return x**2+2*x-35
    tol=0.0000000001
    
    h=0.01
    p=(f(x+h)-f(x-h))/(2*h)
    k=h/10
    q=(f(x+k)-f(x-k))/(2*k)
    while abs(p-q)>tol:
        h=h/10
        k=k/10
        p=(f(x+h)-f(x-h))/(2*h)
        q=(f(x+k)-f(x-h))/(2*k)
    return q

tol1=float(input("Enter tolerance like 0.01,0.001,0.0001 etc. "))
a=float(input("Enter any number that can be solution: "))
y=fn1(a)
print(y)
while abs(fn(a))>tol1:
    a=a-(fn(a)/fn1(a))
print("Solution is ",a)



