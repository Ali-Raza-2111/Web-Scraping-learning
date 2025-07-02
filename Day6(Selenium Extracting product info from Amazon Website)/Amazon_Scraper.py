# from datetime import datetime
# import requests
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import csv

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"


# def extract_product_html(url):
#     res = requests.get(url,headers={'User-Agent': USER_AGENT})
#     return res.content



        
# def extract_price_info(soup):
#     price = soup.find('span',class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
#     print(price)

# def extract_product_details(url):
#     product_info = {}
#     Product_html = extract_rendered_html(url)
#     soup = BeautifulSoup(Product_html,'lxml')
#     print(soup.prettify())

    
# if __name__ == "__main__":
#     with open('Amazon_product_Urls.csv',newline='') as csvfile:
#         reader = csv.reader(csvfile,delimiter=',')
#         for row in reader:
#             url = row[0]
#             extract_product_details(url)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def extract_rendered_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")

    service = Service()  # if chromedriver is in PATH; else provide executable_path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)  # wait for JS to render content
        rendered_html = driver.page_source
        return rendered_html
    finally:
        driver.quit()


def extract_price_info_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")

    service = Service()  # assumes chromedriver is in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)  # give JS content time to load

        try:
            # Look for span with class a-price-whole
            price_whole = driver.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text

            # Optional: try to get fractional part if available
            try:
                price_fraction = driver.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text
                full_price = f"{price_whole}.{price_fraction}"
            except NoSuchElementException:
                full_price = price_whole

        except NoSuchElementException:
            full_price = "Price not found"

        return full_price
        

    finally:
        driver.quit()
        
def extract_product_title_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")

    service = Service()  # assumes chromedriver is in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)  # let content load

        try:
            title_element = driver.find_element(By.ID, 'productTitle')
            product_title = title_element.text.strip()
        except NoSuchElementException:
            product_title = "Title not found"

        return product_title

    finally:
        driver.quit()
        
        
if __name__ == "__main__":
    import csv

    with open('Amazon_product_Urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            product_info = {}
            product_info['price']   = extract_price_info_selenium(url)
            product_info['Title']  = extract_product_title_selenium(url)
            print(product_info)