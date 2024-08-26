import requests
from bs4 import BeautifulSoup

file = open("recette.html", "r")
html_content = file.read()
file.close()

soup = BeautifulSoup(html_content, "html.parser")

title_h1 = soup.find("h1")
list_div_center = soup.find_all("div", class_="centre")
description = list_div_center[1].find("p", class_="description")

div_info = soup.find("div", class_="info")
image = div_info.find("img")

print(f"Title of the html page: {title_h1.text}")
print(f"Paragraph of the description: {description.text}")

print(f"src of the image is: {image['src']}")
