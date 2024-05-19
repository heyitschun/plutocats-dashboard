from dash import html
import dash_bootstrap_components as dbc
import styles

trackers = dbc.Row([
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
            html.Div("Quit Price", className=styles.stat_label),
            html.Div("0.0", className=styles.stat_value, id="book-value-label")
        ]),
        dbc.Row([
            html.Div("Quit + Royalties", className=styles.stat_label),
            html.Div("0.0", className=styles.stat_value, id="quit-royalties-label")
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