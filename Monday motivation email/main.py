import smtplib
import datetime as dt
import random

my_gmail = "pythonpracticemail23@gmail.com"
my_password = "cfisbdclaclhlln"

date_time = dt.datetime.now()

if date_time.weekday() == 0:
    with open("Monday motivation email\quotes.txt",'r') as file:
        data =  file.readlines()
        quote = random.choice(data)
    print("sent")
    with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail,password=my_password)
        connection.sendmail(from_addr=my_gmail,to_addrs="xyz@gmail.com",msg=f"Subject:Motivational Quote\n\n{quote}")