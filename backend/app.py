import requests
from dotenv import load_dotenv
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()

alchemy_url = os.getenv("ALCHEMY_URL")


# retrieve the live ETH price
def get_eth_price():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids" : "ethereum",
        "vs_currencies" : "eur"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

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

    response = requests.post(alchemy_url, json=payload, timeout=10)

    response.raise_for_status()

    data = response.json()

    balance_hex = data["result"]

    balance_wei = int(balance_hex, 16)

    balance_eth = balance_wei / (10 ** 18)

    return balance_eth


@app.route("/")
def home():
    return "Crypto Wallet Tracker API"

@app.route("/api/wallet/<wallet_address>")
def wallet(wallet_address):

    if not wallet_address.startswith("0x") or len(wallet_address) != 42:

        return {
            "error": "Invalid Ethereum wallet address"
        }

    address_hex = wallet_address[2:]

    try: 
        int(address_hex, 16)

    except ValueError:
        return {
            "error": "Invalid Ethereum wallet address"
        }

    try:
        current_price = get_eth_price()

        eth_balance = get_eth_balance(wallet_address)

        wallet_value = eth_balance * current_price

    except (requests.RequestException, KeyError, ValueError):
        return {
            "error": "Unable to retrieve wallet data"
        }

    return {
        "wallet_address": wallet_address,
        "eth_balance" : eth_balance,
        "wallet_value" : wallet_value,
        "eth_price_eur" : current_price
    }

if __name__ == "__main__":
    app.run()



# OLD TESTING CODE

#wallet_address = "0x80ed97ff038cAe9be7D9132347B9a3128D5f09fC"

#current_price = get_eth_price()

#eth_balance = get_eth_balance(wallet_address)

#wallet_value = eth_balance * current_price

#print(f"Current Ethereum price: €{current_price:.2f}")
#print(f"Current wallet address: {wallet_address}")
#print(f"Current ETH balance: {eth_balance} ETH")
#print(f"Current wallet value: €{wallet_value:.2f}")
