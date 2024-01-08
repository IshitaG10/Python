import requests

class Post:
    def __init__(self):
        self.response = requests.get(url = "https://api.npoint.io/31a2c4a8ff45a8cf362e")
        self.blogs = self.response.json()