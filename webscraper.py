from bs4 import BeautifulSoup

import requests

import csv

URL = 'https://www.vocabulary.com/lists/52473'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

words = []
definitions = []

with open("data.csv", "w", newline='', encoding="utf-8") as data:

    writer = csv.writer(data)

    for word in soup.find_all(class_ = "word dynamictext"):
        words.append(word.text)
        
    for definition in soup.find_all(class_ = "definition"):
        definitions.append(definition.text)

    for i in range(len(words)):
        writer.writerow([words[i], definitions[i]])

