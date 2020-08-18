import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новосибирск')

url = ('https://sinoptik.ua/погода-новосибирск')
page = requests.get(url).content
soup = BeautifulSoup(page, 'html.parser')

@bot.message_handler(commands = ['start'])                              
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ", reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        bot.send_message(message.chat.id, 'Погода в Новосибирске:')
        for el in soup.select('#bd1c'):
            t_now = el.select('.tabsContent .today-temp')[0].text
        bot.send_message(message.chat.id, t_now)
        for el in soup.select('#bd1'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
        bot.send_message(message.chat.id, t_min)
        bot.send_message(message.chat.id, t_max)
            
bot.polling()