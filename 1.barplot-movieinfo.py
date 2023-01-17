import pandas as pd

from collections import Counter

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

!pip install plotly==5.4.0
import plotly.express as px

import plotly.graph_objects as go

#vertical barplot

sns.set_theme(style="whitegrid", font_scale=3)
fig, ax = plt.subplots(figsize=(50, 20))

ax = sns.barplot(x=movieinfo("Genre")[0][1:20], y=movieinfo("Genre")[1][1:20])
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

txt = 'Source: \n "Wiki Movie Plots" (2018) by the user JustinR on Kaggle'
plt.figtext(0.5, -0.2, txt, wrap=True, horizontalalignment='center', fontsize=25)

plt.title('Most Produced Film Genres from 1901 to 2017', fontsize=75, pad=50)
plt.xlabel('Genres', fontsize=50, labelpad=50)
plt.ylabel('Number of Releases', fontsize=50, labelpad=50)

#orizontal barplot

sns.set_theme(style="whitegrid", font_scale=3)
fig, ax = plt.subplots(figsize=(50, 20))

ax = sns.barplot(y=movieinfo("Genre")[0][1:20], x=movieinfo("Genre")[1][1:20])

txt = 'Source: \n "Wiki Movie Plots" (2018) by the user JustinR on Kaggle'
plt.figtext(0.5, -0.01, txt, wrap=True, horizontalalignment='center', fontsize=25)

plt.title('Most Produced Film Genres from 1901 to 2017', fontsize=75, pad=50)
plt.xlabel('Genres', fontsize=50, labelpad=50)
plt.ylabel('Number of Releases', fontsize=50, labelpad=50)
