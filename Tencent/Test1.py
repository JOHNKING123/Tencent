# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import *

beer = pd.read_excel(r'C:\Users\13186\Desktop\tmp\test1.xlsx',sep = ' ')
beer.isnull()
beer.dropna(inplace=True)

print beer

beer['c'] = ['x','x','z']

print beer

rs =  beer.groupby('c').agg({'a':'count'})
print rs


# hot_station =list(filter(lambda x:  int(x) >1, rs))
hot_station = []

for index, row in rs.iterrows():
    # print(index) # 输出每行的索引值
    print index,row['a']
