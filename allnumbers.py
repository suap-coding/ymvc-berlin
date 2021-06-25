#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:17:18 2021

@author: mateo
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

df = pd.read_csv('business1.csv')

print(df.columns)

sns.relplot(
    data=df,
    x="stars", y="hours",
     
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
