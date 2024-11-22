import pandas as pd
import plotly.express as px
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_pickle('/content/drive/MyDrive/Colab Notebooks/LocationData-processed.pkl')

px.set_mapbox_access_token('pk.eyJ1IjoidGFrYWhhc3IiLCJhIjoiY20yZHJtMG9nMTZqMTJqb24zNzdjbjNneiJ9.9HzFVcQz7xZB50YTLp1QiA')

df_2 = df.loc['2020-04-20 00:00:00.000':'2020-04-27 23:59:59.999']

fig2 = px.scatter_mapbox(df_2,
                        lat = 'latitude',
                        lon = 'longitude' )
fig2.show()

fig1 = px.density_mapbox(df_2,
                        lat = 'latitude',
                        lon = 'longitude',
                        radius = 10,
                        zoom = 10)

fig1.show()

fig2.write_html('fig2.html')
fig1.write_html('fig1.html')
