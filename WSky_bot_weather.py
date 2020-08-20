import telebot
import requests
import emoji
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1166518757:AAHpKdLanplZO0Ueec6Er3L9bSLjL1Wuvwc')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новосибирск', 'Погода на 7 дней')

URL_NOW = ('https://weather.com/ru-RU/weather/today/l/49e03742ba04a23306057562ca075f4f84cdad1af49f8f0729b4c0bbccfa1eaa')
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
'accept': '*/*'}
CLOUD = emoji.emojize(' :cloud_with_rain: ')
page_now = requests.get(URL_NOW).content
soup_now = BeautifulSoup(page_now, 'html.parser')
URL_10 = ('https://weather.com/ru-RU/weather/tenday/l/49e03742ba04a23306057562ca075f4f84cdad1af49f8f0729b4c0bbccfa1eaa#detailIndex5')
page_10 = requests.get(URL_10).content
soup_10 = BeautifulSoup(page_10, 'html.parser')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, выбери город: ", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Новосибирск':
        for el in soup_now.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--hero--2QGgO'):
            t_now = el.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2icPt')[0].text
        for el in soup_now.select('._-_-components-src-organism-TodayDetailsCard-TodayDetailsCard--detailsContainer--2yLtL'):
            t_max_min = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[0].text
            t_wind = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[1].text
            t_hum = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[2].text
            t_dew = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[3].text
            t_pres = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[4].text
            t_violet = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[5].text
            t_visib = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[6].text
            t_moon = el.select('._-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q')[7].text
        bot.send_message(message.chat.id, 'Сейчас ' +  t_now +
        '\n' + 'Макс./Мин.:  ' + t_max_min + '\n' + 'Ветер:  ' + t_wind +
        '\n' + 'Влажность:  ' + t_hum + '\n' + 'Точка росы:  ' + t_dew +
        '\n' + 'Давление:  ' + t_pres + '\n' + 'Индекс УФ:  ' + t_violet +
        '\n' + 'Видимость:  ' + t_visib + '\n' + 'Фаза луны:  ' + t_moon)
    if message.text == 'Погода на 7 дней':
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[0].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[0].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[0].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[0].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[1].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[1].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[1].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[2].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[1].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[4].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[2].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[2].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[4].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[2].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[7].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[3].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[3].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[6].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[3].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[10].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[4].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[4].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[8].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[4].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[13].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[5].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[5].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[10].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[5].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[16].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
        for el in soup_10.select('._-_-components-src-organism-DailyForecast-DailyForecast--DisclosureList--nosQS'):
            t_tod = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--daypartName--kbngc')[6].text
            t_temp = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp')[6].text
            t_sky = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--extendedData--307Ax')[12].text
            t_rain = el.select('._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--precip--1a98O')[6].text
            t_wind = el.select('._-_-components-src-atom-WeatherData-Wind-Wind--windWrapper--3Ly7c')[19].text
            bot.send_message(message.chat.id, t_tod + ' Темп:' + t_temp + ' ' + t_sky + CLOUD + t_rain + ' ' + t_wind)
bot.polling()
