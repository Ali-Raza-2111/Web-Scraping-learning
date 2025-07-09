from selenium.webdriver.common.by import By
from prettytable import PrettyTable

class BookingReport:
    def __init__(self, driver):
        self.driver = driver
        
    def Return_Hotels_details(self, hotel_boxes):
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

    def report_result(self, hotels):
        table = PrettyTable()

    # Set table columns
        table.field_names = ["No.", "Hotel Name", "Price", "Score"]

        # Add each hotel as a new row
        for i, hotel in enumerate(hotels, start=1):
            table.add_row([i, hotel["name"], hotel["price"], hotel["score"]])

        print(table)
        return hotels
