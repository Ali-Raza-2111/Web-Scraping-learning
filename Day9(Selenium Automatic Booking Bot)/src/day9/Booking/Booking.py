from selenium import webdriver
import Booking.Constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from Booking.Booking_Filtration import BookingFiltration
from Booking.Booking_report import BookingReport
class Booking(webdriver.Chrome):
    def __init__(self, driver_path = 'chromedriver.exe',TearDown = False):
        self.driver_path = driver_path
        self.TearDown = TearDown
        super(Booking, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.TearDown:
            self.quit()
            
    def dismiss_sign_button(self):
        try:
            self.find_element(By.CSS_SELECTOR,"button[aria-label='Dismiss sign-in info.']").click()
        except:
            pass
        
    
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.CSS_SELECTOR,"input[name='ss']")
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(2)
        first_result = self.find_element(By.CSS_SELECTOR,"li[id='autocomplete-result-0']")
        first_result.click()
    
    
    def select_date(self,check_in_date,check_out_date):
        self.implicitly_wait(10)
        check_in_element = self.find_element(By.CSS_SELECTOR,f"[data-date='{check_in_date}']")
        check_in_element.click()
        
        check_out_element = self.find_element(By.CSS_SELECTOR,f"[data-date='{check_out_date}']")
        check_out_element.click()
        
        
    
    def wait_for_element(self, by, value, condition=EC.presence_of_element_located, timeout=10):
        """Reusable explicit wait for element presence or other conditions"""
        wait = WebDriverWait(self, timeout)
        return wait.until(condition((by, value)))
    
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.dismiss_sign_button()
        
    def select_adults(self,count = 1):
        self.implicitly_wait(10)
        adult_button = self.find_element(By.CSS_SELECTOR,"button[aria-label='Number of travelers and rooms. Currently selected: 2 adults · 0 children · 1 room']")
        adult_button.click()
        decrease_button = self.find_element(By.CSS_SELECTOR, 'button[tabindex="-1"]:not([disabled]) svg path[d="M20.25 12.75H3.75a.75.75 0 0 1 0-1.5h16.5a.75.75 0 0 1 0 1.5"]')
        decrease_button.click()
        
        increase_button = self.find_element(
            By.CSS_SELECTOR, 
            'button[tabindex="-1"]:not([disabled]) svg path[d="M20.25 11.25h-7.5v-7.5a.75.75 0 0 0-1.5 0v7.5h-7.5a.75.75 0 0 0 0 1.5h7.5v7.5a.75.75 0 0 0 1.5 0v-7.5h7.5a.75.75 0 0 0 0-1.5"]')
        
        for _ in range(count-1):
            increase_button.click()
    
    
    def submit_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,"button[type='submit']")
        search_button.click()
        
    def apply_filtrations(self):
        filtration = BookingFiltration(driver = self)
        filtration.select_star_checkbox(star_rating = 5)
        filtration.click_sort_toggle()
        filtration.select_price_sort("Price (lowest first)")
        
    def report_result(self):
        self.implicitly_wait(10)
        lists = self.find_elements(By.CSS_SELECTOR, "div[role='list']")
        hotel_boxes = []
        
        for list_container in lists:
            hotel_boxes.extend(list_container.find_elements(By.CSS_SELECTOR, "div[role='listitem']"))
        
        
        report = BookingReport(driver = self)
        hotel_data = report.Return_Hotels_details()
        headers = ["Name", "Price", "Score"]
        report.display_and_save_to_excel(hotel_data, headers, excel_filename="hotels.xlsx")
        
        