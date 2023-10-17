from flask import Flask
import requests
from bs4 import BeautifulSoup
import json
from flask_cors import CORS, cross_origin

#flask is not cooperating with me tonight
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def nfl_news():
    nfl_url = "https://www.nfl.com/news/"
    nfl_response = requests.get(nfl_url)

    nfl_soup = BeautifulSoup(nfl_response.content, "html.parser")

    nfl_news_titles = nfl_soup.find_all("h3", class_ ="d3-o-media-object__title")

    news_headlines = []
    for title in nfl_news_titles:
        news_headlines.append(title.text.strip())
        #print(title.text.strip())

    return json.dumps(news_headlines) 


if __name__ == "__main__":
	#app.run()
    app.run(host='0.0.0.0', port=9000)

