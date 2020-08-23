import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новосибирск')

URL = ('https://yandex.ru/pogoda/?lat=55.03019714&lon=82.92043304')
page = requests.get(URL).content
soup = BeautifulSoup(page, 'html.parser')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        for el in soup.select('.fact__temp'):
            t_now = el.select('.temp__value')[0].text
        for el in soup.select('.link__feelings'):
            t_sky = el.select('.link__condition')[0].text
            t_sen = el.select('.term__label')[0].text
            t_now_sen = el.select('.temp__value')[0].text
        bot.send_message(message.chat.id,  'Текущая температура: ' + t_now + ' ' + t_sky + 
            '\n' + t_sen + ': ' + t_now_sen)

bot.polling()
