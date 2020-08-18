import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

@bot.message_handler(commands=['start'])                              
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        bot.send_message(message.chat.id, 'Погода в Новосибирске: ')

bot.polling()