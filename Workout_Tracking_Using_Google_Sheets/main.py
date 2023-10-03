import requests
from datetime import datetime


#------------------ENVIRONMENT VARIABLE------------------------------
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

#---------------------------DATE AND TIME--------------------------------
now = datetime.now()
date  = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

#-------------------------------NUTRITIONIX API ACCESS----------------------------
API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY
}

user_input = input("Tell me which exercises you did: ")

params = {
    "query" : user_input,
    "gender" : "female",
    "weight_kg" : 51,
    "height_cm" : 167,
    "age" : 20
}

response = requests.post(url= API_ENDPOINT,json= params,headers=headers)
response.raise_for_status()
data = response.json()


#--------------------------------SHEETY API ACCESSS----------------------------------------------
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
BEARER = os.getenv("BEARER")

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}

for exercise in data['exercises']:
    workout_data = {
        "sheet1":{
            "date" : date,
            "time" : time,
            "exercise" : exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url = SHEETY_ENDPOINT,json=workout_data,headers=headers)
    print(sheety_response.status_code)
    print(sheety_response.text)