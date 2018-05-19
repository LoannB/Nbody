#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:46:07 2018

@author: Loann Brahimi
"""

import numpy as np
import matplotlib.pyplot as plt 
import freader as fr

dim = int(fr.search("dimension","../parameters/structure.txt")[0])
N   = int(fr.search("num_bodies","../parameters/main_parameters.txt")[0]) 
myfile_title = "../dist/"


#N = 50

#myfile_title = "../dist/"
ext = ".dat"
dist = "uniform_circle"
myfile_title +=dist
myfile_title+=ext

myfile = open(myfile_title, "w")

rx = np.zeros(N)
ry = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)




if (dist == "uniform_rectangle") : 
    for ii in range(N) : 
        rx[ii] = np.random.uniform(low=-1.0, high=1.0)
        ry[ii] = np.random.uniform(low=-1.0, high=1.0)
        vx[ii] = np.random.uniform(low=-1.0, high=1.0)
        vy[ii] = np.random.uniform(low=-1.0, high=1.0)
if (dist == "uniform_circle") : 
    for ii in range(N) : 
        r = np.random.uniform(low=0., high=1.0)
        theta = np.random.uniform(low=0., high=2.*np.pi)
        rx[ii] = r*np.cos(theta)
        ry[ii] = r*np.sin(theta)
        vr = 1#np.random.uniform(low=0., high=1.0)
        v_theta = 1#np.random.uniform(low=0., high=2.*np.pi)
        vx[ii] = vr*r**(-1)*np.cos(v_theta)
        vy[ii] = vr*r**(-1)*np.sin(v_theta)  


plt.figure()
plt.plot(rx, ry, ',')

plt.figure()
plt.plot(vx, vy, ',')



for ii in range(N) : 
    myfile.write(str(ii)+"\t"+str(rx[ii])+"\t"+str(ry[ii])+"\t"+str(vx[ii])+"\t"+str(vy[ii])+"\n")

myfile.close()
    
