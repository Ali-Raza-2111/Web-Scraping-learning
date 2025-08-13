from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

# Fetch page content
response = requests.get('https://books.toscrape.com/')
response.encoding = 'utf-8'
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')

# Extract data
data = []
li = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for l in li:
    title = l.find('h3').a['title']
    price = l.find('p', class_='price_color').text
    data.append({'Title': title, 'Price': price})

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Books Data"

# Add header
ws.append(['Title', 'Price'])

# Add data rows
for item in data:
    ws.append([item['Title'], item['Price']])

# Save file
wb.save('books_data.xlsx')


