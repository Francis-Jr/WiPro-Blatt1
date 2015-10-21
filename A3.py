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
if C <= 0.:
    agg = "fest"
elif C >= 100.:
    agg = "gasfoermig"
    
    
"""ODER analog zu a ? b : c """
s =  "fest" if C<0. else "gas" if C > 100. else "fluessig"
