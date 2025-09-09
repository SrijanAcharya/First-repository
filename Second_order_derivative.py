# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 17:01:07 2025

@author: Student
"""

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
a=float(input(" Enter the point at which we are finding second order derivative: "))
tol1=float(input("Enter tolerance like 0.01,0.001,0.0001: "))
i=0.01
m=(fn1(a+i)-fn1(a))/i
j=i/10
n=(fn1(a+j)-fn1(a))/j
while abs(m-n)>tol1:
    i=i/10
    j=j/10
    m=(fn1(a+i)-fn1(a))/i
    n=(fn1(a+j)-fn1(a))/j
print("second order derivative is ",n)