#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:59:14 2021

@author: mateo
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

df = pd.read_csv('yelp_dataset.csv')

#Location vs Stars
all_cities = df['address'].values.tolist()
a = list(set(all_cities))
h = len(a)
#Average Value for city -> make dictionary with city and all values
for n in range(len(df)):
   for a in range(h):
       b[all_cities[a]] = df.loc[n, 'stars']
       b[all_cities[a]].append(df.loc[n, 'stars'])

print(b)