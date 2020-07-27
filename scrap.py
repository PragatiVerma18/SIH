import requests
import json
from bs4 import BeautifulSoup
import csv

url = 'https://www.classcentral.com/report/swayam-moocs-course-list/'
response = requests.get(url).content.decode()

soup = BeautifulSoup(response, 'html.parser')
table = soup.find("div", {"class": "articleContent"})
rows = table.find_all("li")
links_with_text = []
# for i in rows:
#     links = i.a.attrs['href']
#     provider = i.find('em')
#     rating = i.text
# print(rating)
# print(link, provider, rating)

for i in rows[14:]:
    data = {}
    data['link'] = i.a.attrs['href']
    if i.find('em'):
        data['provider'] = i.find('em').text
    else:
        data['provider'] = ''
    if i.text:
        data['rating'] = i.text
    else:
        data['rating'] = ''
    # data['rating'] = i.text
    links_with_text.append(data)

# print(links_with_text)

with open("data.json", "w") as writeJSON:
    json.dump(links_with_text, writeJSON, ensure_ascii=False)
# print(rows)
