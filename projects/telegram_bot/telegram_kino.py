import telebot
import requests
from bs4 import BeautifulSoup as BS
import json # чтобы работать с json объектами
import webbrowser # это библиотека взаимодействует с веб сайтами он открывает веб сайты
from telebot import types 
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

bot = telebot.TeleBot('6746732884:AAF0JuOOQAgeRjDNs6mstjp9sCRlQCdhMz0')

"================Кинопоиск=================="

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет введи название фильма,дорамы или кино')

@bot.message_handler(content_types=['text'])
def get_kino(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://www.kinopoisk.ru/index.php?kp_query={city}', headers=header)
    try:
        if res.status_code == 200:
            soup = BS(res.text, 'lxml')
            enn = soup.find('div', class_='search_results')
            enn_ = soup.find('div', class_='info').text.strip()
            enn_get = 'https://www.kinopoisk.ru/' + enn.find('a', class_='js-serp-metrika').get('data-url').replace('cast/', '')
            bot.reply_to(message, f'{enn_} \n {enn_get}')
        else:
            bot.reply_to(message, 'Введите корректное название фильма')
    except Exception as a:
        bot.reply_to(message, 'К сожелению ничего не найдено')


bot.polling(non_stop=True)

