import requests
from bs4 import BeautifulSoup as BS
import csv
from time import sleep
# from time import sleep - стоит импортировать в дальнейшем эту модуль потому что при использовании нашей методики процесс проходит очень быстро и сайты просто могут заблокировать нас
# requests - это такой модуль который позволяет нам брать данные из какого то сайта и т.д
# enterkg = requests.get('https://enter.kg/computers/noutbuki_bishkek').text


# бывает что сайты нас заблокируют ведь когда мы отправляем запрос им собщается что это разработчик или бот и т.д 
# а это не к добру им но есть когда мы отправляем запрос можем передать через праметр headers='' фальшивые данные чтобы 
headers = {'UserAgent':'Mozilla/0.5'}
# бывает что в сайте несколько страниц и мы можем сами легко посмотреть сколько там страниц 
# для этого нужен цикл можем сделать столько цифр сколько страниц и ниже использовали f строку для того чтобы получить вот эти значение со всех страниц
for count in range(1, 7):

    # sleep(3) # чмсло внутри sleep передается в секундах
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'  # тут будет храниться просто обычная ссылка тоесть мы его сохранили в переменной url

    response = requests.get(url, headers=headers)  # тут мы отправили запрос странице url но этим нельзя работать потому чту его нельзя перебрать по тегам и т.д тут каша не сваренная

    soup = BS(response.text, 'lxml')  # тут мы уже можем пройтись циклом или же просто с помощью методов перебрать какие то теги
# .find - возювращает первый совпавпавший тег и возвращает тип данных строка
# data = soup.find('div', class_='w-full rounded border') # этот код вернет нам первый попавший тег с таким классом тоесть метод .find - возвращает первый совпадающий элемент 
# print(data)

# name = data.find('h4').text.replace('\n', '') # этот код вернет текст внутри тега h4 text - это атрибут который читает текст и его же возвращает в виде строки (после приминение этого метода останется \n сверхи и снизу его сразу нужно обработать)
# print(name)
# price = data.find('h5').text.replace('\n', '') # этот код вернет цену товара (\n будет присутствовать только в том случае если тег состоит из нескольких строк)
# print(price)

# .get = позволяет  получить содержимый атрибут 
# когда мы получаем атрибут или переменную а точнее ссылку он недает нам полный ответ, чтобы получить к ней доступ мы должны прописать корневой адрес с https до com как показано снизу
# img_ = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
# print(img_)




# .find_all = возвращает все совпадающие теги и он вовращет тип данных список
# после метода .find_all необходимо пройтись поциклу если необходимо перебрать внутренние теги атрибуты и т.д
    data1 = soup.find_all('div', class_='w-full rounded border')
# print(data1)
    for i in data1:
        name1 = i.find('h4').text.replace('\n', '')
        price1 = i.find('h5').text.replace('\n', '')
        img_1 = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
        # print(name1+'\n'+price1 +'\n'+ img_1 +'\n')


"=== Итак с верху мы запалучили с главной страницы название, цену и сылку на картинку совсех страниц==="


header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
def get_url():
    for count in range(1, 7):

        sleep(1)
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}' 

        response = requests.get(url, headers=headers) 

        soup = BS(response.text, 'lxml')

        data1 = soup.find_all('div', class_='w-full rounded border')

        for i in data1:
            # так как внутри data1 есть и другие теги и сылка чтобы перейти по этой странице  то нам необходимо заполучить именно эту сылку и не забываем добавить сюда корень
            card_url = "https://scrapingclub.com" + i.find('a').get('href')
            # print(card_url)
            # здесь все это добавляем в список чтобы потом работать легче проходясь по циклу и т.д
            yield card_url

# уже переходим по каждой страничке нашего сайта

def array():
    for card_url in get_url():
        # проделываем такой же путь как и в начале но уже с каждой страницой
        response = requests.get(card_url, headers=headers) 

        soup = BS(response.text, 'lxml')
        # будем использовать метод .find() потому что внутри каждой карточки нетак уж и много
        data1 = soup.find('div', class_='my-8 w-full rounded border')
        # print(data1)
        name = data1.find('h3', class_='card-title').text.replace('\n', '')
        # print(name)
        price = data1.find('h4', class_='my-4 card-price').text
        # print(price)
        text = data1.find('p', class_='card-description').text
        # print(text)
        url_img = "https://scrapingclub.com" + data1.find('img', class_='card-img-top').get("src")
        # print(url_img)

        dict_ = {
            'name':name,
            'price': price, 
            'text':text,
            'url_img': url_img
        }


        with open('main_p.csv', 'a') as csv_file:
            names = ['name', 'price', 'text', 'url_img']
            writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=names)
            writer.writerow(dict_)



"=== На верху мы зашли к каждой странице и спарсили необходимые данные====="





        















