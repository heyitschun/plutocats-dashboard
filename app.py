from dash import Dash, html, dcc
# import pandas as pd
# import plotly.express as px
import dash_bootstrap_components as dbc

import styles
from catstats import *
from helpers import *
from contracts import *
from constants import *
from callbacks import register_callbacks


# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.MORPH]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Plutostats - A Plutocats Dashboard"

register_callbacks(app)

server = app.server

# App layout
app.layout = dbc.Container([
    dbc.Row([
        html.Div('Plutostats', className="text-info fw-bold text-center fs-3 my-4")
    ]),

    html.Hr(className="border border-dark"),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.Div("Current Reserves", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="current-reserves-label")
            ]),
            dbc.Row([
                html.Div("Circulating Supply", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="circulating-supply-label")
            ]),
            dbc.Row([
                html.Div("Mint Price", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="mint-price-label")
            ]),
            dbc.Row([
                html.Div("Market Price", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="market-price-label")
            ]),
        ]),
        dbc.Col([
            dbc.Row([
                html.Div("Book Value per Cat", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="book-value-label")
            ]),
            dbc.Row([
                html.Div("Mint Premium (ETH)", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="premium-eth-label")
            ]),
            dbc.Row([
                html.Div("Mint Premium (%)", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="premium-percent-label")
            ]),
        ])
    ]),

    dcc.Interval(
        id="combined-interval",
        interval=1*DELAY,
        n_intervals=0
    ),

    html.Hr(),

    html.Footer([
        html.Div("Discord for suggestions:", className="text-center"),
        html.Div("@zkchun", className="text-center"),
        html.Div([
            html.Div("Keep this site alive:", className="text-center mt-3"),
            html.Div("0x732b964599313Df7E7Cc0222d6502f1150749f33", className="text-center")
        ])
    ])

], fluid=True)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
