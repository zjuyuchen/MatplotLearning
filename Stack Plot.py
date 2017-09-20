# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:25:51 2017

@author: yc
"""
import matplotlib.pyplot as plt
###Stack plot
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
working = [2,3,4,3,2]
playing = [7,8,7,2,2]
eating = [8,6,7,8,13]
plt.stackplot(days, sleeping, working, playing, eating, colors= ['m','r','b','c'])
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()