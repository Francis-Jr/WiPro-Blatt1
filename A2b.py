# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:59:17 2015

@author: jakobunfried
"""

import math

a = 0.2
b = 2.0
c = 1.0

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2.0 * a) 
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2.0 * a) 

print "x1 = "+str(x1)
print "x2 = " + str(x2)