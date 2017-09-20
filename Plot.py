# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:25:50 2017

@author: yc
"""

x = [1,2,3,4]
y = [4,5,6,7]

x2 = [1,2,3,4]
y2 = [10,11,12,13]

plt.plot(x,y)
plt.plot(x2,y2)
plt.xlabel("Plot number X")
plt.ylabel("Interesting Graph Y")
plt.title("Interesting graph\nCheck it out")
plt.legend()
plt.show()