#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

notification_manager = NotificationManager()

sheet_data_manager = DataManager()
cities = sheet_data_manager.get_cities()
customer_data = sheet_data_manager.get_customer_details()


flight_search = FlightSearch(cities)
iata_codes = flight_search.get_IATA()

sheet_data_manager.put_iata_code(iata_codes)
sheet_data = sheet_data_manager.get_data()

for item in sheet_data:
    flight = flight_search.get_flight_price(ORIGIN_CITY_CODE,item["iataCode"])
    if flight == None:
        continue
    if item['lowestPrice'] > flight.price:
        for item in customer_data:
            email = item['email']
            notification_manager.send_mail(flight,email)
        