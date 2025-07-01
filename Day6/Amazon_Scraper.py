from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"


def extract_product_html(url):
    res = requests.get(url,headers={'User-Agent': USER_AGENT})
    return res.content


def extract_product_details(url):
    product_info = {}
    Product_html = extract_product_html(url)
    soup = BeautifulSoup(Product_html,'lxml')
    print(soup)
    
    
if __name__ == "__main__":
    with open('Amazon_product_Urls.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            url = row[0]
            extract_product_details(url)