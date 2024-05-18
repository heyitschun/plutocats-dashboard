import os
from dotenv import load_dotenv

if os.getenv('FLASK_ENV') == 'development':
    from dotenv import load_dotenv
    load_dotenv()

CATS_CONTRACT = os.getenv("CATS_CONTRACT")
CATS_RESERVE = os.getenv("CATS_RESERVE")
BLASTSCAN_API_KEY = os.getenv("BLASTSCAN_API_KEY")
BLURETH_CONTRACT = os.getenv("BLURETH_CONTRACT")
WETH_CONTRACT = os.getenv("WETH_CONTRACT")