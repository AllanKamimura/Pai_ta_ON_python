# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:24:49 2020

@author: allan
"""

import math
n = (8*int(input(""))+1)**0.5
if math.floor(n) == math.ceil(n):
    print("YES")
else:
    print("NO")
