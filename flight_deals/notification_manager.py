import smtplib
from flight_data import FlightData
#------------------ENVIRONMENT VARIABLE------------------------------
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_gmail = os.getenv("MY_GMAIL")
my_password = os.getenv("MY_PASSWORD")

class NotificationManager:

    def send_mail(self,flight:FlightData,email):
        if flight.stop_overs == 0:
            content = f"FLIGHT INFORMATION:\nPrice: £{flight.price}\nOrigin City:{flight.origin_city}\nOrigin Airport Code:{flight.origin_airport}\nDestination City:{flight.destination_city}\nDestination Airport:{flight.destination_airport}\nOut Date: {flight.out_date}\nReturn Date:{flight.return_date}"
            with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                connection.starttls()
                connection.login(user=my_gmail,password=my_password)
                connection.sendmail(from_addr=my_gmail,to_addrs=email,msg=f"Subject:Price dropped for flight to {flight.destination_city}\n\n{content}".encode("utf-8"))
        else:
            content = f"FLIGHT INFORMATION:\n{flight.price}\nOrigin City:{flight.origin_city}\nOrigin Airport Code:{flight.origin_airport}\nDestination City:{flight.destination_city}\nDestination Airport:{flight.destination_airport}\nStop Over: {flight.stop_overs}\nVia City: {flight.via_city}\nOut Date: {flight.out_date}\nReturn Date:{flight.return_date}"
            with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                connection.starttls()
                connection.login(user=my_gmail,password=my_password)
                connection.sendmail(from_addr=my_gmail,to_addrs=email,msg=f"Subject:Price dropped for flight to {flight.destination_city}\n\n{content}".encode("utf-8"))

