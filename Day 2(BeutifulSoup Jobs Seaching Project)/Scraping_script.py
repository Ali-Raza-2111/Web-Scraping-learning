from bs4 import BeautifulSoup
import requests

HTML_Content = requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=").text

soup = BeautifulSoup(HTML_Content,'lxml')


job = soup.find_all('span',class_='srp-comp-name')
title = soup.select('h3 a')
location = soup.find_all('div',class_='srp-loc')

for j , t,l in zip(job,title,location):
    print(f'Job title is {t.text} and company name is {j.text} and location is {l.text}')


