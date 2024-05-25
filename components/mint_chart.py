from dash import dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("./historical_mints.csv")

fig = px.line(df, x="blockNumber", y="value")

fig.add_shape(
    type='line',
    x0=df["blockNumber"].min(), x1=df["blockNumber"].max(),
    y0=0.0, y1=0.0,
    line=dict(color='floralwhite', dash='dot')
)

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

historical_mints = dcc.Graph(
    figure=fig,
    id="historical-mint-chart"
)