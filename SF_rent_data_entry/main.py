from web_scraping import get_data
from data_entry import data_entering

address, price, link = get_data()
length = len(address)
data_entering(address,price,link,length)
