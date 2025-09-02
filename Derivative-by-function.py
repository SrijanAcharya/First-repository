# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 17:05:25 2025

@author: Student
"""

def derivative_of_cos_using_function(y):
    """Enter the point at which you find the derivative. for 3pi enter 3 , for pi/2 enter 0.5 etc. :"""
    import numpy as np
    def f(x):
        return np.cos(x)
    tol=0.000000000001
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
    return print("The result of derivative",q)