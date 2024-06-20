import requests
from pprint import pprint
from bs4 import BeautifulSoup

site_data = requests.get("https://www.varzesh3.com").text
soup = BeautifulSoup(site_data, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.title.parent)
# print(soup.title.parent.text)
# print(soup.title.parent.text)
# print(soup.find('a'))  # document.querySelector !support-selector -> Search by tag and attrs
# print(soup.select_one('a'))  # document.querySelector
# print(len(soup.find_all('a')))  # document.querySelectorAll
# print(len(soup.select('a')))  # document.querySelectorAll
# print(soup)
# print(soup.find_all("#new .videobox > a.title")
# print(soup.find("div", id="new").find_all("div", {"class": "videobox"}))

data = [{"link": a['href'], "title": a.text} for a in soup.select("#new a.title")]

pprint(data)
