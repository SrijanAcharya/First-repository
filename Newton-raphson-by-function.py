# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 16:01:28 2025

@author: Student
"""

def solution_by_newton_raphson(a,tol1):
    """ (Enter any number that can be solution: ,Enter tolerance like 0.01,0.001,0.0001 etc. )"""
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
    
    y=fn1(a)
    print(y)
    while abs(fn(a))>tol1:
        a=a-(fn(a)/fn1(a))
    return print("Solution is ",a)