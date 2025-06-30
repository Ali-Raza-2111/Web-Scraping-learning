from bs4 import BeautifulSoup
import requests

HTML_Content = requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=").text
unfimilar_skills = input("Enter the skills")

soup = BeautifulSoup(HTML_Content,'lxml')

JOBS = soup.find_all('div',class_='srp-listing')
# print(JOBS)
for job in JOBS:
    
    title_tag = job.find('div',class_='srp-job-heading')
    title = title_tag.a.text.strip() if title_tag and title_tag.a else "N/A"
     
    
    location = title_tag.h4.span.text.strip() if title_tag and title_tag.span else "N/A"
    skills_tags = job.find_all('a',class_='srphglt')
    
    link = job.find('a',class_ = 'srp-apply-new')['href']
    skills = [s.text.strip() for s in skills_tags] if skills_tags else ["N/A"]
    if 
    print(title)
    print(location)
    print("Skills:", ', '.join(skills))
    print(f'Apply here: {link}' if link else link)
    print('')





