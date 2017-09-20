# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:32:53 2017

@author: yc
"""

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

x, y = np.loadtxt('test.txt', delimiter=' ', unpack=True)

plt.plot(x,y, label = "Probe")
plt.xlabel("Time")
plt.ylabel("Probe_T(K)")
plt.legend()
plt.show()