# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:49:21 2017

@author: yc
"""

import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
def graph_data(stock):
    stock_price_url = 'https://finance.yahoo.com/quote/ALNY/history?p=ALNY'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    print(source_code)
    
#    stock_data = []
#    split_source = source_code.split('\n')
#    plt.xlabel('year')
#    plt.ylable('price')
#    plt.title('Stock:' stock)
#    plt.legend()
#    plt.show()
graph_data('TSLA')
    
    