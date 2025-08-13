from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import smtplib
service = Service(executable_path="./chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
DRIVER = webdriver.Chrome(service=service,options = chrome_options)
def login():
    DRIVER.get('https://news.ycombinator.com/news')
    
def extracting_News():
    headLine = []
    Head_Lines = DRIVER.find_elements(By.XPATH,'//span[@class="titleline"]/a')
    for i, headline in enumerate(Head_Lines):
        headLine.append(str(i+1) + ". " + headline.text+"\n"+headline.get_attribute('href'))
    
    return headLine       
    
def sending_email(headline):
    with open("config.json") as f:
        config = json.load(f)
        
    my_email = config["email"]
    my_password = config["password"]
    
    msg = "Subject: New Headlines\n\n"
    msg += "Here are the latest news headlines:\n\n"

    for i, news in enumerate(headline, start=1):
        msg += f"{news}\n\n"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="receivergmail.com",
                msg=msg.encode("utf-8")
            )
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
    
if __name__ == "__main__":
    login()
    headline = extracting_News()
    sending_email(headline)
    