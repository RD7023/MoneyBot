import requests


def get_price(text):
    price_ = text.split('price":"')[1]
    price_ = price_.split('"')[0]
    return price_


def req_prices():
    pair_list = ["USDT_UAH", "BTC_UAH", "BTC_USDT"]
    message = ''
    for pair in pair_list:
        url = 'https://api.exmo.com/v1.1/trades?pair=' + pair
        x = requests.get(url)
        price = get_price(x.text)
        message += pair+": "+price+"\n"
    return message


msg = req_prices()
print(msg)
