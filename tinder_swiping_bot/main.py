from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

EMAIL_ID = os.getenv("MY_GMAIL")
PASSWORD = os.getenv("FACEBOOK_PW")

#----------------------SELENEIUM-----------------------------------
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://tinder.com/app/recs")
time.sleep(3)
#--------logging in------------------------
log_in = driver.find_element(By.XPATH, value='//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()
time.sleep(2)
try:
    more_options = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_options.click()
    time.sleep(2)
except NoSuchElementException:
    pass
fb_login = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
fb_login.click()
time.sleep(4)

#---------------fb login page----------------------
base_window = driver.window_handles[0]
fb_login_page = driver.window_handles[1]
driver.switch_to.window(fb_login_page)
input_email = driver.find_element(By.ID, value="email")
input_email.send_keys(EMAIL_ID)
input_email = driver.find_element(By.ID, value="pass")
input_email.send_keys(PASSWORD)
input_email.send_keys(Keys.ENTER)
time.sleep(5)

#---------------SWIPING-------------------
driver.switch_to.window(base_window)
accept_cookies = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_cookies.click()
time.sleep(3)
allow_loc = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_loc.click()
time.sleep(3)
notification = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification.click()
time.sleep(5)


for i in range(10):
    try:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
        time.sleep(2)

    except NoSuchElementException:
        time.sleep(3)
        continue