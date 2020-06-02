# python3

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df_ini = pd.read_csv('/home/taimur/Documents/Drilling Data Processing/singer_vert.csv')
df_ini = df_ini[df_ini['Hole Depth']>0]
df_on_btm = df_ini[df_ini['Bit Status']==1]
print(df_ini.shape)

fig = make_subplots(rows = 5, cols = 1)

fig.add_trace(go.Scatter(x = df_on_btm['Hole Depth'], y = df_on_btm['Bit Weight']),
              row=1, col=1)

fig.add_trace(go.Scatter(x = df_on_btm['Hole Depth'], y = df_on_btm['ROP - Fast']),
              row=2, col=1)

fig.add_trace(go.Scatter(x = df_on_btm['Hole Depth'], y = df_on_btm['Diff Press']),
              row=3, col=1)

fig.add_trace(go.Scatter(x = df_on_btm['Hole Depth'], y = df_on_btm['Top Drive RPM']),
              row=4, col=1)

fig.add_trace(go.Scatter(x = df_on_btm['Hole Depth'], y = df_on_btm['Pump Pressure']),
              row=5, col=1)

fig.show()
