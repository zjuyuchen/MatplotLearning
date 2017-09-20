# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:27:25 2017

@author: yc
"""

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
working = [2,3,4,3,2]
playing = [7,8,7,2,2]
eating = [8,6,7,8,13]

slices = [7,2,2,13]
colors = ['g','b','r','c','k']
activities = ['sleeping','working','playing','eating']

plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.title("Pie Plot")
plt.show()