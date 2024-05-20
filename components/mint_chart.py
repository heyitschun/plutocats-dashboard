from dash import dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("./historical_mints.csv")

fig = px.line(df, x="blockNumber", y="value")
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)


historical_mints = dcc.Graph(
    figure=fig,
    id="historical-mint-chart"
)