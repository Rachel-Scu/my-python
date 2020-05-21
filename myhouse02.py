from urllib import request
from urllib import error
import socket
from bs4 import BeautifulSoup as bs

url = 'https://cd.ixiangzhu.com/house/index.html?page=1'

try:
    resp = request.urlopen(url)
    html_data = resp.read().decode('utf-8')
except error.URLError as ex:
    html_data = None
except socket.timeout as ex:
    html_data = None

if html_data:
    #print(html_data)

    soup = bs(html_data, 'html.parser')

    house_div = soup.find_all('div', class_='house-items')
    #print(house_div)


    house_list_a = house_div[0].find_all('a')    
    #print(house_list_a)

    house_list=[]

    for ahref in house_list_a:
        if ahref.string:
            house_list.append(ahref.string)
        

    #print(house_list)

    price_list = house_div[0].find_all('div', class_='house-price')
    print(price_list)


    for (houseName, husePrice) in zip(house_list, price_list):
        print(houseName)
        print(husePrice.span.string)