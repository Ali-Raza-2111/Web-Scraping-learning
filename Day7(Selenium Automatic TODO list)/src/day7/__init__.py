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
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value = "//a[@href='https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D']").click()
        time.sleep(5)
        Email = DRIVER.find_element(By.CSS_SELECTOR, "input[type='email']")
        time.sleep(2)
        Email.send_keys(credientials['Username'])
        time.sleep(2)
        DRIVER.find_element(By.CSS_SELECTOR, "span[class='css-178ag6o']").click()
        time.sleep(3)
        password = DRIVER.find_element(By.CSS_SELECTOR, "input[id='password']")
        password.send_keys(credientials['Password'])
        time.sleep(2)
        DRIVER.find_element(By.CSS_SELECTOR, "span[class='css-178ag6o']").click()
def main() -> None:
    try:
        DRIVER.get("https://trello.com/")
        login()
        input("BOT operation completed. Press enter to exit.")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()
    

if __name__ == '__main__':
    main()

def main() -> None:
    print("Hello from day7!")

