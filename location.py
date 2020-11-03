# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:39:51 2020

@author: allan
"""


import csv

f = open("air_data_monitor_locations.csv", "r")
g = open("PM2.5_dataset.csv", "r")
h = open("final.csv","w", newline='')

replace = {}
for line in f:
    station,lat,long = line.split(",")
    replace[station] = lat.strip(),long.strip()
        
for lineas in g:
    text = lineas.strip()
    text = text.split(",")
    if text[1] in replace.keys():
        lat,long = replace[text[1]]
        text.append(lat)
        text.append(long)
    csv.writer(h).writerow(text)
    
f.close()
g.close()
h.close()
        



    
