import requests
import urllib.parse
import json

google_news = "https://news.google.com/news?cf=all&hl=en&pz=1&ned=en_ke&output=rss"
google_news_url = "https://ajax.googleapis.com/ajax/services/feed/load?v=1.0&q=%s" % urllib.parse.quote(google_news)

response = requests.get(google_news_url)

if response.status_code == 200:
    news = json.loads(response.content.decode("utf-8"))
    for new in news['responseData']['feed']['entries']:
        print(new['title'])
