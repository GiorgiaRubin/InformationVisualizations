import pandas as pd

from collections import Counter

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

!pip install plotly==5.4.0
import plotly.express as px

import plotly.graph_objects as go


sns.set_theme(style="whitegrid", font_scale=3, palette="colorblind")
fig, ax = plt.subplots(figsize=(50, 20))

plt.title('Trend of Some Movie Genres from 1901 to 2017', fontsize=75, pad=50)
plt.xlabel('Years', fontsize=50, labelpad=50)
plt.ylabel('Number of Releases', fontsize=50, labelpad=50)

txt = 'Source: \n "Wiki Movie Plots" (2018) by the user JustinR on Kaggle'
plt.figtext(0.5, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=25)

ax = sns.lineplot(x=list(genretrend('western').keys()),y=list(genretrend('western').values()), lw=5, label="Western")
ax = sns.lineplot(x=list(genretrend('musical').keys()),y=list(genretrend('musical').values()), lw=5, label="Musical")
ax = sns.lineplot(x=list(genretrend('action').keys()),y=list(genretrend('action').values()), lw=5, label="Action")


#INTERACTIVE LINEPLOT

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(genretrend('western').keys()),y=list(genretrend('western').values()),
                    mode='lines',
                    name='Western'))
fig.add_trace(go.Scatter(x=list(genretrend('musical').keys()),y=list(genretrend('musical').values()),
                    mode='lines',
                    name='Musical'))
fig.add_trace(go.Scatter(x=list(genretrend('action').keys()),y=list(genretrend('action').values()),
                    mode='lines',
                    name='Action'))
fig.add_trace(go.Scatter(x=list(genretrend('drama').keys()),y=list(genretrend('drama').values()),
                    mode='lines',
                    name='Drama',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('comedy').keys()),y=list(genretrend('comedy').values()),
                    mode='lines',
                    name='Comedy',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('horror').keys()),y=list(genretrend('horror').values()),
                    mode='lines',
                    name='Horror',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('thriller').keys()),y=list(genretrend('thriller').values()),
                    mode='lines',
                    name='Thriller',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('romance').keys()),y=list(genretrend('romance').values()),
                    mode='lines',
                    name='Romance',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('crime').keys()),y=list(genretrend('crime').values()),
                    mode='lines',
                    name='Crime',
                    visible="legendonly"))
fig.add_trace(go.Scatter(x=list(genretrend('adventure').keys()),y=list(genretrend('adventure').values()),
                    mode='lines',
                    name='Adventure',
                    visible="legendonly"))

fig.update_layout(title= "Trend of Some Movie Genres from 1901 to 2017", legend_title = "Genres (Click to show)", plot_bgcolor = "#fff")
fig.update_xaxes(title= 'Years<br><sup>Source: "Wiki Movie Plots" (2018) by the user JustinR on Kaggle</sup>', gridcolor = "#DCDCDC")
fig.update_yaxes(title= 'Number of Releases', gridcolor = "#DCDCDC")
                     
fig.show()
