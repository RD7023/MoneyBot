import requests


def binance_market():
    url = 'https://api.binance.com//api/v3/ticker/bookTicker?symbol=USDTUAH'
    x = requests.get(url)
    price = x.text.split('"askPrice":"')[1].split('","askQty"')[0]
    message = "BINANCE MARKET: " + price
    return message


print(binance_market())
