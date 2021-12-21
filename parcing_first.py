from bs4 import BeautifulSoup
# from datetime import datetime
import requests
import re
import itertools
import csv

# парсинг данных со стораницы отзывов
URL = 'https://mooc.ru/company/neural-university/reviews'
page = requests.get(URL)
print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

reviews = (soup.find_all('span', class_='body font-size-14'))
name_reviews = soup.find_all('span', class_='ml-2 font-size-12 color-middlegray')
date_reviews = soup.find_all('span', class_='ml-4 font-size-12 color-middlegray')


# парсинг названия компании
headline = soup.find_all('div', class_= 'col-12 col-md-9')
for hd in headline:
    art = str(hd.text)



# создание списков
all_reviews = []
all_dates = []
all_names = []

#  приведение к строке данных к строке и формирование списка отзывов
for rev in reviews:
    r = str(rev.text)
    all_reviews.append(r)

#  приведение к строке данных к строке и формирование списка дат размещения отзывов
for date in date_reviews:
    d = str(date.text)
    all_dates.append(d)
# print(all_dates)

#  приведение к строке данных к строке и формирование списка авторов
for name in name_reviews:
    n = str(name.text)
    all_names.append(n)
# print(all_names)

g = list(map(list, zip(all_dates, all_names, all_reviews)))
# print(g, type(g))
i = 0
with open('data_reviews.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['ИСТОЧНИК ИНФОРМАЦИИ: ', URL])
    writer.writerow(['ОТЗЫВЫ О КОМПАНИИ: ', art])
    writer.writerow(['ДАТА', 'АВТОР', 'ОТЗЫВ'])
    for item in g:
        writer.writerows([item])
import openpyxl
from string import ascii_uppercase
