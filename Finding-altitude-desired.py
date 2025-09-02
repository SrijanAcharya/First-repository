# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 11:21:48 2025

@author: Student
"""

import numpy as np
T=float(input("Enter the time period of the satellite in second: "))
G=6.67*(10**(-11))
M=6.0*(10**24)
R=6271
h=(G*M*(T**2)/(4*(np.pi)**2))**(1/3)-R
print("Your desired altitude should be",h,"meters")