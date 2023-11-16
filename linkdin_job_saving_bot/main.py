from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

EMAIL_ID = os.getenv("MY_GMAIL")
PASSWORD = os.getenv("LINKED_IN_PW")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3680980761&f_E=1%2C2&geoId=102713980&keywords=Python%20Developer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()
email_input = driver.find_element(By.ID, value = "username")
email_input.send_keys(EMAIL_ID)
password_input = driver.find_element(By.ID, value= "password")
password_input.send_keys(PASSWORD)
submit_button = driver.find_element(By.CSS_SELECTOR, value=" form button")
submit_button.click()
time.sleep(10)

jobs = driver.find_elements(By.CLASS_NAME, value="job-card-list__title")
for job in jobs:
    job.click()
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR,value='.jobs-save-button')
    save_button.click()
    follow_button = driver.find_element(By.CLASS_NAME, value="follow")
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();",follow_button)
    follow_button.click()
    time.sleep(2)