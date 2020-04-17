import pandas as pd
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')

## splitting properties ##
properties = []
with open('properties.txt') as fp:
    line = fp.readline()
    line = fp.readline()
    while line and len(line) > 0:
        line = fp.readline()
        properties.append(line[3:-1])
        
propsDf = df["PROPERTIES"].str.split(",", expand=True) 
for i in range(len(properties)):
    prop = properties[i]
    df[prop] = propsDf[i].astype("float64")
df.drop(columns="PROPERTIES",inplace=True)
