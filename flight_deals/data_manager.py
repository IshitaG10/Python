import requests
#------------------ENVIRONMENT VARIABLE------------------------------
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

#--------------------SHEETY API-----------------------------------------
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT_FLIGHTDEALS")
SHEETY_ENDPOINT_USERS = os.getenv("SHEETY_ENDPOINT_USERS")
BEARER = os.getenv("BEARER")

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT,headers=headers)
        response.raise_for_status()
        data = response.json()['sheet1']
        return data

    def get_cities(self):
        cities=[]
        for item in self.data:
            city = item['city'].lower()
            cities.append(city)
        return cities
    
    def put_iata_code(self,iata_codes):
        for i in range(len(iata_codes)):
            url = f"{SHEETY_ENDPOINT}/{i+2}"
            item = self.data[i]
            if item['iataCode'] == "":
                item['iataCode'] = iata_codes[i]
                update_data = {
                    'sheet1': item
                }
                requests.put(url=url,json=update_data,headers=headers)
                
    def get_customer_details(self):
        response = requests.get(url=SHEETY_ENDPOINT_USERS,headers=headers)
        response.raise_for_status()
        data = response.json()['users']
        return data

            


