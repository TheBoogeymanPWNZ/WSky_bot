import telebot
import requests
import emoji
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
        for el in soup.select('.fact__temp-wrap'):
            t_now = el.select('.fact__temp_size_s')[0].text
        for el in soup.select('.link__feelings'):
            t_sky = el.select('.link__condition')[0].text
            t_sen = el.select('.fact__feels-like')[0].text
        for el in soup.select('.fact__props'):
            t_wind = el.select('.term_orient_v')[0].text
            t_hum = el.select('.fact__humidity')[0].text
            t_press = el.select('.fact__pressure')[0].text
            t_water = el.select('.fact__water-temp')[0].text
        bot.send_message(message.chat.id, t_now + '🌡️' +
                         '\n' + t_sky +
                         '\n' + t_sen + '🌡️' +
                         '\n' + '🌪️' + t_wind +
                         '\n' + '💧' + t_hum +
                         '\n' + '🩺' + t_press +
                         '\n' + '🌊' + t_water)


bot.polling()
