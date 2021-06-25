#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:24:33 2021

@author: mateo
"""

print('hello')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

df = pd.read_csv('yelp_dataset.csv')

print(df.columns)

print(df['attributes'])

