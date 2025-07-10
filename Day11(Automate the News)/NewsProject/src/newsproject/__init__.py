from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
website = 'https://www.thesun.co.uk/news/worldnews/'
path = './chromedriver.exe'
Service = Service(executable_path=path)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
DRIVER = webdriver.Chrome(service=Service,options=options)
DRIVER.get(website)
DRIVER.implicitly_wait(10)
containers = DRIVER.find_elements(By.XPATH,value='//div[@class = "teaser__copy-container"]')
titles = []
Subtitiles = []
Links =[]

for container in containers:
    Title = container.find_element(By.XPATH,value='./a/span').text
    Subtitile = container.find_element(By.XPATH,value='./a/h3').text
    
    Link = container.find_element(By.XPATH,value='./a').get_attribute('href')
    
    titles.append(Title)
    Subtitiles.append(Subtitile)
    Links.append(Link)


pd.DataFrame({
    'Title':titles,
    'Subtitile':Subtitiles,
    'Link':Links
}).to_csv('news.csv',index=False)

DRIVER.quit()

