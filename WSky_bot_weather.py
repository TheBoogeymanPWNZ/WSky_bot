import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новосибирск')

URL = ('https://weather.com/ru-RU/weather/today/l/49e03742ba04a23306057562ca075f4f84cdad1af49f8f0729b4c0bbccfa1eaa')
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 
'accept': '*/*'}
page = requests.get(URL).content
soup = BeautifulSoup(page, 'html.parser')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        bot.send_message(message.chat.id, 'Погода в Новосибирске:')
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--hero--2QGgO'):
            t_now = el.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt')[0].text
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_max_min = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[0].text  
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_wind = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[1].text         
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_hum = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[2].text       
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_dew = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[3].text  
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_pres = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[4].text
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_violet = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[5].text
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_visib = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[6].text    
        for el in soup.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_moon = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[7].text 
        bot.send_message(message.chat.id, 'Сейчас ' +  t_now + 
        '\n' + 'Макс./Мин.:  ' + t_max_min + '\n' + 'Ветер:  ' + t_wind + 
        '\n' + 'Влажность:  ' + t_hum + '\n' + 'Точка росы:  ' + t_dew +
        '\n' + 'Давление:  ' + t_pres + '\n' + 'Индекс УФ:  ' + t_violet +
        '\n' + 'Видимость:  ' + t_visib + '\n' + 'Фаза луны:  ' + t_moon)

bot.polling()
