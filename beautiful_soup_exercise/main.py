from bs4 import BeautifulSoup

with open("beautiful_soup_exercise\website.html") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)
# print(soup.prettify())

# all_anchors = soup.find_all(name='a')
# print(all_paragraphs)

# for tag in all_anchors:
    # print(tag)
    # print(tag.get("href"))

# heading = soup.find(name='h1',id = 'name')
# print(heading.getText())

# class_heading = soup.find_all(class_ = 'heading')
# print(class_heading)

# section_heading = soup.find(name='h3', class_ = 'heading')
# print(section_heading.getText())
# print(section_heading.name)

# link = soup.select_one(selector="p a")
# print(link)

id_selector = soup.select_one(selector="#name")
print(id_selector)

class_selector = soup.select(".heading")
print(class_selector)
