# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import *

def get_distance(array_1, array_2):
    lon_a = array_1[0]
    lat_a = array_1[1]
    lon_b = array_2[0]
    lat_b = array_2[1]
    radlat1 = radians(lat_a)
    radlat2 = radians(lat_b)
    a = radlat1 - radlat2
    b = radians(lon_a) - radians(lon_b)
    s = 2 * asin(sqrt(pow(sin(a/2),2) + cos(radlat1) * cos(radlat2)*pow(sin(b/2),2)))
    earth_radius = 6378137
    s = s * earth_radius
    return s

beer = pd.read_excel(r'C:\Users\13186\Desktop\tmp\station_gps.xlsx',sep = ' ')
beer.isnull()
beer.dropna(inplace=True)
X = beer[['longitude','latitude']]
db = DBSCAN(eps = 500, min_samples=2,metric= get_distance).fit(X)

labels = db.labels_
beer['cluster_db'] = labels
beer.sort_values('cluster_db')
#统计分类后各簇的数目
point_count = beer.groupby('cluster_db').agg({'latitude':'count'})
#筛选数值大于500的类簇（交通热点阈值）
# hot_station =list(filter(lambda x:  int(x['latitude']) >1000, point_count.iterrows))
hot_station = []
for index, row in point_count.iterrows():
   if int(row['latitude']) > 1000 :
       hot_station.append(index)
       print index,row['latitude']
# print(hot_station)

hot_station1 = []
# for x in point_count:
#     hot_station1.append(x)
#     print(x)

#筛选后，分析各个簇的经纬度的均值
if len(hot_station) > 0 :
    # beer['cluster_db'] = hot_station
    print(beer.groupby(beer['cluster_db']).mean())
#画图
plt.ylim(22.4, 23.9)
plt.xlim(112.9,114.1)
plt.scatter(beer['longitude'],beer['latitude'],c = beer['cluster_db'])
plt.legend(labels = beer['cluster_db'] )
plt.show()