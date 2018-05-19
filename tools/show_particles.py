#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:39:23 2018

@author: Loann Brahimi
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------ Structure de la grille de calcul -------------------------------------
ti = 0     # Instant initial 
tf = 3e0    # Instant final 
dt = 1e-3  # Incrément linéaire de temps
nstept = int((tf-ti)/dt) # Nombre de pas temporels de la simulation

N = 50; 
file_name = "../out/body_" 
ext = ".dat"
myfile_name = []

for ii in range(N) : 
    myfile_name.append(file_name+str(ii)+ext)
    print myfile_name[ii]

data = []
for ii in range(N) : 
    data.append(open(myfile_name[ii], 'r').readlines())
    for jj in range(len(data[ii])) : 
        data[ii][jj] = data[ii][jj].split()
        for col in range(len(data[ii][jj])) : 
            data[ii][jj][col] = float(data[ii][jj][col])

time = []
for ii in range(len(data[0])) : 
    time.append(data[0][ii][0])

rx = np.zeros((N, len(time)))
ry = np.zeros((N, len(time)))

for ii in range(N) : 
    for jj in range(len(data[ii])) : 
        rx[ii,jj] = data[ii][jj][1]
        ry[ii,jj] = data[ii][jj][2]

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Loann Brahimi'), bitrate=1800)

def update_line(num, data, line):
#    line.set_data(data[...,:num])
    line.set_data(data[...,num])
    return line,


fig = plt.figure(facecolor="black")
plt.style.use('dark_background')
l, = plt.plot([], [], ',', color='white')

line_ani = animation.FuncAnimation(fig, update_line, nstept, fargs=(np.array([rx[:,:], ry[:,:]]), l),
    interval=10, blit=True, repeat=True)

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.show()


#for ii in range(N) : 
#    plt.plot(rx[ii], ry[ii], '-')
#plt.show()
