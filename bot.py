import telebot
from time import sleep
from exmo_requests import req_prices
from c2c_binance import c2c_price
from binance_requests import binance_market


bot = telebot.TeleBot('1217393493:AAHDAWBWWAl322CVqA69RZvCHnGDUGGVLEY')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/start')

freq = 30

@bot.message_handler(commands=['start'])
def start_message(message):
    while True:
        send_msg = req_prices()
        bot.send_message(message.chat.id, send_msg, reply_markup=keyboard1)
        send_msg = c2c_price()
        bot.send_message(message.chat.id, send_msg, reply_markup=keyboard1)
        send_msg = binance_market()
        bot.send_message(message.chat.id, send_msg, reply_markup=keyboard1)
        sleep(freq)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, "Привіт, творець")
    elif message.text.lower() == 'бувай':
        bot.send_message(message.chat.id, 'Бувай творець')
    else:
        bot.send_message(message.chat.id, 'Я ще занадто тупий, почекайте трохи')


bot.polling()
