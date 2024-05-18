from web3 import Web3
from client import client

###################
### Conversions ###

def to_eth(wei):
    return round(float(Web3.from_wei(wei, 'ether')),5)


###########################
### Network Information ###

def block_timestamp(): 
    block_number = client.eth.block_number
    block = client.eth.get_block(block_number)
    ts = block.timestamp
    return ts
