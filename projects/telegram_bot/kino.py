import telebot
import requests
from bs4 import BeautifulSoup as BS
import json # чтобы работать с json объектами
import webbrowser # это библиотека взаимодействует с веб сайтами он открывает веб сайты
from telebot import types


res = requests.get(f'https://www.kinopoisk.ru/index.php?kp_query=энн')
soup = BS(res.text, 'lxml')
enn = soup.find('div', class_='search_results')
# print(enn.text)
enn_ = soup.find('div', class_='info').text.strip()
enn_get = 'https://www.kinopoisk.ru/' + enn.find('a', class_='js-serp-metrika').get('data-url').replace('cast/', '')
print(enn_)
print(enn_get)

