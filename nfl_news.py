#the following scripts fetches titles fo the latest news articles 
#from a sports news website nfl.com
#Algorithn:
#1. Make a request to the website
#2. Create a Beautifulsoup object
#3. find all the articles
#4. Print the titles

import requests
from bs4 import BeautifulSoup

nfl_url = "https://www.nfl.com/news/"
nfl_response = requests.get(nfl_url)

nfl_soup = BeautifulSoup(nfl_response.content, "html.parser")

nfl_news_titles = nfl_soup.find_all("h3", class_ ="d3-o-media-object__title")

for title in nfl_news_titles:
    print(title.text.strip())

