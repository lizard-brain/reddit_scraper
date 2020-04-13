import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('0_stats.csv')
print (df)

fig = go.Figure(go.Scatter(x = df['localtime_human'], y = df['percent'],
                  name='Poop'))
'''
fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
'''
fig.show()

