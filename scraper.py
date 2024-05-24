import requests
from sessions import fetch
from bs4 import BeautifulSoup
from constants import CATS_CONTRACT, BLAST_CHAIN_ID
from env_vars import RESERVOIR_API_KEY

def get_market_floor() -> str:
    # url = f"https://blast.mintify.xyz/blast/{CATS_CONTRACT}"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")
    # price_element = soup.find("div", class_="current-floor")
    # floor_price = price_element.find("span").text
    # floor_price = round(float(floor_price), 3)
    
    url = f"https://api.reservoir.tools/collections/search/v1?chains={BLAST_CHAIN_ID}&prefix={CATS_CONTRACT}"

    headers = {
        "accept": "*/*",
        "x-api-key": RESERVOIR_API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    floor_price = data["collections"][0]["floorAskPrice"]

    label = str(floor_price) + " ETH"

    return label

