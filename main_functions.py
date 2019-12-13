#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : main_functions.py

"""Fonctions qui calcule l'evolution de la grille des hauteurs de la vague
"""

import numpy as np


def partial2_x(grille, dx):
    """
    :param grille: grille des hauteurs
    :param dx: pas de discretisation suivant les x
    :return: grille des derivees secondes de la hauteur par rapport a x
    """
    grilleBackward = np.roll(grille, -1, axis=1)
    grilleForward = np.roll(grille, 1, axis=1)
    res = (grilleForward - 2*grille + grilleBackward) / dx**2  # conditions aux bords periodiques
    return res


def partial2_y(grille, dy):
    """
    :param grille: grille des hauteurs
    :param dx: pas de discretisation suivant les y
    :return: grille des derivees secondes de la hauteur par rapport a y
    """
    grilleBackward = np.roll(grille, -1, axis=0)
    grilleForward = np.roll(grille, 1, axis=0)
    res = (grilleForward - 2*grille + grilleBackward) / dy**2  # conditions aux bords periodiques
    return res


def temps_suivant(grille_tn, grille_tnm1, dt, dx, dy, c):
    """
    :param grille_tnm1: configuration au temps t_(n-1)
    :param grille_tnm2: configuration au temps t_(n-2)
    :param dt: pas de discretisation du temps
    :return: configuration au temps t_n
    """
    return dt**2 * c**2 * (partial2_x(grille_tn, dx) + partial2_y(grille_tn, dy)) + 2*grille_tn - grille_tnm1
