import requests 
import json
from datetime import date
from dateutil.relativedelta import relativedelta
import urllib.parse
from flight_data import FlightData

#------------------ENVIRONMENT VARIABLE------------------------------
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

#------------------TEQUILA API------------------------------

TEQUILA_API_LOCATION_ENDPOINT = os.getenv("TEQUILA_API_LOCATION_ENDPOINT")
headers={
        "apikey" : os.getenv("TEQUILA_API_KEY")
        }


TEQUILA_API_SEARCH_ENDPOINT = os.getenv("TEQUILA_API_SEARCH_ENDPOINT")
headers={
        "apikey" : os.getenv("TEQUILA_API_KEY")
        }


class FlightSearch:
    def __init__(self,terms):
        self.terms = terms
        
    def get_IATA(self):
        iata_code = []
        for term in self.terms: 
            query ={
                'term' : term,
                'location_types' : "city"
            } 
            response = requests.get(url=TEQUILA_API_LOCATION_ENDPOINT,params=query,headers=headers)
            response.raise_for_status()
            data = response.json()['locations'][0]['code']
            iata_code.append(data)
        return iata_code
    
    def get_flight_price(self,origin_city_code,destination_city_code):
        stop_over = 0
        from_time = date.today()
        to_time = date.today() + relativedelta(months=+6)

        query = {
                "fly_from" : origin_city_code,
                "fly_to" : destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
        }

        #used to escape the error of '/' converting to '%2F' in date
        query_str = urllib.parse.urlencode(query, safe='/')

        response = requests.get(url=TEQUILA_API_SEARCH_ENDPOINT,params=query_str,headers=headers)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            
        except IndexError:
            stop_over = 1
            query = {
                "fly_from" : origin_city_code,
                "fly_to" : destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 2,
                "curr": "GBP"
            }
            query_string = urllib.parse.urlencode(query, safe='/')
            response = requests.get(url=TEQUILA_API_SEARCH_ENDPOINT,params=query_string,headers=headers)
            try:
                data = response.json()["data"][0]
                
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs=stop_over,
            via_city=data["route"][0]["cityTo"]
        )
        return flight_data