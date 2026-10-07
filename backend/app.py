import requests
from dotenv import load_dotenv
import os


load_dotenv()

alchemy_url = os.getenv("ALCHEMY_URL")


# retrieve the live ETH price
def get_eth_price():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids" : "ethereum",
        "vs_currencies" : "eur"
    }

    response = requests.get(url, params=params)

    data = response.json()

    eth_price = data["ethereum"]["eur"]

    return eth_price


# retrieve balance from an ETH wallet address
def get_eth_balance(wallet_address):

    payload = {
        "jsonrpc": "2.0",
        "method" : "eth_getBalance",
        "params" : [ wallet_address, "latest" ],
        "id" : 1
    }

    response = requests.post(alchemy_url, json=payload)

    data = response.json()

    balance_hex = data["result"]

    balance_wei = int(balance_hex, 16)

    balance_eth = balance_wei / (10 ** 18)

    return balance_eth


wallet_address = "0x80ed97ff038cAe9be7D9132347B9a3128D5f09fC"

current_price = get_eth_price()

eth_balance = get_eth_balance(wallet_address)

wallet_valve = eth_balance * current_price

print(f"Current Ethereum price: €{current_price:.2f}")
print(f"Current wallet address: {wallet_address}")
print(f"Current ETH balance: {eth_balance} ETH")
print(f"Current wallet value: €{wallet_valve:.2f}")
