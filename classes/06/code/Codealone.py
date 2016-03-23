# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:36:21 2016

@author: black
"""

C:\Users\Michael_Lin\Google Drive\My Academic Files\General Assembly\Github-repo\GA-DAT-SF-21\classes\06\datasets
C:/Users/Michael_Lin/Google Drive/My Academic Files/General Assembly/Github-repo/GA-DAT-SF-21/classes/06/datasets


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

pd.set_option('display.max_rows', 10)
pd.set_option('display.notebook_repr_html', True)
pd.set_option('display.max_columns', 10)

%matplotlib inline
plt.style.use('ggplot')

def read_dataset():
    return pd.read_csv(os.path.join('..', 'datasets', 'zillow-06-starter.csv'), index_col = 'ID')

df = read_dataset()
df.head()

model = smf.ols(formula = 'SalePrice~Size', data = df).fit()

model.summary()

