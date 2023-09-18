##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import datetime as dt
import random
import smtplib


# RANDOM_INT = random.randint(1,3)
EMAIL = "pythonpracticemail23@gmail.com"
PASSWORD = "cfisbdclaclhlln"
PLACEHOLDER = "[NAME]"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=EMAIL,password=PASSWORD)

df = pd.read_csv("Birthday Wisher\\birthdays.csv")

today = dt.datetime.now()
date_today = [today.month,today.day]


new_df = df[(df["month"] == date_today[0]) & (df["day"] == date_today[1])]

if new_df is not None:
    names = list(new_df.name)
    email = list(new_df.email)
    
    for i in range(len(new_df)):
        random_int  = random.randint(1,3)
        with open(f"Birthday Wisher\letter_templates\letter_{random_int}.txt",'r') as letter:
            letter_text = letter.read()
        letter_text = letter_text.replace(PLACEHOLDER,names[i])
        connection.sendmail(from_addr=EMAIL,to_addrs=email[i],msg=f"Subject: Happy Birthday\n\n{letter_text}")
        print("sent")

connection.close()