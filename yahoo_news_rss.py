import requests
import datetime


def savexml(topic):
    URL = f"https://news.yahoo.co.jp/rss/topics/{topic}.xml"
    r = requests.get(URL)
    with open("test.xml", "a") as f:
        f.write(r.text)


savexml("it")
