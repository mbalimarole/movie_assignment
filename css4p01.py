# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:41:39 2024

@author: mbali
"""

import pandas as pd 
df = pd.read_csv("movie_dataset.csv", sep=";")
df = pd.read_csv("movie_dataset.csv",sep=";",index_col=0)

import pandas as pd

df = pd.read_csv("movie_dataset.csv",sep=";")

pd.set_option('display.max_rows',None)

print(df)

df.dropna(inplace = True)
df = df.reset_index(drop=True)
df.drop_duplicates(inplace = True)

print(df.info())
print(df.describe())









