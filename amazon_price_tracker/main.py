import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_gmail = os.getenv("MY_GMAIL")
my_password = os.getenv("MY_PASSWORD")


URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9",

}


response = requests.get(url=URL,headers=headers)
response.raise_for_status()
web_page = response.text

amazon_soup = BeautifulSoup(web_page, "lxml")
price = float(((amazon_soup.select(selector="span .a-offscreen" )[1]).getText()).strip("$"))
product_name = ((amazon_soup.find(name = "span", id = "productTitle" )).getText()).strip()


if price< 300:
    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail,password=my_password)
        connection.sendmail(from_addr=my_gmail,to_addrs=my_gmail,msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}.\n{URL}")
