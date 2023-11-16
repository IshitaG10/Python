from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program is done running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value= "#articlecount a").text
print(article_count)

driver.quit()
