from web3 import Web3
from web3.types import Timestamp, BlockData
from client import client

###################
### Conversions ###

def to_eth(wei):
    return round(float(Web3.from_wei(wei, 'ether')),5)


###########################
### Network Information ###

def block_timestamp(): 
    block_number = client.eth.block_number
    block: BlockData = client.eth.get_block(block_number)
    ts: Timestamp = block.timestamp
    return ts

##############
### Format ###

def format_to_eth_string(ether):
    return f"{to_eth(ether):,.3f} ETH"