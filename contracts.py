import json
import os
from dotenv import load_dotenv
from client import client

if os.getenv('FLASK_ENV') == 'development':
    from dotenv import load_dotenv
    load_dotenv()

CATS_CONTRACT = os.getenv("CATS_CONTRACT")
CATS_RESERVE = os.getenv("CATS_RESERVE")
BLASTSCAN_API_KEY = os.getenv("BLASTSCAN_API_KEY")

with open("./PlutocatsTokenABI.json", "r") as f:
    PLUTOCATS_ABI = json.loads(f.read())
    
contract = client.eth.contract(address=CATS_CONTRACT, abi=PLUTOCATS_ABI)