import requests
from bs4 import BeautifulSoup


def c2c_price():
    url = 'https://c2c.binance.com/ua/trade/sell/USDT'
    x = requests.get(url, cookies={"common_fiat":"UAH"})
    soup = BeautifulSoup(x.content, 'html.parser')
    results = soup.find_all(class_='css-1m1f8hn')
    price = str(results[0]).split(">")[1].split("</")[0]
    message = "C2С BINANCE USDT_UAH: " + price
    return message


print(c2c_price())