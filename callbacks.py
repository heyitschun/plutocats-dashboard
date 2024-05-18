from dash.dependencies import Input, Output
from catstats import *
from scraper import *

def update_book_value():
    book_value = get_book_per_cat()
    return format_to_eth_string(book_value)

def update_book_royalties():
    quit_plus = get_quit_plus_royalties()
    return format_to_eth_string(quit_plus)

def update_mint_price():
    price_wei = get_price()
    return format_to_eth_string(price_wei)

def update_current_reserves():
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
    premium_percent = f"{premium/book * 100:.2f}%"
    return premium_percent

def update_market_price():
    market_price = get_market_floor()
    return market_price

def register_callbacks(app):
    
    @app.callback(
        [
            Output("book-value-label", "children"),
            Output("quit-royalties-label", "children"),
            Output("mint-price-label", "children"),
            Output("current-reserves-label", "children"),
            Output("circulating-supply-label", "children"),
            Output("premium-eth-label", "children"),
            Output("premium-percent-label", "children"),
            Output("market-price-label", "children")
        ],
        [Input("combined-interval", "n_intervals")]
    )
    def update_stat_elements(n):
        return (
            update_book_value(),
            update_book_royalties(),
            update_mint_price(),
            update_current_reserves(),
            update_circulating_supply(),
            update_premium_eth(),
            update_premium_percent(),
            update_market_price()
        )