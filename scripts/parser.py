import requests
from bs4 import BeautifulSoup
import urllib.parse
import json

def advanced_search(dictionary):
#     dictionary = {}
#     dictionary['region'] = input("Введите регион \n")
#     dictionary['city'] = input("Введите город \n")
#     dictionary['street'] = input("Введите улицу \n")
#     dictionary['house'] = input("Введите дом \n")
    q = ' '.join(dictionary.values())
    encode = urllib.parse.urlencode({'query': q}) #кодирую кириллицу в ASCII
    url = 'https://www.reformagkh.ru/search/houses?' + encode
    r = requests.get(url) #Подстановка адреса и последующий парс таблицы
    soup = BeautifulSoup(r.text, 'lxml')
#     try:
    ads = soup.find('td').find_all('a') #если адрес не найден, уходит в начало
#     except AttributeError:
#         print("Проверьте правильность набора адреса\n")
#         advanced_search(dictionary)
    ads = soup.find('td').find_all('a')
    temp = str(ads).split('"') #рассплитил тэг "а"
    url = 'https://www.reformagkh.ru'
    url =  url + temp[1] #подставил ссылку в измененную урл
    return url

def get_main_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    ads = soup.find_all('table', class_ = "col_list") #парсит вообще все таблицы на сайте

    table0_spans = {}
    for index, span in enumerate(ads[0].find_all('span')):
        if index % 2 != 0:
            table0_spans[index] = " ".join(span.text.split())


    table1_spans = {}
    for index, span in enumerate(ads[1].find_all('span')):
        if index % 2 != 0:
            table1_spans[index] = " ".join(span.text.split())


    table2_spans = {}
    for index, span in enumerate(ads[8].find_all('span')):
        if index % 2 != 0:
            table2_spans[index] = " ".join(span.text.split())

    qwe = []
    for i in range(1, 8, 2):
        qwe.append(table0_spans[i])
    for i in range(1, 12, 2):
        qwe.append(table1_spans[i])
    for i in range(1, 4, 2):
        qwe.append(table2_spans[i])
    
    return qwe
