from web3 import Web3

client = Web3(Web3.HTTPProvider("https://rpc.blast.io"))
assert client.is_connected(), "Failed to connect to Blast"