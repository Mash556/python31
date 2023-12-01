import requests
from bs4 import BeautifulSoup as BS
import csv


# Py. Hackathon: Parsing  
# 📌 Данный хакатон нацелен на закрепление темы Parsing и делится на 3 уровня сложности: легкий, средний и тяжелый ⤵️​
"==================================================================================="
# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: лёгкая - 80 баллов)

# for count in range(1, 20): 
#     url = f'https://www.kivano.kg/mobilnye-telefony?page={count}'
#     response = requests.get(url)
#     soup = (BS(response.text, 'lxml'))

#     div = soup.find_all('div', class_='listbox_title oh')
    
#     for a in div:
#         try:
#              name = a.find('strong').text
#         except:
#             name = ''
#         try:
#             href = 'https://www.kivano.kg' + a.find('a').get('href')
#         except:
#             href = ''

#         div_price = soup.find_all('div', class_='listbox_price text-center')

#         for i in div_price:
#             try:
#                 price = i.find('strong').text.strip()
#             except:
#                 price = ''

#             data = {
#                 'name': name,
#                 'price': price,
#                 'href': href
#             }

#             with open('kivano_hackaton.csv', 'a') as csv_file:
#                 names = ['name', 'price', 'href']
#                 writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=names)
#                 writer.writerow(data)
"======================================================================================="


"==================================================================================="
# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя - 90 баллов)


for page in range(1, 2124):
    url = f'https://www.mashina.kg/search/?currency=2&price_from=&price_to=&page={page}'
    response = requests.get(url)
    soup = BS(response.text, 'lxml')


    name_mashinka = soup.find_all('h2', class_='name')
    for name in name_mashinka:
        try:
            name_mashinka = (name.text.strip())
        except:
            name_mashinka = ''


    price_mashinka = soup.find_all('div', class_='block price')
    for price in price_mashinka:
        try:
            price_mashinka = price.find('strong').text.strip()
        except:
            price_mashinka = ''


    img_mashinka = soup.find_all('div', class_='list-item list-label')
    for img in img_mashinka:
        try:
            img_mashinka = (img.find('img', class_='lazy-image-attr').get('src'))
        except:
            img_mashinka = ''
        # print(img_mashinka)


    short_desc_mashinka = soup.find_all('div', class_='list-item list-label')
    for img in short_desc_mashinka:
        try:
            short_desc_mashinka = list(img.find('div', class_='block info-wrapper item-info-wrapper').text.strip().replace('  ', '').replace('\n', ''))
        except:
            short_desc_mashinka = ''
        print(''.join(short_desc_mashinka))



    # dict_ = {
    #     'name': name_mashinka,
    #     'price': price_mashinka,
    #     'img': img_mashinka,
    #     'short': ''.join(short_desc_mashinka)
    # }

    # with open('mashinka_hackaton.csv', 'a') as f:
    #     names = ['name', 'price', 'img', 'short']
    #     writer = csv.DictWriter(f, delimiter='|', fieldnames=names)
    #     writer.writerow(dict_)


        

    


