import pandas as pd

from collections import Counter

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

!pip install plotly==5.4.0
import plotly.express as px

import plotly.graph_objects as go

fig = px.treemap(disney3, path=["year", "movie_title"], values="total_gross")
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.show()
