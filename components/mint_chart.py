from dash import dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("./historical_mints.csv")

historical_mints = dcc.Graph(
    figure=px.line(df, x='blockNumber', y='value'),
    id="historical-mint-chart"
)