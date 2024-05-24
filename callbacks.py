import requests
import pandas as pd
import plotly.express as px
from database import engine
from dash.dependencies import Input, Output
from dash import Dash
from catstats import *
from scraper import *
from urls import parse_normal_transations_url

def update_book_value() -> str:
    book_value = get_book_per_cat()
    return format_to_eth_string(book_value)

def update_book_royalties() -> str:
    quit_plus = get_quit_plus_royalties()
    return format_to_eth_string(quit_plus)

def update_mint_price() -> str:
    price_wei = get_price()
    return format_to_eth_string(price_wei)

def update_current_reserves() -> str:
    current_reserve = get_current_reserve()
    return format_to_eth_string(current_reserve)

def update_circulating_supply():
    current_supply = get_adjusted_total_supply()
    return current_supply

def update_premium_eth():
    premium = get_price() - get_book_per_cat()
    return format_to_eth_string(premium)

def update_premium_percent():
    book = get_book_per_cat()
    premium = get_price() - book
    premium_percent = f"{premium/book * 100:,.2f}%"
    return premium_percent

def update_market_price():
    market_price = get_market_floor()
    return market_price

def fetch_latest_txns_from_api(df):
    txns = []
    max_block_number = df['blockNumber'].max() + 1
    url = parse_normal_transations_url(CATS_CONTRACT, max_block_number, 1)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    data = response.json()
    
    if data["result"] == None or data["result"] == []:
        return None
    
    txns.extend(data["result"])
    txns_df = pd.DataFrame(txns)
    txns_df = txns_df[txns_df["functionName"] == "mint()"][["blockNumber", "timeStamp", "value", "functionName"]].copy()
    txns_df["value"] = pd.to_numeric(txns_df["value"], errors='coerce').fillna(0).astype(int)
    txns_df["blockNumber"] = pd.to_numeric(txns_df["blockNumber"], errors='coerce').fillna(0).astype(int)
    txns_df["value"] = txns_df["value"].apply(to_eth)
    txns_df = txns_df.sort_values("blockNumber", ascending=True)
    return txns_df

# def update_mint_chart():
#     df = pd.read_csv("./historical_mints.csv")
#     new_df = fetch_latest_txns_from_api(df)
#     df = pd.concat([df, new_df], ignore_index=True)
#     df = df.sort_values(by="blockNumber", ascending=True)
#     df = df.reset_index(drop=True)
#     df.to_csv("./historical_mints.csv", index=False)

#     fig = px.line(df, x="blockNumber", y="value")
#     fig.update_layout(
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)"
#     )

#     return fig

def update_mint_chart():
    df = pd.read_sql("SELECT * FROM historical_mints", engine)
    new_df = fetch_latest_txns_from_api(df)
    if new_df is not None:
        df = pd.concat([df, new_df], ignore_index=True)
        df = df.sort_values(by="blockNumber", ascending=True)
        df = df.reset_index(drop=True)
        df.to_sql("historical_mints", engine, if_exists="replace", index=False)

    fig = px.line(df, x="blockNumber", y="value")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig

def register_callbacks(app: Dash) -> None:
    @app.callback(
        [
            Output("book-value-label", "children"),
            Output("quit-royalties-label", "children"),
            Output("mint-price-label", "children"),
            Output("current-reserves-label", "children"),
            Output("circulating-supply-label", "children"),
            Output("premium-eth-label", "children"),
            Output("premium-percent-label", "children"),
            Output("market-price-label", "children"),
            Output("historical-mint-chart", "figure")
        ],
        [Input("combined-interval", "n_intervals")]
    )
    def update_stat_elements(n) -> tuple:
        return (
            update_book_value(),
            update_book_royalties(),
            update_mint_price(),
            update_current_reserves(),
            update_circulating_supply(),
            update_premium_eth(),
            update_premium_percent(),
            update_market_price(),
            update_mint_chart()
        )