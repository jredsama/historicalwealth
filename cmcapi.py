import requests
import json
from pprint import pprint

while True:
# URL list
    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
    parameters = {"id": 'ripple', "price_usd": ''}
    request = requests.get(globalURL)
    data = request.json()
    globalMarketCap = data["total_market_cap_usd"]

# UI
    print()
    print("Are you ready for some history with a modern perspective? Let's get digital!")
    print("Cryptocurrency Global Market Cap (Top 10): $" + str(globalMarketCap))
    print("Type 'all' to show the Top 10 or enter the name of the coin")
    print()
    choice = input("Which would you like to view?: ")

    if choice == "all":
        request = requests.get(tickerURL)
        data = request.json()

        for i in data:
            ticker = i["symbol"]
            price = i["price_usd"]

            print(ticker + ":\t\t$" + price)
        print()

    else:
            tickerURL += "/" +choice+"/"
            request = requests.get(tickerURL)
            data = request.json()

            ticker = data[0]["symbol"]
            price = data[0]["price_usd"]

            print(ticker + ":\t\t$" + price)
            print()

    choice2 = input("Would you like to try it again? (yes/no): ")
    if choice2 == "yes":
        continue
    if choice2 == "no":
        break
