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
PASSWORD = os.getenv("TWITTER_PW")
USERNAME = os.getenv("TWITTER_UN")

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        privacy_policy = self.driver.find_element(By.ID, value = "onetrust-accept-btn-handler")
        privacy_policy.click()
        start = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return download_speed, upload_speed
    def tweet_at_provider(self,down,up):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        email_id = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_id.send_keys(EMAIL_ID)
        next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()
        time.sleep(2)
        try:
            password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(2)
        except NoSuchElementException:
            user_name = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            user_name.send_keys(USERNAME)
            user_name.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text = f"Hey Internet Provider, why is my internet speed {down}down/{up}up when I am paying for {self.down}down/{self.up}up?"
        tweet.send_keys(text)
        # post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div')
        # post.click()
        self.driver.quit()

bot = InternetSpeedTwitterBot()
download_speed,upload_speed = bot.get_internet_speed()
bot.tweet_at_provider(download_speed,upload_speed)
