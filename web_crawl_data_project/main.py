
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

def crawl_book_prices():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://books.toscrape.com/")
    time.sleep(2)

    price_elements = driver.find_elements(By.CSS_SELECTOR, ".product_price .price_color")
    print("Dữ liệu thu được:")

    for price_element in price_elements:
        price_text = price_element.text.replace('£', '').strip()
        price = float(price_text)
        discount_percent = random.choice([0, 5, 10, 20, 30, 50])
        expected_result = round(price * (1 - discount_percent / 100), 2)
        print(f"Price: {price} | Discount: {discount_percent}% | Expected Result: {expected_result}")

    driver.quit()

if __name__ == "__main__":
    crawl_book_prices()
