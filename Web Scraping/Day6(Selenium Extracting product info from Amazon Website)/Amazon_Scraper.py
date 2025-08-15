from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
from datetime import datetime

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

def extract_product_info(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={USER_AGENT}")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    product_info = {'URL': url}

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 2)

        # Product Title
        try:
            title_element = wait.until(EC.presence_of_element_located((By.ID, 'productTitle')))
            product_info['Title'] = title_element.text.strip()
        except TimeoutException:
            product_info['Title'] = "Title not found"

        # Price
        try:
            price_whole = driver.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
            try:
                price_fraction = driver.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text
                full_price = f"{price_whole}.{price_fraction}"
            except NoSuchElementException:
                full_price = price_whole
            product_info['Price'] = full_price
        except NoSuchElementException:
            product_info['Price'] = "Price not found"

        # Rating
        try:
            rating_span = wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, '#acrPopover span.a-size-base.a-color-base'
            )))
            product_info['Rating'] = rating_span.text.strip()
        except TimeoutException:
            product_info['Rating'] = "Rating not found"

        # Technical Details (as key-value pairs)
        tech_specs = {}
        try:
            table = driver.find_element(By.ID, 'productDetails_techSpec_section_1')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                try:
                    key = row.find_element(By.TAG_NAME, 'th').text.strip()
                    value = row.find_element(By.TAG_NAME, 'td').text.strip()
                    tech_specs[key] = value
                except NoSuchElementException:
                    continue
            product_info['Technical_Details'] = json.dumps(tech_specs)  # store as JSON string
        except NoSuchElementException:
            product_info['Technical_Details'] = "{}"

    finally:
        driver.quit()

    return product_info


# Main program
if __name__ == "__main__":
   
    current_date = datetime.now().strftime("%m-%d-%Y")
    output_filename = f"output-{current_date}.csv"

    with open('Amazon_product_Urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        product_urls = [row[0] for row in reader]

    # Get headers from first product info to ensure all keys are present
    first_product_info = extract_product_info(product_urls[0])
    fieldnames = list(first_product_info.keys())

    # Write data to CSV
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write and print first product info
        writer.writerow(first_product_info)
        print(f"📦 Title: {first_product_info['Title']}")
        print(f"💵 Price: {first_product_info['Price']}")
        print("-" * 50)

        # Process and print remaining URLs
        for url in product_urls[1:]:
            product_info = extract_product_info(url)
            writer.writerow(product_info)
            print(f"📦 Title: {product_info['Title']}")
            print(f"💵 Price: {product_info['Price']}")
            print("-" * 50)

    print(f"✅ Data extraction complete. Saved to {output_filename}")

