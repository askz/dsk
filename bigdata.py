#!/usr/bin/env python3
import pandas
from matplotlib import pyplot as plt
import matplotlib as mpl
from descartes import PolygonPatch
import json as simplejson
import numpy as np

data = pandas.read_csv("pub/accidents.csv",na_values='9999')
# data = pandas.read_csv("vehicules.csv",dtype=object)
com = data['com']

print(com)

counts = com.value_counts(sort=False)
print(counts)


#data.plot(legend=False)
#plt.savefig('test.png')
