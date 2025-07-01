from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":
    with open('Amazon_product_Urls.csv',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            url = row[0]
            print(url)