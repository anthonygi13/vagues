#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : animations.py

"""Script qui fait la modelisation et cree les animations
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation
from main_functions import *


def conditions_initiales1(nb_periodes=5, A=0.025):
    """
    Conditions initiales pour onde plane
    :param nb_periodes: nombre de periodes spatiales dessinees
    :param A: amplitude de l'onde
    :return: grilles initiales aux temps t0 et t1
    """
    check_nb_periodes(nb_periodes)
    T = xmax / nb_periodes
    grille_t0 = h + A * np.cos(x * 2 * np.pi / T)
    grille_t1 = h + A * np.cos((x - c * dt) * 2 * np.pi / T)
    return grille_t0, grille_t1


def conditions_initiales2(nb_periodes_x=2, nb_periodes_y=2, A=0.025):
    """
    Conditions initiales pour une onde interessante visuellement
    :param nb_periodes_x: nombre de periodes spatiales dessinees pour l'onde se propageant suivant x
    :param nb_periodes_y: nombre de periodes spatiales dessinees pour les ondes se propageant suivant y
    :param A: amplitude caracteristique de l'onde
    :return: grilles initiales aux temps t0 et t1
    """
    check_nb_periodes(nb_periodes_x)
    check_nb_periodes(nb_periodes_y)
    Tx = xmax / nb_periodes_x
    Ty = ymax / nb_periodes_y
    grille_t0 = h + A*np.cos(x*2*np.pi/Tx) + A/2*np.cos(y*2*np.pi/Ty + np.pi/2) + A/2*np.cos(y*2*np.pi/Ty + np.pi/2)
    grille_t1 = h + A*np.cos((x-c*dt)*2*np.pi/Tx) + A/2*np.cos((y-c*dt)*2*np.pi/Ty + np.pi/2) + A/2*np.cos((y+c*dt)*2*np.pi/Ty + np.pi/2)
    return grille_t0, grille_t1


def check_nb_periodes(nb_periodes):
    """
    Verifie que nb_periode soit un entier pour qu'on puisse mettre des conditions au bord periodiques
    :param nb_periodes: un nombre de periodes spatiales dessinees
    """
    if type(nb_periodes) != int:
        raise TypeError("Le nombre de periodes nb_periodes doit etre un entier (pour la periodisation).")


def animate(frame, animation_id):
    """
    Fonction appelee pour la creation de chaque frame de l'animation
    :param frame: numero de la frame
    :param animation_id: numero de l'animation
    """
    global grille_tn
    global grille_tnm1
    grille_tn, grille_tnm1 = temps_suivant(grille_tn, grille_tnm1, dt, dx, dy, c), grille_tn
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, grille_tn, color='blue')
    print("Animation {}/{}: {}% done".format(animation_id+1, len(conditions_initiales), int(frame/nframe*100)))


# parametres du probleme (en unite SI)
xmax = 0.5
ymax = 0.5

dt = 0.0005
dx = 0.001
dy = 0.001

h = 0.1
g = 9.81
c = np.sqrt(g*h)


# settings
x = np.arange(0, xmax, dx)
y = np.arange(0, ymax, dy)
x, y = np.meshgrid(x, y)
x, y = x.T, y.T


# animations
nframe = 300
conditions_initiales = (conditions_initiales1, conditions_initiales2)

for i, condition_initiale in enumerate(conditions_initiales):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    grille_tnm1, grille_tn = condition_initiale()

    plot = [ax.plot_surface(x, y, grille_tnm1, color='blue')]
    ax.set_zlim(0, h*2)

    ani = animation.FuncAnimation(fig, animate, fargs=(i,), frames=nframe, interval=25, repeat=True)
    ani.save('wave{}.mp4'.format(i+1))
