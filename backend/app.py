import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids" : "ethereum",
    "vs_currencies" : "eur"
}

response = requests.get(url, params=params)

data = response.json()

eth_price = data["ethereum"]["eur"]
print(eth_price)