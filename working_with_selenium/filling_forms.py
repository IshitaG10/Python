from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program is done running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# link = driver.find_element(By.LINK_TEXT, value= "View history")
# link.click()

# search_bar = driver.find_element(By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Ishita")
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Gupta")
email= driver.find_element(By.NAME, value="email")
email.send_keys("ig@gkjbl.com")
submit_button = driver.find_element(By.CLASS_NAME, value="btn-primary")
submit_button.click()