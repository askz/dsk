#!/usr/bin/env python3
from pandas import DataFrame, read_csv
from numpy import random

import matplotlib.pyplot as plt
import pandas as pd


filename = "data/insee_postal.csv"
df = read_csv(filename, sep=";")

df2 = DataFrame(data=df, columns=['insee_com','postal_code','nom_comm','nom_dept','nom_region', 'geo_shape', 'code_comm', 'code_dept'])

print(df2.head)
