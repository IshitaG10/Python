from bs4 import BeautifulSoup
import requests

def get_data():
    URL = "https://appbrewery.github.io/Zillow-Clone/"
    response = requests.get(url=URL)
    content = response.text
    zillow_web_page = BeautifulSoup(content, "html.parser")
    properties = zillow_web_page.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
    property_links = [link.get("href") for link in properties]
    property_address = [(address.getText()).strip("\n ") for address in properties]
    prices = zillow_web_page.find_all(name = "span" ,class_ = "PropertyCardWrapper__StyledPriceLine")
    property_prices = [(price.getText()).strip("+ 1 /mobd") for price in prices]
    return property_address, property_prices, property_links

 