# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:06:05 2023

@author: aa23ajh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bcs = pd.read_csv("BCS_ann.csv")
bp= pd.read_csv("BP_ann.csv")
tsco= pd.read_csv("TSCO_ann.csv")
vod= pd.read_csv("vod_ann.csv")

plt.Figure()

plt.subplot(2, 2, 1)
plt.hist(bcs["ann_return"], label="Barclays")

plt.legend()
plt.ylabel("N")
plt.xlabel("returns (%)")

plt.subplot(2, 2, 2)
plt.hist(bp["ann_return"], label="BP")
plt.legend()

plt.subplot(2, 2, 3)
plt.hist(tsco["ann_return"], label="TESCO")
plt.legend()
plt.xlabel("returns (%)")
plt.ylabel("N")

plt.subplot(2, 2, 4)
plt.hist(vod["ann_return"], label="VODAPHONE")

plt.legend()
plt.xlabel("returns (%)")
plt.show()

plt.Figure()
plt.hist(tsco["ann_return"], label="TESCO" , alpha=0.7,density=True)

plt.legend()
plt.xlabel("returns (%)")
plt.ylabel("N")
plt.show()

plt.Figure()

plt.boxplot([bcs["ann_return"], bp["ann_return"], tsco["ann_return"], vod["ann_return"]], 
             labels=["Barclays", "BP", "Tesco", "Vodaphone"])

cap = np.array([33367, 68785, 20979, 29741])
stocks = ["Barclays", "BP", "Tesco", "Vodaphone"]

ftse = 1814000
cap = cap/ftse

plt.figure()
plt.pie(cap, labels=stocks, normalize=True)
plt.show()

print(cap)
