from selenium.webdriver.common.by import By
from prettytable import PrettyTable
from openpyxl import Workbook
class BookingReport:
    def __init__(self, driver):
        self.driver = driver
        
    def Return_Hotels_details(self):
        hotels = []
        hotel_cards = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")

        for card in hotel_cards:
            data = {"name": None, "price": None, "score": None}
            try:
                # 1. Hotel name
                title = card.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text.strip()
                data["name"] = title
            except Exception as e:
                print(f"⚠️ Name not found: {e}")

            try:
                # 2. Price — capture discounted or base
                price_elem = card.find_element(By.CSS_SELECTOR, "div[data-testid='price-and-discounted-price'], span[data-testid='price-and-discounted-price']")
                data["price"] = price_elem.text.strip()
            except Exception:
                try:
                    price_elem = card.find_element(By.CSS_SELECTOR, "span.fff1944c52.d68334ea31")
                    data["price"] = price_elem.text.strip()
                except Exception as e:
                    print(f"⚠️ Price not found: {e}")

            try:
                # 3. Score — inside data-testid review-score
                score_elem = card.find_element(By.CSS_SELECTOR, "div[data-testid='review-score'] .f63b14ab7a")
                data["score"] = score_elem.text.strip()
            except Exception as e:
                print(f"⚠️ Score not found: {e}")

            hotels.append(data)

        return hotels

    
    def display_and_save_to_excel(self, data, headers, excel_filename="output.xlsx"):
        # Display in console using PrettyTable
        table = PrettyTable()
        table.field_names = headers

        for row in data:
            row_values = [row.get(header.lower(), "N/A") for header in headers]  # matching keys to headers
            table.add_row(row_values)

        print(table)

        # Write to Excel using openpyxl
        wb = Workbook()
        ws = wb.active
        ws.title = "Data"

        # Write headers
        ws.append(headers)

        # Write data rows
        for row in data:
            row_values = [row.get(header.lower(), "N/A") for header in headers]
            ws.append(row_values)

        wb.save(excel_filename)
        print(f"\n✅ Data saved to {excel_filename}")

