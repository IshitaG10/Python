import requests
from datetime import datetime,timezone
import smtplib
import time

MY_LAT = 31.104605
MY_LONG = 77.173424
EMAIL = "pythonpracticemail23@gmail.com"
PASSWORD = "kkaneeurilqqekfl"



def iss_is_overhead():
    data = requests.get(url = "http://api.open-notify.org/iss-now.json")
    data.raise_for_status()
    #iss position
    iss_longitude = float(data.json()["iss_position"]["latitude"])
    iss_latitude = float(data.json()["iss_position"]["longitude"])
    if (MY_LAT-5<=iss_latitude<MY_LAT+5) and (MY_LONG-5<=iss_longitude<MY_LONG+5) :
        return True

def is_nighttime():

    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()


    #we get time in UTC 
    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    #local time in UTC
    time_now = datetime.now(timezone.utc).hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if iss_is_overhead() and is_nighttime():
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr= EMAIL,
            to_addrs=EMAIL,
            msg="Subject: LOOK UP\n\nThe ISS is above you in the sky."
            )
