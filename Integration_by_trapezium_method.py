# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:26:39 2025

@author: Student
"""

def f(x):
    return 2*x+3
a=float(input("Enter lower limit of integral :"))
b=float(input("Enter upper limit of integral :"))
n=int(input("Enter the no of trapezium you want to divide the area under curve :"))
h=(b-a)/n
integral=0
for p in range(0,n):
    integral = integral+(h/2*(f(a+p*h)+f(a+p*h+h)))
print("Answer of the integration is",integral)
