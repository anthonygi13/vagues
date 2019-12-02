#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File : animations.py

"""Affiche et/ou enregistre les rendus visuels (pour plusieurs conditions initiales differentes eventuellement) (sans interruption !)
"""

import matplotlib.pyplot as plt
import numpy as np
from main_functions import *

xmax = 0.5
ymax = 0.5

dt = 0.01
dx = xmax
ymax = 