# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

h=float(input("Enter the height of the tower in metres: "))
t=float(input("Enter the time in second for which the ball is falling: "))
g=float(input("Enter value of acceleration due to gravity in m/s^2: "))
S=0.5*g*t**2
X=h-S
print("The ball is",X,"metre above from the ground.")