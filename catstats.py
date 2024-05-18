from contracts import contract
from client import client
from helpers import *
from urls import parse_token_url
from env_vars import *
import requests

def get_sold():
    sold = contract.functions.totalSupply().call()
    return sold

def get_adjusted_total_supply():
    return contract.functions.adjustedTotalSupply().call()

def get_current_reserve():
    return client.eth.get_balance(CATS_RESERVE)

def get_book_per_cat():
    current_reserve = get_current_reserve()
    current_supply = get_adjusted_total_supply()
    book_value_per_cat = current_reserve / current_supply
    return book_value_per_cat

def get_quit_plus_royalties():
    tokens = [BLURETH_CONTRACT, WETH_CONTRACT]
    book = get_book_per_cat()
    current_supply = get_adjusted_total_supply()
    royalties = 0
    for token in tokens:
        try:
            u = parse_token_url(CATS_RESERVE, token)
            response = requests.get(u)
            response.raise_for_status()
            data = response.json()
            if data.get("status") == "1" and "result" in data:
                royalties += int(data["result"])
            else:
                pass
        except:
            pass
    total_quit = book + (royalties / current_supply)
    return total_quit

def get_price():
    price_wei = contract.functions.getPrice().call()
    return price_wei

def format_to_eth_string(ether):
    return f"{to_eth(ether)} ETH"