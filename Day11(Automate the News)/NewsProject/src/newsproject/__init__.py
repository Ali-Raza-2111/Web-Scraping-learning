from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import os
import sys

<<<<<<< HEAD

=======
>>>>>>> 2cd670202ba26f2861e037a853b77aca47e8b02c
application_path =os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m %d %Y")

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
fileName = f'News-Headline{month_day_year}.csv'
final_path = os.path.join(application_path,fileName)
pd.DataFrame({
    'Title':titles,
    'Subtitile':Subtitiles,
    'Link':Links
}).to_csv(final_path,index=False)
<<<<<<< HEAD
=======

DRIVER.quit()
>>>>>>> 2cd670202ba26f2861e037a853b77aca47e8b02c

DRIVER.quit()