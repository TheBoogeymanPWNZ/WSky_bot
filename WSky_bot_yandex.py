import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новосибирск')

URL = ('https://yandex.ru/pogoda/?lat=55.03019714&lon=82.92043304')
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 
'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='content__main')
    
    weather = []
    for item in items:
        weather.append({
            'title': item.find('h1', class_='title title_level_1 header-title__title').get_text(strip=True),
            't_now': item.find('div', class_='fact__temp-wrap').get_text(strip=True)
        })
    print(weather)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        URL = ('https://yandex.ru/pogoda/?lat=55.03019714&lon=82.92043304')
        HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 
        'accept': '*/*'}
        def get_html(url, params=None):
            r = requests.get(url, headers = HEADERS, params=params)
            return r
        bot.send_message(message.chat.id, 'Погода в Новосибирске:')
        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all(class_='content__main')
    
            weather = []
            for item in items:
                weather.append({
                    "title": item.find('h1', class_='title title_level_1 header-title__title').text,
                    "t_now": item.find('div', class_='fact__temp-wrap').text
                })
            print(weather)
            bot.send_message(message.chat.id, weather)
        def parse():
            html = get_html(URL)
            if html.status_code == 200:
                get_content(html.text)
            else:
                print('Error')

        parse()
bot.polling()
