#!/usr/bin/env python3
import pandas
from matplotlib import pyplot as plt
import matplotlib as mpl
from descartes import PolygonPatch
import json as simplejson
import numpy as np
import os


data = pandas.read_csv("data/accidents.csv",sep=',')
accid_df = pandas.DataFrame({'code_comm' : data['code_comm'], 'accidents' : 1})
accid_df = accid_df.groupby('code_comm').sum()

data = pandas.read_csv('data/insee_postal.csv', sep=';')
insee_df = pandas.DataFrame(data=data, columns=['code_comm', 'insee_com', 'nom_comm', 'geo_shape', 'code_dept'])
insee_df.set_index('code_comm')

result = pandas.concat((insee_df, accid_df), axis=1)
result['accidents'].fillna(0, inplace=True)
result = result.sort('insee_com', ascending=True)

dept_df = result.groupby('code_dept').sum()
result.set_index('code_dept')

result = pandas.concat((result, dept_df), axis=1)
print(result)
# result.to_csv('test.csv')

# data = pandas.read_csv('test.csv')

# print(data)

# fig = plt.figure(figsize=(20,20))
# ax = fig.add_subplot(111)
# patches = []
 
# for geojson, accidents in zip(result["geo_shape"], result["accidents"]):
#     #turn json into a python object
#     poly = simplejson.loads(geojson)
#     try:
#         patch = PolygonPatch(poly, fc=plt.cm.autumn_r(accidents/100), ec="k", zorder=1, lw=0.3)
#         ax.add_patch(patch)
#     except:
#         pass

# ax.set_xlim(-5,10)
# ax.set_ylim(40.3, 51.)
# ax.axis("off")
# norm = mpl.colors.Normalize(vmin = result["accidents"].min(), vmax = result["accidents"].max())
# ax1 = fig.add_axes([0.1, 0.052, 0.85, 0.053])
# cb1 = mpl.colorbar.ColorbarBase(ax1, cmap = plt.cm.autumn_r,
#                                    norm = norm,
#                                    orientation = "horizontal")
# cb1.set_label("accidents")

# plt.savefig("accidents.png")