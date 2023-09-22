import requests
import smtplib

EMAIL = "pythonpracticemail23@gmail.com"
PASSWORD = "fgsjbvldkvfdnvlvsd"


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "sfavbijboboj"
parameters = {
    "lat" : 31.1042,
    "lon" : 77.171,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()['hourly']
will_rain = "False"
for i in range(0,12):
    if data[i]['weather'][0]['id']<700:
        will_rain = "True"

if will_rain:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr= EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Weather Alert\n\nBring an umbrella."
            )
        print("sent")
