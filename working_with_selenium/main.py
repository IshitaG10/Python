from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program is done running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#----------------Getting price from amazon---------------------
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/")

# price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

#-------------Using another way to find elements in webpage---------------------
driver.get("https://python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute('type'))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# print(button.get_attribute("title"))

# documentation = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation.text)

bug_submission = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_submission.get_attribute("href"))

#drive.close()   #closes the tab opened
driver.quit()   #closes the browser