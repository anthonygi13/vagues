#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : animations.py

"""
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation
from main_functions import *


def animate(frame):
    global grille_tn
    global grille_tnm1
    grille_tn, grille_tnm1 = temps_suivant(grille_tn, grille_tnm1, dt, dx, dy, c), grille_tn
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, grille_tn, color='blue')
    print("{}% done".format(int(frame/nframe*100)))

# parametres du probleme (en unite SI)
xmax = 0.5
ymax = 0.5

dt = 0.001
dx = 0.001
dy = 0.001

h = 0.1
g = 9.81
c = np.sqrt(g*h)

x = np.arange(0, xmax, dx)
y = np.arange(0, ymax, dy)
x, y = np.meshgrid(x, y)
x, y = x.T, y.T

# conditions initiales (onde plane)
nb_periodes = 5  # entier
T = xmax / nb_periodes
A = 0.025
grille_t0 = h + A*np.cos(x*2*np.pi/T)
grille_t1 = h + A*np.cos((x-c*dt)*2*np.pi/T)

# plot
nframe = 100

fig = plt.figure()
ax = fig.gca(projection='3d')

grille_tnm1 = grille_t0
grille_tn = grille_t1

plot = [ax.plot_surface(x, y, grille_t0, color='blue')]
ax.set_zlim(0, h*2)

# TODO: afficher animation ?

ani = animation.FuncAnimation(fig, animate, frames=nframe, interval=50, repeat=True)
ani.save('wave.mp4')
