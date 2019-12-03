#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : functions.py


import matplotlib.pyplot as plt
import numpy as np


def partial2_x(grille, dx):
    res = np.zeros(grille.shape)
    res[1:-1] = (grille[2:] - 2*grille[1:-1] + grille[:-2]) / dx**2
    res[0] = res[1]
    res[-1] = res[-2]
    return res


def partial2_y(grille, dy):
    res = np.zeros(grille.shape)
    res[:, 1:-1] = (grille[:, 2:] - 2 * grille[:, 1:-1] + grille[:, :-2]) / dy**2
    res[:, 0] = res[:, 1]
    res[:, -1] = res[:, -2]
    return res


def temps_suivant(grille_tn, grille_tnm1, dt, dx, dy, c):
    """
    :param grille_tnm1: configuration au temps t_(n-1)
    :param grille_tnm2: configuration au temps t_(n-2)
    :param dt: pas de temps
    :return: configuration au temps t_n
    """
    return dt**2 * c**2 * (partial2_x(grille_tn, dx) + partial2_y(grille_tn, dy)) + 2*grille_tn - grille_tnm1
