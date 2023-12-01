"=========================Parsing. Таск 5========================="
# import requests
# from bs4 import BeautifulSoup as BS

# url = requests.get('https://enter.kg/')
# soup = BS(url.text, 'lxml')

# category = soup.find_all('div', class_='category')
# category_list = []
# category2 = soup.find('ul', class_='VMmenu').find_all('a')
# for i in category2:
#     category_list.append(i.text.strip())
# for i in category:
#     category_list.append(i.find('span', class_='category-product-count').text)

# def find_category(categories, keyword):
#     list_ = []
#     for i in categories:
#         if keyword.lower() in i.lower():
#             list_.append(i.strip())
#     return list_
    

# print(find_category(category_list, 'Ноутбуки')) 



'=======================Задание 4========================'

# import requests
# from bs4 import BeautifulSoup as BS

# def getTitle(url):
#     response = requests.get(url)
#     soup = BS(response.text, 'lxml')
#     div = soup.find('h1')
#     if div:
#         return div
#     else:
#         return  "Title could not be found"
# print(getTitle('http://www.example.com/'))






"======================Parsing. Таск 6============================="
# import requests
# from bs4 import BeautifulSoup as BS

# url = "https://www.imdb.com/chart/top" 
# header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
# # фальшивая информация о себе header
# session = requests.Session()
# response = session.get(url,headers=header)  # тут как раз так и отправляю фальшивую информацию
# soup = BS(response.text, "lxml") 

# title = soup.find_all('a', class_='ipc-title-link-wrapper')
# # print(title)

# # for i in title:
# #     if 'shawshank'.lower() in i.find('h3').text.lower():
# #         print(i.get('href'))
# # проверка на того правильно ли пишу функцию
# def get_link(title_list, name):
#     for i in title_list:
#         if name.lower() in i.find('h3').text.lower():
#             return 'https://www.imdb.com' + i.get('href')

# print(get_link(title, 'pulp') )

# import requests
# from bs4 import BeautifulSoup as BS





"===================Parsing. Таск 2============================="
# import requests 
# from bs4 import BeautifulSoup as BS

# source = requests.get('http://www.example.com/')
# response = BS(source.text, 'lxml')

# print(f'h1: {response.h1.text}')

# print(f'p: {response.p.text}')

# print(f"a: {response.a.get('href')}")