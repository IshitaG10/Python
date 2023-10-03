import requests
from datetime import datetime

TOKEN = "h3hori09vow94rrhc93fh792"
USERNAME = "ishitag10"
headers = {
    "X-USER-TOKEN" : TOKEN
}
GRAPH_ID = "graph1rt"
#_______________________________ CREATING ACCOUNT________________________________

pixela_endpoint = "https://pixe.la/v1/users"

# user_params ={
#     "token": TOKEN,
#     "username" : USERNAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
# }

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)



#______________________________________CREATING GRAPH____________________________________

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config={
#   "id":"graph1rt",
#   "name": "Coding Graph",
#   "unit" : "hr",
#   "type" : "int",
#   "color" : "ajisai"

# }


#CREATING GRAPH 
# response = requests.post(url = graph_endpoint,json=graph_config,headers = headers)
# print(response.text)

#_______________________________POSTING A PIXEL_________________________________

# API_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()

# pixel_post_params = {
#     "date" : today.strftime("%Y%m%d"),
#     "quantity" : "2"
# }

# response = requests.post(url = API_endpoint, json= pixel_post_params,headers = headers)
# print(response.text)

#__________________________________UPDATING A PIXEL_____________________________

API_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231003"

# update_params = {
#     "quantity": "4"
# }

# response = requests.put(url = API_endpoint,json=update_params,headers=headers)
# print(response.text)

#_________________________________DELETING A PIXEL_______________________
response = requests.delete(url=API_endpoint,headers=headers)
print(response.text)