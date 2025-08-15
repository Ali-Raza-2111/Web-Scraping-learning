import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from prettytable import PrettyTable
from openpyxl import Workbook
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")


DRIVER = uc.Chrome(driver_executable_path='./chromedriver.exe',options=options)

def login():
    DRIVER.get('https://www.udemy.com/')
    time.sleep(2)
def finding_Search():
    DRIVER.implicitly_wait(10)
    course_title = input("Enter the course title: ")
    
    try:
        search_button =DRIVER.find_element(By.XPATH,"//button[@data-css-toggle-id='header-toggle-search-bar']")
        search_button.click()
        time.sleep(2)
        search_bar = DRIVER.find_element(By.XPATH,"//input[@data-testid='search-input']")
        search_bar.send_keys(course_title)
        time.sleep(1)
        submit = DRIVER.find_element(By.XPATH,"//button[@type = 'submit']")
        submit.click()
        time.sleep(2)
    except:
        DRIVER.find_element(By.XPATH,"//form[contains(@class, 'ud-search-form-autocomplete-input-group') and contains(@class, 'ud-search-form-autocomplete-input-group-reversed')]/input[@data-testid='search-input']").send_keys(course_title)
        time.sleep(1)
        submit = DRIVER.find_element(By.XPATH,"//form[contains(@class, 'ud-search-form-autocomplete-input-group') and contains(@class, 'ud-search-form-autocomplete-input-group-reversed')]/button[@type = 'submit']")
        submit.click()
        time.sleep(2)
        
    
def Extracting_data():
    DRIVER.implicitly_wait(3)
    course_info = []
    Boxes = DRIVER.find_elements(By.XPATH,"//div[@class = 'content-grid-item-module--item--MDYzd course-list--margin-bottom--fyWuF']")
    for box in Boxes:
        try:
            title = box.find_element(By.XPATH,".//div[@class = 'card-title-module--clipped--DPJnT']").text
        except:
            title = None
        try:
            description = box.find_element(By.XPATH,".//div[@class = 'ud-text-md card-description-module--description--5tzNB']/span").text
        except:
            description = None
        try:
            instructor = box.find_element(By.XPATH,".//span[@data-testid='safely-set-inner-html:course-card:visible-instructors']").text
        except:
            instructor = None
            
        course = {'title':title,'description':description,'instructor':instructor}
        course_info.append(course)
    return course_info
    
def display_data_pretty(course_info):
    table = PrettyTable()

    # Define column headers
    table.field_names = ["Title", "Description", "Instructor"]

    # Add rows
    for course in course_info:
        table.add_row([course['title'], course['description'], course['instructor']])

    # Optional: Align columns (left align)
    table.align["Title"] = "l"
    table.align["Description"] = "l"
    table.align["Instructor"] = "l"

    print(table)

def save_data_to_excel(course_info, filename="courses.xlsx"):
    # Create a workbook and select active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Courses"

    # Write the header row
    headers = ["Title", "Description", "Instructor"]
    ws.append(headers)

    # Write the course data
    for course in course_info:
        ws.append([course['title'], course['description'], course['instructor']])

    # Save the workbook
    wb.save(filename)
    print(f"Data successfully saved to {filename}")
    
if __name__ == '__main__':
    courses_info = []
    while True:
        print("\n📚 Udemy Course Scraper 📚")
        print("1.Scrape new Courses")
        print("2.View data in tables")
        print("3.Export data to Excel")
        print("4.Exit")
        
        choice = input("Enter your choice:(1-4) ")
        if choice == '1':
            login()
            finding_Search()
            courses_info = Extracting_data()
        elif choice == '2':
            display_data_pretty(courses_info)
        elif choice == '3':
            save_data_to_excel(courses_info)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
    

