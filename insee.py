#!/usr/bin/env python3
from pandas import DataFrame, read_csv
from numpy import random

import matplotlib.pyplot as plt
import pandas as pd

# data files
insee_data = "data/insee_postal.csv"
accid_data = "data/accidents.csv"

# readings CSVs and parsing with separator 
insee_df = read_csv(insee_data, sep=";")
accid_df = read_csv(accid_data, sep=",")

# selecting columns
insee_df = DataFrame(data=insee_df, columns=['code_comm', 'insee_com', 'nom_comm', 'postal_code', 'nom_dept', 'nom_region', 'geo_shape', 'code_dept'])
accid_df = DataFrame(data=accid_df, columns=['numac', 'lum', 'agg', 'int', 'atm', 'col', 'adr', 'dep', 'code_comm', 'gps', 'lat', 'long', 'catr', 'voie', 'v1', 'v2', 'infra', 'situ', 'circ', 'nbv', 'vosp', 'prof', 'plan', 'ttue', 'tbg', 'tbl', 'tindm', 'numero', 'libellevoie', 'grav'])


merged = DataFrame.merge(accid_df, insee_df, how='outer', on='code_comm', copy=False)

print(merged.info)