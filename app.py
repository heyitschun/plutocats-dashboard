# Import packages
import requests
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from catstats import *
from helpers import *
from contracts import *
from constants import *
import styles


# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.MORPH]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Plutostats - A Plutocats Dashboard"

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
                html.Div("Circulating Cats", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="circulating-supply-label")
            ]),
            dbc.Row([
                html.Div("Mint Price", className=styles.stat_label),
                html.Div("0.0", className=styles.stat_value, id="mint-price-label")
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
            id="datatable-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="book-value-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="current-reserves-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="circulating-supply-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="mint-price-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="premium-eth-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),
    dcc.Interval(
            id="premium-percent-interval",
            interval=1*DELAY, # in milliseconds
            n_intervals=0
    ),

    html.Hr(),

    dbc.Row([
        html.Div("Tag me in the Plutocats Discord for suggestions:", className="text-center"),
        html.Div("@zkchun", className="text-center")
    ]),

    dbc.Row([
        html.Div("Keep this site alive:", className="text-center mt-3"),
        html.Div("0x732b964599313Df7E7Cc0222d6502f1150749f33", className="text-center")
    ]),

], fluid=True)


@callback(
    Output("book-value-label", "children"),
    Input("book-value-interval", "n_intervals")
)
def update_book_value(n):
    book_value = get_book_per_cat()
    return format_to_eth_string(book_value)

@callback(
    Output("mint-price-label", "children"),
    Input("mint-price-interval", "n_intervals")
)
def update_mint_price(n):
    price_wei = get_price()
    return format_to_eth_string(price_wei)

@callback(
    Output("current-reserves-label", "children"),
    Input("current-reserves-interval", "n_intervals")
)
def update_current_reserves(n):
    current_reserve = get_current_reserve()
    return format_to_eth_string(current_reserve)

@callback(
    Output("circulating-supply-label", "children"),
    Input("circulating-supply-interval", "n_intervals")
)
def update_circulating_supply(n):
    current_supply = get_adjusted_total_supply()
    return current_supply

@callback(
    Output("premium-eth-label", "children"),
    Input("premium-eth-interval", "n_intervals")
)
def update_premium_eth(n):
    premium = get_price() - get_book_per_cat()
    return format_to_eth_string(premium)

@callback(
    Output("premium-percent-label", "children"),
    Input("premium-percent-interval", "n_intervals")
)
def update_premium_percent(n):
    book = get_book_per_cat()
    premium = get_price() - book
    premium_percent = f"{premium/book * 100:.2f}%"
    return premium_percent

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
