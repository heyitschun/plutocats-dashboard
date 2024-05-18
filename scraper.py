import requests
from bs4 import BeautifulSoup

from contracts import *

def get_market_floor():
    url = f"https://blast.mintify.xyz/blast/{CATS_CONTRACT}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.find("div", class_="current-floor")
    floor_price = price_element.find("span").text

    return floor_price + " ETH"

