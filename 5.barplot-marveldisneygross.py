import pandas as pd

from collections import Counter

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

!pip install plotly==5.4.0
import plotly.express as px

import plotly.graph_objects as go

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)
        

fig, ax = plt.subplots(figsize=(50, 20))
sns.set_theme(style="whitegrid", font_scale=3)

plt.title('Revenues of Disney/Marvel compared', fontsize=75, pad=50)
plt.xlabel('Years', fontsize=50, labelpad=50)
plt.ylabel('Revenues (in Billions)', fontsize=50, labelpad=50)

txt = 'Source: \n "Disney Movies 1937-2016 Gross Income" by the user Rashik Rahman on Kaggle and Wikipedia'
plt.figtext(0.5, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=25)

ax = sns.barplot(x=list(yearrange2),y=marveltotalgross,color="#fa4d56",zorder=2)
ax = sns.barplot(x=list(yearrange2),y=totalgross,color="#1192e8",zorder=1)

show_values(ax)
