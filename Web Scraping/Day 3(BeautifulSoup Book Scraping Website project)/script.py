from bs4 import  BeautifulSoup
import requests

response = requests.get('https://books.toscrape.com/')
response.encoding = 'utf-8' 
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')


li = soup.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
for l in li:
    title = l.find('h3').a['title']
    price = l.find('p',class_ = 'price_color').text
    print(f'title is {title} and price is {price}')


