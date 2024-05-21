import json
from client import client
from constants import CATS_CONTRACT
from web3.contract.contract import Contract

with open("./PlutocatsTokenABI.json", "r") as f:
    PLUTOCATS_ABI = json.loads(f.read())
    
contract: Contract = client.eth.contract(address=CATS_CONTRACT, abi=PLUTOCATS_ABI)