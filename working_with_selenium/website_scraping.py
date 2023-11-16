from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org")

event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
upcoming_events = {}

for i in range(len(event_time)):
   upcoming_events[i] = {
      'time' : event_time[i].text,
      'name' : event_name[i].text
   }

print(upcoming_events)
driver.quit()
