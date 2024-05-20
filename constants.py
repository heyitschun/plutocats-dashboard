ALLOWED_TYPES_NUM = ("number")
ALLOWED_TYPES_DATE = ("text")

DELAY = 10000

BLAST_RPC_URLS = [
    "https://rpc.blast.io",
    "https://rpc.ankr.com/blast",
    "https://blastl2-mainnet.public.blastapi.io",
    "https://blast.din.dev/rpc",
    "https://blast.blockpi.network/v1/rpc/public"
]

START_BLOCK = 817948
START_TIME = 1710445629

METHOD_IDS = {
    "0x70bce2d6": "takeAskSingle",
    "0xda815cb5": "takeBidSingle",
    "0x3925c3c3": "takeAsk",
    "0x7034d120": "takeBid"
}

CATS_CONTRACT = "0xF084962cdC640ED5c7d4e35E52929dAC06B60F7C"
CATS_RESERVE = "0x4eA682B94B7e13894C3d0b9afEbFbDd38CdACc3C"
BLURETH_CONTRACT = "0xB772d5C5F4A2Eef67dfbc89AA658D2711341b8E5"
WETH_CONTRACT = "0x4300000000000000000000000000000000000004"