import json
from web3 import Web3
from dotenv import dotenv_values
from client import client

config = dotenv_values(".env")

CATS_CONTRACT = config["CATS_CONTRACT"]
CATS_RESERVE = config["CATS_RESERVE"]
BLASTSCAN_API_KEY = config["BLASTSCAN_API_KEY"]

with open("./PlutocatsTokenABI.json", "r") as f:
    PLUTOCATS_ABI = json.loads(f.read())
    
contract = client.eth.contract(address=CATS_CONTRACT, abi=PLUTOCATS_ABI)