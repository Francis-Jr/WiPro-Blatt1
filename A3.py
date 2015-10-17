# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:07:00 2015

@author: jakobunfried
"""

F = 47

F = F/1.0
C = 5.0 / 9.0 * (F-32)
print C

agg = "fluessig"
if C <= 0:
    agg = "fest"
if C >= 100:
    agg = "gasfoermig"
    
print agg