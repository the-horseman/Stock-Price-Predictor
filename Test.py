import requests
import json

url = "https://yfapi.net/v6/finance/recommendationsbysymbol/TATASTEEL.NS"

# querystring = {"symbols": "AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-api-key': "I8xBy8R9s17Hxd0hJWw31ExfqTV2f1i176OlKFH0"
}

response = requests.request("GET", url, headers=headers)

ex = json.loads(response.text)["finance"]["result"][0]["recommendedSymbols"]
print(ex)
