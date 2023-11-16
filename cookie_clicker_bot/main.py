from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# keep chrome browser open after program is done running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")


timeout = time.time() + 60*5
start_time = time.time()

while True:
    cookie.click()
    now_time = time.time()
    elapsed_time = now_time-start_time

    if timeout < time.time():
        break
    if elapsed_time>=5:
        cookie_num = int(((driver.find_element(By.ID, value="money").text).replace(",","")).strip(""))
        store_list = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = []

        for item in store_list:
            if item.text != "":
                price = ((item.text.split("-")[1]).replace(",","")).strip("")
                prices.append(int(price))

        purchasable = [price for price in prices if price<=cookie_num]
        buy_item_index = prices.index(max(purchasable))
        store_list[buy_item_index].click()
        start_time = time.time()

cookie_per_sec = driver.find_element(By.ID, value="cps").text
print(cookie_per_sec)

driver.quit()