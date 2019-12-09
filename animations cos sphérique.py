#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : animations.py

"""Affiche et/ou enregistre les rendus visuels (pour plusieurs conditions initiales differentes eventuellement) (sans interruption !)
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from main_functions import *


# TODO: changer les conditions de periodisation

# parametres du probleme (en unite SI)
xmax = 0.5
ymax = 0.5

dt = 0.0002
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
T = 0.05
A = 0.025
grille_t0 = h + A*np.cos(np.sqrt((x-xmax/2)**2+(y-ymax/2)**2)*2*np.pi/T)  # FIXME: probleme : normalement decroit en 1/r, mais du coup diverge en 0, faudrait trouver un moyen de gerer ca...
grille_t1 = h + A*np.cos((np.sqrt((x-xmax/2)**2+(y-ymax/2)**2)-c*dt)*2*np.pi/T)  # FIXME: en plus de base c pas periodique la solution donc bof bof...

# plot
fig = plt.figure()
ax = fig.gca(projection='3d')

grille_tnm1 = grille_t0
grille_tn = grille_t1

ax.plot_surface(x, y, grille_t0)
ax.set_zlim3d(0, h*2)
plt.pause(dt)

ax.clear()
ax.plot_surface(x, y, grille_t1)
ax.set_zlim3d(0, h*2)
plt.pause(dt)

# FIXME: faire quelque chose pour la lenteur de l'animation et le bug des bords
while plt.get_fignums():
    grille_tn, grille_tnm1 = temps_suivant(grille_tn, grille_tnm1, dt, dx, dy, c), grille_tn
    ax.clear()
    ax.plot_surface(x, y, grille_tn)
    ax.set_zlim3d(0, h * 2)
    plt.pause(dt)
