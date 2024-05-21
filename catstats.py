from contracts import contract
from client import client
from helpers import *
from urls import parse_token_url
from constants import *
import requests

def get_sold() -> int:
    sold = contract.functions.totalSupply().call()
    if not isinstance(sold, int):
        return 0
    return sold

def get_adjusted_total_supply() -> int:
    ats = contract.functions.adjustedTotalSupply().call()
    if not isinstance(ats, int):
        return 1
    return ats

def get_current_reserve() -> int:
    reserve = client.eth.get_balance(CATS_RESERVE)
    if not isinstance(reserve, int):
        return 0
    return reserve

def get_book_per_cat() -> float:
    current_reserve = get_current_reserve()
    current_supply = get_adjusted_total_supply()
    book_value_per_cat = current_reserve / current_supply
    return book_value_per_cat

def get_quit_plus_royalties() -> float:
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
            royalties += 0
    total_quit = book + (royalties / current_supply)
    return total_quit

def get_price() -> int:
    price_wei = contract.functions.getPrice().call()
    if not isinstance(price_wei, int):
        return 0
    return price_wei