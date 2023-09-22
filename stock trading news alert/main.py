import requests
from datetime import date,timedelta
import math
import smtplib
import html

EMAIL = "pythonpracticemail23@gmail.com"
PASSWORD = "dcWBIFUVCIWKKbjxh"

STOCK = "AMZN"
COMPANY_NAME = "amazon"
STOCK_API_KEY = "dcWBIFUVCIWKKbjxh"
NEWS_API_KEY = "dcWBIFUVCIWKKbjxh"

#Getting date

# Today date
today = date.today()
 
# Yesterday date
yesterday = str(today - timedelta(days = 2))
day_before_yesterday = str(today - timedelta(days = 3))


stock_pararmeters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "q" : COMPANY_NAME,
    "from" : yesterday,
    "to" : yesterday,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

connection = smtplib.SMTP("smtp.gmail.com",port=587) 
connection.starttls()
connection.login(user=EMAIL,password=PASSWORD)

#retreiving stock data from API
response = requests.get(url ="https://www.alphavantage.co/query",params=stock_pararmeters)
response.raise_for_status()

#getting data
stock_data = response.json()['Time Series (Daily)']
latest_closing_price = float(stock_data[yesterday]['4. close'])
previous_closing_price = float(stock_data[day_before_yesterday]['4. close'])

#calculating increase/decrease
symbol=""
change_percent = math.floor(((latest_closing_price-previous_closing_price)/previous_closing_price)*100)
if change_percent <0:
    change_percent = -1 * change_percent
    symbol = "🔻"
else:
    headline_text = "🔺"

#sending mail
if change_percent>=5:
    #retrieving data from news API
    news = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
    news.raise_for_status()
    news_data = news.json()
    sliced_news_data =news.json()['articles'][:3]


    for i in range(len(sliced_news_data)):
        headline = sliced_news_data[i]['title']
        description = sliced_news_data[i]['description']
        connection.sendmail(
            from_addr= EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:AMZN: {symbol}{change_percent}%\n\nHeadline:{headline}\nBreif:{description}".encode('utf-8')
            )
        print("sent")
connection.close()

