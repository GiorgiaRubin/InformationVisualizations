import pandas as pd

from collections import Counter

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

!pip install plotly==5.4.0
import plotly.express as px

import plotly.graph_objects as go

fig, ax = plt.subplots(figsize=(50, 20))

plt.title('Revenues of Disney Movies by Genre', fontsize=75, pad=50)
plt.xlabel('Years', fontsize=50, labelpad=50)
plt.ylabel('Genres', fontsize=50, labelpad=50)

txt = 'Source: \n "Disney Movies 1937-2016 Gross Income" by the user Rashik Rahman on Kaggle'
plt.figtext(0.5, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=25)

ax = sns.scatterplot(x=disney3["year"], y=disney3["genre"], size=disney3["total_gross"], 
                     sizes=(100,10000), hue=disney3["genre"], legend=False)
