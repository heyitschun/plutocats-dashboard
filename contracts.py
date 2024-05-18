import json
from client import client
from env_vars import *

with open("./PlutocatsTokenABI.json", "r") as f:
    PLUTOCATS_ABI = json.loads(f.read())
    
contract = client.eth.contract(address=CATS_CONTRACT, abi=PLUTOCATS_ABI)