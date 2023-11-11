import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

web_page_content = BeautifulSoup(content,"html.parser")
all_movies = web_page_content.find_all(name = "h3", class_ = "title")
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]
with open("top_100_movies\\100_movies.txt", mode = "w", encoding= 'utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
    


