# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:25:51 2017

@author: yc
"""
import matplotlib.pyplot as plt
###Scatter plot
x = [1,2,3,4,5,6,7]
y = [5,3,4,6,8,3,3]
y2 = [1,2,3,5,6,2,3]
plt.scatter(x,y, label = 'scatter', color = 'b', s = 100 ,marker = "*")
plt.plot(x,y2, label = "Line", color = 'r')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()