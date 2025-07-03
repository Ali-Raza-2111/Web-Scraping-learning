import time
import os
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date

DRIVER_PATH = "chromedriver.exe"
OP = webdriver.ChromeOptions()
OP.add_argument('headless')
DRIVER = webdriver.Chrome()

def login():
    with open('config.json') as config_file:
        credientials = json.load(config_file)
   
def main() -> None:
    try:
        DRIVER.get("https://trello.com/")
        input("BOT operation completed. Press enter to exit.")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()
    

if __name__ == '__main__':
    main()