from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        
        
    def select_star_checkbox(self, star_rating: int):
        """
        Clicks the label for the given star_rating (2-5), which in turn checks the hidden input.
        """
        wait = WebDriverWait(self.driver, 10)
        try:
            
            container_css = f'div[data-filters-item="class:class={star_rating}"]'
            container = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, container_css)
            ))

            
            label = container.find_element(By.TAG_NAME, "label")

            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
            wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[@for='{ label.get_attribute('for') }']")))
            try:
                label.click()
            except Exception:
                
                self.driver.execute_script("arguments[0].click();", label)

            print(f"{star_rating}-star checkbox is now selected via its label.")

        except Exception as e:
            print(f"Error selecting {star_rating}-star checkbox: {e}")
            
            
    def click_sort_toggle(self):
        """
        Clicks the "Sort by: ..." toggle (the <span class="cd46a6a263"> wrapper).
        """
        wait = WebDriverWait(self.driver, 10)
        try:
            # Locate the span whose text starts with "Sort by:"
            toggle = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(@class,'a9918d47bf') and starts-with(normalize-space(.),'Sort by:')]"
            )))
            toggle.click()
            print("Sort-by toggle clicked.")
        except Exception as e:
            print(f"Error clicking sort-by toggle: {e}")
            
    
    def select_price_sort(self, option_text: str):
        """
        Clicks the price-sort button whose visible text matches `option_text`.
        Examples for option_text:
          - "Price (lowest first)"
          - "Price (highest first)"
          - "Best reviewed & lowest price"
        """
        wait = WebDriverWait(self.driver, 10)
        try:
            # 1) Wait until the button with a span matching the exact text is clickable
            btn = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                f"//button[.//span[normalize-space(text())='{option_text}']]"
            )))

            # 2) Scroll into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", btn
            )

            # 3) Click (with JS fallback)
            try:
                btn.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", btn)

            print(f"Clicked sort option: {option_text}")

        except Exception as e:
            print(f"Error clicking sort option “{option_text}”: {e}")