#!/usr/bin/env python3
import pandas
from matplotlib import pyplot as plt
import matplotlib as mpl
from descartes import PolygonPatch
import json as simplejson
import numpy as np
import os

if os.path.isdir("data"):
  data = pandas.read_csv("data/accidents.csv",na_values='9999')
else:
  print("Please run 'make download' to grab data required by this tool!\n")
#data = pandas.read_csv("vehicules.csv",dtype=object)
com = data['com']

print(com)

counts = com.value_counts(sort=True)

print(counts)


#data.plot(legend=False)
#plt.savefig('test.png')
