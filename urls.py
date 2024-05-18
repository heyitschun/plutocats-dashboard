from env_vars import *

def parse_token_url(account_address, token_address):
    url = f"https://api.blastscan.io/api?module=account&action=tokenbalance&contractaddress={token_address}&address={account_address}&tag=latest&apikey={BLASTSCAN_API_KEY}"
    
    return url