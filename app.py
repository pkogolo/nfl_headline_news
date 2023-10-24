#THE ORIOGINAL CODE THAT WORKS BELOW

from flask import Flask
import requests
from bs4 import BeautifulSoup
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def nfl_news():
    nfl_url = "https://www.nfl.com/news/"
    nfl_response = requests.get(nfl_url)
    nfl_soup = BeautifulSoup(nfl_response.content, "html.parser")
    nfl_news_titles = nfl_soup.find_all("h3", class_ ="d3-o-media-object__title")
    nfl_news_details = nfl_soup.find_all("div", class_ = "d3-o-media-object")
    
    

    news_headlines = []  # an empty list
    for title, news in zip(nfl_news_titles, nfl_news_details):  # use zip to iterate through two lists simultaneously
        news_dict = {}  # An empty dictionary
        title_text = title.text.strip()
        news_dict["headline"] = title_text  # creating a dictionary key called "headline" with the value title_text
        links = news.find("a")
        hrefs = links["href"]
        main_link = "https://www.nfl.com" + hrefs  # fix the URL construction
        news_dict["link"] = main_link  # Creating a dictionary key called "link" with the value main_link
        news_headlines.append(news_dict)
        print(main_link, "\n")  # change to main_link instead of hrefs


    return json.dumps(news_headlines) 


if __name__ == "__main__":
	#app.run()
    app.run(host='0.0.0.0', port=9000)

