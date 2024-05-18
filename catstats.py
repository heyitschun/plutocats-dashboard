from contracts import contract, CATS_RESERVE
from client import client
from helpers import *

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

def get_price():
    price_wei = contract.functions.getPrice().call()
    return price_wei

def format_to_eth_string(ether):
    return f"{to_eth(ether)} ETH"