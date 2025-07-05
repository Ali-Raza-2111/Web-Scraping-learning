from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
DRIVER_PATH = "chromedriver.exe"
OP = webdriver.ChromeOptions()
OP.add_argument('headless')
DRIVER = webdriver.Chrome()
DRIVER.get("https://automationintesting.com/selenium/testpage/?colour=Red")

def screenshot():
    DRIVER.save_screenshot("screenshot.png")
def Adding_info():
    DRIVER.implicitly_wait(10)
    first_Name = DRIVER.find_element(By.ID, "firstname")
    sur_Name = DRIVER.find_element(By.ID, "surname")
    first_Name.send_keys("Ali Raza")
    sur_Name.send_keys("Khadim Hussain")
    gender_dropDown = Select(DRIVER.find_element(By.ID, "gender"))
    gender_dropDown.select_by_value("male")
    
    blue_radio_button = DRIVER.find_element(By.ID, "blue")
    blue_radio_button.click()
    text_Area = DRIVER.find_element(By.XPATH, "//textarea[@placeholder='Tell us some fun stuff!']")
    text_Area.send_keys("I just built my first Selenium automation script and it works perfectly! Loving how easy it is to fill out forms and interact with web elements programmatically.")
    
    
    Region_DropDown = Select(DRIVER.find_element(By.ID, "continent"))
    Region_DropDown.select_by_value("asia")
    
    
    email_checkbox = DRIVER.find_element(By.ID, "checkbox1")
    email_checkbox.click()
    sms_checkbox = DRIVER.find_element(By.ID, "checkbox2")
    sms_checkbox.click()
    
    
def main() -> None:
    print("Hello from day8!")
    Adding_info()
    screenshot()
    input("Press Enter to exit")
if __name__ == '__main__':
    main()