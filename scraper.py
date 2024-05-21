import requests
from bs4 import BeautifulSoup
from constants import CATS_CONTRACT

def get_market_floor() -> str:
    url = f"https://blast.mintify.xyz/blast/{CATS_CONTRACT}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_element = soup.find("div", class_="current-floor")
    floor_price = price_element.find("span").text
    floor_price = round(float(floor_price), 3)
    label = str(floor_price) + " ETH"

    return label

