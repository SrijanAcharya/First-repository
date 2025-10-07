# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 11:23:16 2025

@author: Student
"""

def f(x):
    return 2*x*x
a=float(input("Enter lower limit of integral :"))
b=float(input("Enter upper limit of integral :"))
n=int(input("Enter the no of trapezium you want to divide the area under curve :"))
h=(b-a)/n
q=f(a)+f(b)
add=0
for p in range(1,n):
    add=add+(f(a+p*h))
answer=(2*add+q)*h/2
print("Result of integration :",answer)