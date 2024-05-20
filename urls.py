from env_vars import BLASTSCAN_API_KEY

def parse_token_url(account_address, token_address):
    url = f"https://api.blastscan.io/api?module=account&action=tokenbalance&contractaddress={token_address}&address={account_address}&tag=latest&apikey={BLASTSCAN_API_KEY}"
    return url

def parse_normal_transations_url(account_address, start, page, end=99999999):
    url = f"https://api.blastscan.io/api?module=account&action=txlist&address={account_address}&startblock={start}&endblock={end}&page={page}&offset=50&sort=desc&apikey={BLASTSCAN_API_KEY}"
    return url

def parse_event_logs_url(contract_address, from_block, to_block, page):
    url = f"https://api.blastscan.io/api?module=logs&action=getLogs&address={contract_address}&fromBlock={from_block}&toBlock={to_block}&page={page}&offset=10&apikey={BLASTSCAN_API_KEY}"
    return url