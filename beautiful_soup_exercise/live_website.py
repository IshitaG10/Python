import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
content = response.text

ycb_content = BeautifulSoup(content, "html.parser")

articles = ycb_content.find_all(name="span", class_="titleline")
article_title = []
article_links = []
article_votes = [score.getText().split()[0] for score in ycb_content.find_all(name="span", class_="score")]
for article in articles:
    text = article.getText()
    article_title.append(text)
    link = article.find("a").get("href")
    article_links.append(link)

max_votes_ind = article_votes.index(max(article_votes))
print("Most popular Article")
print(f"Name: {article_title[max_votes_ind]}")
print(f"Link: {article_links[max_votes_ind]}")